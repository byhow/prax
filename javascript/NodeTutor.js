const http = require('http');
const os = require('os');
const EventEmitter = require('events');
const emitter = new EventEmitter();
var totalMemory = os.totalmem();

// ES6 above
console.log(`Total memory is ${totalMemory}`);

// arrow function
emitter.on('messageLogged', (arg) => {
    console.log('Listener called', arg);
});

emitter.emit('messageLogged', {id: 1, url: 'http://'});

class Logger {
    log(message) {
        console.log(message);

        this.emit('messageLogged', {id: 1, url: 'http://'});
    }
}

module.exports = Logger;

const server = http.createServer((req, res) => {
    if (req.url === '/') {
        res.write('Hello World!');
        res.end();
    }
    if (req.url === '/api/courses') {
        res.write(JSON.stringify([1, 2, 3]));
        res.end();
    }
});

server.listen(3000);