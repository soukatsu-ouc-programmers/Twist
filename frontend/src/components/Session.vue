<template>
  <div class="session-block" @click="$router.push('/tweet')">
    <div class="session-text">
      <h4>
        <p to="/tweet">
          セッションタイトル
        </p>
      </h4>
      <p to="/tweet" class="speaker">
        講演者
      </p>
    </div>
  </div>
</template>

<script>
export default {
}
</script>

<style lang="scss" scoped>
  .session-block{
    display: table-cell;
    width: 298px;
    margin: 10px auto;
    padding: 40px 5px 0 5px;
    cursor: pointer;
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
