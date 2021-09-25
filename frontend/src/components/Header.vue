<template>
  <b-navbar toggleable="lg" type="dark" class="header" :sticky="true">
    <b-navbar-brand to="/" v-text="title" />
    <b-navbar-nav class="ml-auto">
      <b-nav-item-dropdown text="日程" right>
        <b-dropdown-item v-for="page in pages" :key="page" v-scroll-to="`#${page}`">
          {{ page }}
        </b-dropdown-item>
      </b-nav-item-dropdown>
      <b-nav-item href="#">
        使い方
      </b-nav-item>
      <b-nav-item :href="url" target="_blank">
        イベント公式サイト
      </b-nav-item>
      <b-nav-item href="https://github.com/soukatsu-ouc-programmers/Twist" target="_blank">
        GitHub
      </b-nav-item>
    </b-navbar-nav>
  </b-navbar>
</template>

<script>
import setting from '../assets/settings/setting.json'

export default {
  data () {
    return {
      title: '',
      url: '',
      pages: []
    }
  },
  mounted () {
    this.init()
  },
  methods: {
    init () {
      this.title = setting.eventName
      this.url = setting.homePage
      this.pages = setting.dates.map((v, i) => v.pageTitle)
    }
  }
}
</script>

<style lang="scss">
  .header {
    background-color: $main-color;
  }
</style>
