<template>
  <div>
    <h3 v-text="name" />
  </div>
</template>

<script>
export default {
  props: {
    name: {
      type: String,
      default: ''
    }
  }
}
</script>

<style lang="scss" scoped>
  h3{
    display: table-cell;
    width: 298px;
    height: 68px;
    margin: 20px auto;
    text-align: center;
    vertical-align: middle;
    border-radius: 61px;
    box-shadow: inset 6px 6px 7px $shadow-color,
    inset -6px -6px 7px $highlight-color;
  }
</style>
