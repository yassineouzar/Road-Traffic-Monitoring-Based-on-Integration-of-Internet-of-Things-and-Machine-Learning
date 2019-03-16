function activer1(){
    console.log("Lauched clicked")
    var wsc = new WebSocket("ws://192.168.43.106:8080");
    wsc.onopen = function(){
        console.log("WebSocket Opened");
        wsc.send("Count");
    }
    wsc.onclose = function(){
        console.log("WebSocket Closed");
    }
    wsc.onmessage = function(res){
        console.log(res.data); 
        var temp = document.getElementById("Nombre");
        temp.innerHTML = res.data;
        wsc.close();
    }
}