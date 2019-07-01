const {Client} = require('pg')
const client = new Client({
    user: "postgres",
    password: "user56",
    host: "localhost",
    database: "db_zoldyck",
    port: 5432
})

client.connect()