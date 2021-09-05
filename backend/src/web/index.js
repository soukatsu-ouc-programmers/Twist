const express = require('express')
const mongodb = require('mongodb')
const app = express()
const MongoClient = mongodb.MongoClient

const client = new MongoClient(`mongodb://${process.env.MONGO_DB_USERNAME}:${process.env.MONGO_DB_PASSWORD}@${process.env.MONGO_DB_HOST}:27017/?authSource=admin`)

app.get('/', async (req, res) => {
    await client.connect();

    const database = client.db('tweet_db')
    const movies = database.collection('test_collection')

    const query = {name: 'test'}
    const movie = await movies.find().toArray()

    console.log(movie)

    res.end('hello')

    client.close()
})

app.listen(3000)
