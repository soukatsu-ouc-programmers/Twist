const mongoose = require('mongoose')
const Schema = mongoose.Schema

const tweetSchema = new Schema({
    _id: String,
    date: Date,
    hashtag: [String]
})

module.exports = mongoose.model('Tweet', tweetSchema)
