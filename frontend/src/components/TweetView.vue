<template>
  <div id="tweet-list">
    <Tweet :id="'1435847868061925381'" />
  </div>
</template>

<script>
import { Tweet } from 'vue-tweet-embed'
export default {
  components: {
    Tweet
  },
  created () {
    this.fetchTweet()
  },
  methods: {
    async fetchTweet () {
      const res = await this.$axios.get('http://localhost:3001/get-tweet/test/')
      // プロキシのつなぎ方わかんね～～～～
      // const res = await this.$axios.get('/api/get-tweet/test')
      this.tweets = res.data
      console.log(this.tweets)
    }
  }
}
</script>

<style lang="scss" scoped>
div#tweet-list{
  width: 40vw;
  padding: 30px;
  text-align: center;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 30px;
  vertical-align: middle;
  border-radius: 61px;
  background: $base-color;
  box-shadow: inset 6px 6px 7px $shadow-color,
              inset -6px -6px 7px $highlight-color;
}
</style>
