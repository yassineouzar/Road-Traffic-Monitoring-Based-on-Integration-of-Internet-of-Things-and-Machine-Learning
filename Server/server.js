const http = require('http');
const fs = require('fs');
const path = require('path');
const url = require('url');
const querystring = require('querystring');
const child_process = require('child_process');
const net = require('net');



s = http.createServer(function (request, response) {	// Create a server
	console.log("Requested URL: " + request.url);
	var pathname = url.parse(request.url).pathname;
	if (request.url === '/') {
		fs.readFile('html/index.htm', function (err, data) {
			if (err) {
				console.log(err);
				response.writeHead(404, { 'Content-Type': 'text/html' }); response.end('404 Page Not Found');
			}
			else {
				response.writeHead(200, { 'Content-Type': 'text/html' });
				response.write(data.toString()); response.end();
			}
		});
	}
	else if (request.url.match(/.htm$/)) {
		fs.readFile('html' + request.url, function (err, data) {
			if (err) {
				console.log(err);
				response.writeHead(404, { 'Content-Type': 'text/html' }); response.end('404 Page Not Found');
			}
			else {
				response.writeHead(200, { 'Content-Type': 'text/html' });
				response.write(data.toString()); response.end();
			}
		});
	}
	else if (request.url.match(/.js$/)) {
		var jsPath = path.join(__dirname, 'Js', request.url);
		var fileStream = fs.createReadStream(jsPath, "UTF-8");
		response.writeHead(200, { 'Content-Type': 'text/javascript' });
		fileStream.pipe(response);
	}
	else if (request.url.match(/.css$/)) {
		/*var cssPath = path.join(__dirname, 'Styles', request.url);
		var fileStream = fs.createReadStream(cssPath, "UTF-8");
		response.writeHead(200, {'Content-Type': 'text/css'});
		fileStream.pipe(response);*/
		fs.readFile('Styles' + request.url, function (err, data) {
			if (err) {
				console.log(err);
				response.writeHead(404, { 'Content-Type': 'text/html' }); response.write('404 Page Not Found');
			}
			else {
				response.writeHead(200, { 'Content-Type': 'text/css' });
				response.write(data.toString()); response.end();
			}
		});
	}
	else if (request.url.match(/.(png|jpg|ico)$/)) {
		var imgPath = path.join(__dirname, 'Img', request.url);
		var imgStream = fs.createReadStream(imgPath);
		response.writeHead(200, { 'Content-Type': 'image/png' });
		imgStream.pipe(response);
	}

	else if (request.url.match(/.mp4$/)) {
		var vidPath = path.join(__dirname, 'Media', request.url);

		fs.stat(vidPath, function(err, stats) {
		if (err) {
			if (err.code === 'ENOENT') {
			// 404 Error if file not found
			return response.sendStatus(404);
			}
			response.end(err);
		}

		var range = request.headers.range;
		if (!range) {
		// 416 Wrong range
			return response.sendStatus(416);
		}
		var positions = range.replace(/bytes=/, "").split("-");
		var start = parseInt(positions[0], 10);
		var total = stats.size;
		var end = positions[1] ? parseInt(positions[1], 10) : total - 1;
		var chunksize = (end - start) + 1;

		response.writeHead(206, {
			"Content-Range": "bytes " + start + "-" + end + "/" + total,
			"Accept-Ranges": "bytes",
			"Content-Length": chunksize,
			"Content-Type": "video/mp4"
		});

		var stream = fs.createReadStream(vidPath, { start: start, end: end })
			.on("open", function() {stream.pipe(response);}) .on("error", function(err) {response.end(err);});

		});
	}

	else { response.writeHead(404, { 'Content-Type': 'text/html' }); response.end('Page Not Found'); }
}).listen(8080);



const WebSocket = require('ws');
const wss = new WebSocket.Server({ server: s });
var sleep;

wss.on('connection', function connection(ws) {
	ws.on('message', function incoming(message) {
		console.log('received: %s', message);
		//var msg = JSON.parse(message);
		// console.log(msg);
		if (message == "launch") {
			child_process.exec('python3 test.py', function (error, stdout, stderr) {
				if (error) {
					console.log(error.stack);
					console.log('Error code: ' + error.code);
					console.log('Signal received: ' + error.signal);
				}
				else {
					console.log("stdout: "+stdout);
					ws.send(stdout)
				}
			});
		}
		if (message == "Count") {
			child_process.exec('python3 Scripts/test.py ', function (error, stdout, stderr) {
				if (error) {
					console.log(error.stack);
					console.log('Error code: ' + error.code);
					console.log('Signal received: ' + error.signal);
				}
				else {
					console.log("stdout: "+stdout);
					ws.send(stdout)
				}
			});
		}
	});
});

console.log('Server running on port 8080');
