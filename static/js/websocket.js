


var socket_url = 'ws://' + window.location.host + window.location.pathname

var socket = new WebSocket(socket_url)
socket.onopen = function (event) {
    console.log('socket opened',event);
}

socket.onmessage = function (event) {
    console.log(event);

    var data = event.data;

    data_js = JSON.parse(data);

    id = data_js.data.id
    total = data_js.data.total

    console.log(id)
    console.log(total)

    
    addData(myChart, id, total)

}