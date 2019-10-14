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


class ConfigurationConsumer(AsyncConsumer):
	
	async def websocket_connect(self, event):
		print ('connection successfull', event)
		
		await self.send({
			'type': 'websocket.accept'
			})

		


	async def websocket_receive(self, event):

		
		

		await self.connectOPC(event)




		await self.send({
		'type': 'websocket.send',
		'text': text_message,

		})


	def connectOPC(self,event):

		eventValue = event.get("text").split(',')
	
		
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
		    print(value)
		    con.commit()
		    sleep(5)
		    ID+=1

		con.close()

	

