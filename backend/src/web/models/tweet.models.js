const mongoose = require('mongoose')
const Schema = mongoose.Schema

const tweetSchema = new Schema({
    id: Number,
    date: Date,
    hashtag: [String]
})

tweetSchema.virtual('str_id').get(() => {
    return String(this._id)
})

module.exports = mongoose.model('Tweet', tweetSchema)
