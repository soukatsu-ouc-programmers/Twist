<template>
  <div v-if="info.sessionTitle != '未登録'" class="session-block" :style="{cursor: 'pointer'}" @click="$emit('move')">
    <div class="session-text">
      <h4 v-text="info.sessionTitle" />
      <p class="speaker" v-text="info.sessionSpeaker" />
    </div>
  </div>
  <div v-else class="session-block">
    <div class="session-text">
      <h4 v-text="'未登録'" />
    </div>
  </div>
</template>

<script>
export default {
  props: {
    info: {
      type: Object,
      default: () => ({ sessionTitle: '未登録', sessionSpeaker: '未登録' })
    }
  }
}
</script>

<style lang="scss" scoped>
  .session-block{
    display: table-cell;
    min-width: 298px;
    margin: 10px auto;
    padding: 40px 5px 0 5px;
    text-align: center;
    height: 200px;
    border-radius: 36px;
    box-shadow: 9px 9px 13px $shadow-color,
    -9px -9px 13px $highlight-color;
    .session-text{
      pointer-events: none;
      white-space: pre-wrap;
      font-size: 10px;
      h4{
        font-size: 15px;
      }
      .speaker{
        display: inline-block;
        margin-top: 30px;
      }
    }
  }
</style>
