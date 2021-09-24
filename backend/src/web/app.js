const express = require('express')
const bodyParser = require('body-parser');

const app = express()
app.use(bodyParser.urlencoded({
    extended: true
}));
app.use(bodyParser.json());


const mongoose = require('mongoose')
mongoose.Promise = global.Promise

const tweetSchema = require('./models/tweet.models')

mongoose.connect(`mongodb://${process.env.MONGO_DB_USERNAME}:${process.env.MONGO_DB_PASSWORD}@${process.env.MONGO_DB_HOST}:27017/${process.env.MONGO_DB_DATABASE}?authSource=admin`)
const db = mongoose.connection
db.on('error', console.error.bind(console, 'connection error:'))

app.get('/tweet/', async (req, res) => {
    const hashtags = req.query.hashtags
    const since = Date.parse(req.query.since)
    const until = Date.parse(req.query.until)

    res.header('Access-Control-Allow-Origin', '*')
    res.header('Access-Control-Allow-Methods', 'GET')

    const tweetData = await tweetSchema.find({
        hashtag: {
            $in: hashtags
        },
        date: {
            $lte: until,
            $gte: since
        }
    })

    res.json(tweetData)
})

app.listen(3000)
