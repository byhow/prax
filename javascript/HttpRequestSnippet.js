const httpRequest = require('https');

function solution(){
    var res = httpRequest.get('https://en.wikipedia.org/w/api.php?action=parse&section=0&format=json&prop=text&page=pizza', (res) => {
        var data = '';

        res.on('data', (chunk) => {
            data += chunk;
            // console.log(data);
        }) 

        
    }).on("error", (err) => {
        console.log("Error: " + err.message);
    });
    return res;
}

console.log(solution());