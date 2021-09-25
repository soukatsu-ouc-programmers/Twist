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
    const hashtags = req.query.hashtags || []
    const since = Date.parse(req.query.since) || new Date()
    const until = Date.parse(req.query.until) || new Date()

    res.header('Access-Control-Allow-Origin', '*')
    res.header('Access-Control-Allow-Methods', 'GET')

    // hashtagsが無い時の分岐だけどもう少し賢い方法がありそう…
    const query = (() => {
        if (hashtags.length != 0) {
            return {
                hashtag: {
                    $in: hashtags
                },
                date: {
                    $gte: since,
                    $lte: until
                }
            }
        } else {
            return {
                date: {
                    $gte: since,
                    $lte: until
                }
            }
        }
    })()

    const tweetData = await tweetSchema.find(query).sort({date: 1})

    const resData = tweetData.map(tweet => ({ str_id: tweet._id }))

    res.json(resData)
})

app.listen(3000)
