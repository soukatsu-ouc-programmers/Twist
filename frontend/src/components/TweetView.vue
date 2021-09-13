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
