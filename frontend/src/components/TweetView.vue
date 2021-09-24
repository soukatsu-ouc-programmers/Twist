<template>
  <div id="tweet-list">
    <Tweet v-for="tweet in tweets" :id="tweet.str_id" :key="tweet.str_id">
      <b-spinner variant="primary" />
    </Tweet>
  </div>
</template>

<script>
import { Tweet } from 'vue-tweet-embed'
export default {
  components: {
    Tweet
  },
  props: {
    period: {
      type: Object,
      default: () => ({ since: '', until: '' })
    },
    hashtags: {
      type: Array[String],
      default: () => ['']
    }
  },
  data () {
    return {
      tweets: []
    }
  },
  created () {
    this.fetchTweet()
  },
  methods: {
    async fetchTweet () {
      const res = await this.$axios.get('http://localhost:3001/tweet/', { params: { hashtags: this.$props.hashtags, since: this.period.since, until: this.period.until } })
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

<style>
.twitter-tweet{
  margin-right: auto;
  margin-left: auto;
}
</style>
