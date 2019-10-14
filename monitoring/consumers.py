import asyncio
import select
import psycopg2
import psycopg2.extensions
from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.db.models.signals import post_save
import OpenOPC, psycopg2
from time import sleep
import pywintypes
from channels.db import database_sync_to_async
import json



class MonitoringConsumer(AsyncConsumer):
	
	async def websocket_connect(self, event):
		print ('connection successfull', event)
		
		await self.send({
			'type': 'websocket.accept'
			})



	async def websocket_receive(self, event):

		

		print (event.get("text"))


		
		while True:

			var = await self.connectOPC(event)	
			await self.send({
			'type': 'websocket.send',
			'text': var,
			})

		

		




	@database_sync_to_async
	def connectOPC(self,event):

		eventValue = event.get("text").split(',')
		print(eventValue)
		
		nameServer = eventValue[0]
		nameTag = eventValue[1]

		print(nameServer,nameTag)

		con = psycopg2.connect("host='localhost' dbname='postgres' user='postgres' password='Direling2017'")   
		cur = con.cursor()

		pywintypes.datetime = pywintypes.TimeType

		opc=OpenOPC.client()
		opc.connect(nameServer)
		tag = nameTag
		ID = 0


		cur.execute(f"delete from orders")


		while True:
			value = opc.read(tag)
			cur.execute(f"INSERT INTO orders VALUES({ID},{value[0]});")
			
			con.commit()
			sleep(1)

			ID = ID + 1

			print (ID)

			json_array = json.dumps({'value' : value,'id' : ID})
			

			return json_array

		con.close()

	@database_sync_to_async
	def get_data_opc(self,event):


		print("CONNECT")
		conn = psycopg2.connect("host='localhost' dbname='postgres' user='postgres' password='Direling2017'")
		conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

		curs = conn.cursor()
		curs.execute("LISTEN events;")

		print ("Waiting for notifications on channel 'DatasetOPC'")

		if select.select([conn],[],[],2) == ([],[],[]):
			print ("Timeout")
		else:
			conn.poll()
			while conn.notifies:
				notify = conn.notifies.pop(0)
				print(notify)
				return (notify.payload)