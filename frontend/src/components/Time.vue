<template>
  <div>
    <p>
      {{ since }}<br>
      {{ until }}
    </p>
  </div>
</template>

<script>
export default {
  props: {
    since: {
      type: String,
      default: '00:00'
    },
    until: {
      type: String,
      default: '00:00'
    }
  }
}
</script>

<style lang="scss" scoped>
div{
  font-size: 1.2rem;
  vertical-align: middle;
}
</style>
