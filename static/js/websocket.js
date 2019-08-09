


var socket_url = 'ws://' + window.location.host + window.location.pathname

var socket = new WebSocket(socket_url)
    socket.onopen = function (event) {
    console.log('socket opened',event);
}













var ctx = document.getElementById('myChart').getContext('2d');
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'bar',

    // The data for our dataset
    data: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [{
            label: 'My First dataset',
            backgroundColor: '#42B782',
            borderColor: '#42B782',
            data: [0, 10, 5, 2, 20, 30, 45]
        }]
    },

    // Configuration options go here
    options: {}
});





new Vue({
  el: '#example-2',
  data : {
    upHere : false
}
})