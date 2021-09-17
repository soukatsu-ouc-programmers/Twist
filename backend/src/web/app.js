const express = require('express')
const app = express()

const mongoose = require('mongoose')
mongoose.Promise = global.Promise

const testSchema = require('./models/sample.models')

mongoose.connect(`mongodb://${process.env.MONGO_DB_USERNAME}:${process.env.MONGO_DB_PASSWORD}@${process.env.MONGO_DB_HOST}:27017/${process.env.MONGO_DB_DATABASE}?authSource=admin`)
const db = mongoose.connection
db.on('error', console.error.bind(console, 'connection error:'))

app.get('/get-tweet/:hashTag', async (req, res) => {

    res.header('Access-Control-Allow-Origin', '*')
    res.header('Access-Control-Allow-Methods', 'GET')  

    const testData = await testSchema.find({})

    console.log(req.params)

    res.json(testData)
})

app.listen(3000)
