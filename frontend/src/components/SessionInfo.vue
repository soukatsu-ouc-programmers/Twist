<template>
  <div>
    <h3 id="hash-tag" v-text="hashTag" />
    <h3 id="period" v-text="`${period.since}～${period.until}`" />
  </div>
</template>

<script>
export default {
  props: {
    hashTag: {
      type: String,
      default: () => ''
    },
    period: {
      type: Object,
      default: () => ({ since: '', until: '' })
    }
  }
}
</script>

<style lang="scss" scoped>
div{
  justify-content: center;
  display: flex;
  text-align: center;
  margin-bottom: 78px;
  h3{
    font-size: 2rem;
    margin: 20px;
  }
}
</style>
