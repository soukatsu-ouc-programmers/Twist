<template>
  <div>
    <h3 id="hash-tag" v-text="'#ルームA'" />
    <h3 id="period" v-text="'10:00～11:00'" />
  </div>
</template>

<script>
export default {
  props: {

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
