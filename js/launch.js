const {Client} = require('pg')
const client = new Client({
    user: "postgres",
    password: "user56",
    host: "localhost",
    database: "db_zoldyck",
    port: 5432
})
var http = require('http').createServer(webServer),
    form = require('fs').readFileSync('launch.html'),
    querystring = require('querystring'),
    util = require('util'),
    dataString = ''

function webServer(req, res){
    if(req.method == 'GET'){
        res.writeHead(200,{'Content-Type': 'text/html'})
        res.end(form)
    }
    if(req.method = 'POST'){
        req
            .on('data', function(data){
            dataString += data
        })
            .on('end',function(){
            executeprojects()
        })
    }
}
http.listen(3000)

async function executeprojects(){
    try{
        await client.connect()
        console.log("Connected successfully.")
        client.query("BEGIN")
        client.query("INSERT into VIDEOJUEGO values ($1,$2,$3,$4,$5)",[getElementById(),,,,])
        client.query("COMMIT")
    }
    catch(ex){
        console.log('Ups! Something wrong happened. '+ ex)
        client.query("ROLLBACK")
    }
    finally{
        await client.end()
        console.log("Client disconnected successfully.")
    }
}