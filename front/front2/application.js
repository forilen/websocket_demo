$(function(){
    var location = {
        'host': '192.168.31.231'
    }
    var inbox = new ReconnectingWebSocket("ws://192.168.31.231:8020?uid=10012");

    inbox.onmessage = function(message) {
        $("#message").append('<li>'+message.data+'</li>');
    };
});
