


var socket_url = 'ws://' + window.location.host + window.location.pathname

var socket = new WebSocket(socket_url)

socket.onopen = function (event) {
		console.log('socket opened',event);

		let nameServer = document.getElementById("valueNameServer");
		let nameTag = document.getElementById("valueTag");
		
		document.forms.nameServerForm.onsubmit = function(e) {
			e.preventDefault();
			console.log(nameServer.value);
			array = [nameServer.value,nameTag.value];
			
			socket.send(array);
			
		};

		var get_data_button = document.getElementById("get_data_button");
		document.forms.get_data.onsubmit = function(e) {
			e.preventDefault();

			socket.send("ON")
			
		};
	    

	}

socket.onmessage = function (event) {
    

    var data = event.data;

    

    data_js = JSON.parse(data);

    console.log(data_js)

    value = data_js.value[0]
    console.log(value)


    time = data_js.value[2]

    preparedTime = time.split(' ')
    preparedTime = preparedTime[1].split('+')

    console.log	(preparedTime[0])

    
    addData(myChart, preparedTime[0], value)

}