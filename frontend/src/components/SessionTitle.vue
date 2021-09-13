<template>
  <div>
    <div class="session-title">
      <div class="session-text">
        <h4 v-text="'title'" />
        <p v-text="'講演者'" />
      </div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style lang="scss" scoped>
  .session-title{
    width: 30vw;
    margin: 50px auto;
    padding: 30px;
    text-align: center;
    border-radius: 36px;
    background: $base-color;
    box-shadow: inset 6px 6px 7px $shadow-color,
                inset -6px -6px 7px $highlight-color;
    .session-text{
      pointer-events: none;
      white-space: pre-wrap;
      font-size: 10px;
      h4{
        font-size: 2rem;
      }
      .speaker{
        display: inline-block;
        margin-top: 30px;
      }
    }
  }
</style>
