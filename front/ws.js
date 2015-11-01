$(function() {
    var exampleSocket = new WebSocket("ws://192.168.31.231:8020/?uid=10012", "protocolOne");

    exampleSocket.onmessage = function(event) {
        $("#chatbox").append("<li>"+"["+Date()+"]"+event.data+"</li>");
    }
});

function sendText() {
    // Construct a msg object containing the data the server needs to process the message from the chat client.
    var msg = {
        type: "message",
        text: document.getElementById("text").value,
        id: clientID,
        date: Date.now()
    };

    // Send the msg object as a JSON-formatted string.
    exampleSocket.send(JSON.stringify(msg));

    // Blank the text input element, ready to receive the next line of text from the user.
    document.getElementById("text").value = "";
}

// exampleSocket.onmessage = function(event) {
//     var f = document.getElementById("chatbox").contentDocument;
//     var text = "";
//     var msg = JSON.parse(event.data);
//     var time = new Date(msg.date);
//     var timeStr = time.toLocaleTimeString();

//     switch (msg.type) {
//         case "id":
//             clientID = msg.id;
//             setUsername();
//             break;
//         case "username":
//             text = "<b>User <em>" + msg.name + "</em> signed in at " + timeStr + "</b><br>";
//             break;
//         case "message":
//             text = "(" + timeStr + ") <b>" + msg.name + "</b>: " + msg.text + "<br>";
//             break;
//         case "rejectusername":
//             text = "<b>Your username has been set to <em>" + msg.name + "</em> because the name you chose is in use.</b><br>"
//             break;
//         case "userlist":
//             var ul = "";
//             for (i = 0; i < msg.users.length; i++) {
//                 ul += msg.users[i] + "<br>";
//             }
//             document.getElementById("userlistbox").innerHTML = ul;
//             break;
//     }

//     if (text.length) {
//         f.write(text);
//         document.getElementById("chatbox").contentWindow.scrollByPages(1);
//     }
// };
