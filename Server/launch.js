function activer(){
    console.log("Lauched clicked")
    var wsc = new WebSocket("ws://192.168.43.106:8080");
    wsc.onopen = function(){
        console.log("WebSocket Opened");
        wsc.send("launch");
    }
    wsc.onclose = function(){
        console.log("WebSocket Closed");
    }
    wsc.onmessage = function(res){
        console.log(res.data); 

        temp.innerHTML = res.data;
        wsc.close();
    }
}