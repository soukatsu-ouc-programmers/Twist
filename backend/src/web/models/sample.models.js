const mongoose = require('mongoose')
const Schema = mongoose.Schema

const tweetSchema = new Schema({
    id: Number,
    date: Date,
    hashtag: [String]
})

const testSchema = new Schema({
    name: String,
    age: Number,
    tag: [String]
})

testSchema.virtual('str_id').get(() => {
    return String(this._id)
})

module.exports = mongoose.model('Test', testSchema)
