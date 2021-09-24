<template>
  <div>
    <h1 class="page-title">
      {{ title }}
    </h1>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <td />
            <td v-for="room, roomIndex in rooms" :key="roomIndex" :style="{color: colors[roomIndex%colors.length]}">
              <ColumnTitle :name="room" />
            </td>
          </tr>
        </thead>
        <tbody>
          <tr v-for="period, periodIndex in periods" :key="period.since">
            <td>
              <Time :since="period.since" :until="period.until" class="time" />
            </td>
            <td v-for="room, roomIndex in rooms" :key="roomIndex" class="session-cell" :style="{color: colors[roomIndex%colors.length]}">
              <Session :info="sessionFilter(room, period.since)" @move="moveTweetPage(room, periodIndex)" />
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import setting from '../assets/settings/Day1.json'

export default {
  data () {
    return {
      title: '',
      sessions: [],
      rooms: [],
      periods: [],
      colors: ['#6fa0e9', '#de6769', '#95c380', '#c17ca0', '#c58f69']
    }
  },
  mounted () {
    this.init()
  },
  methods: {
    init () {
      this.title = setting.pageTitle
      this.sessions = setting.sessions
      this.rooms = setting.rooms
      this.periods = setting.periods
    },
    sessionFilter (room, since) {
      return this.sessions.filter(session => (session.room === room && session.period.since === since))[0]
    },
    moveTweetPage (room, periodIndex) {
      this.$router.push(`/${room}/${periodIndex}`)
    }
  }
}
</script>

<style lang="scss" scoped>
  .page-title{
    margin-top: 2rem;
    margin-bottom: 2rem;
    margin-left: 2rem;
    color: $main-color
  }
  .table-wrap{
    overflow-x: auto;
    white-space: nowrap;
    &::-webkit-scrollbar{
      height: 5px;
    }
    &::-webkit-scrollbar-track{
      border-radius: 5px;
      box-shadow: 0 0 4px #aaa inset;
    }
    &::-webkit-scrollbar-thumb {
      border-radius: 5px;
      background: $main-color;
    }
  }
  table{
    margin: 0 0 275px 0;
  }
  td{
    padding: 10px 20px;
    white-space: pre-wrap;
  }
  .time{
    color: $main-color;
  }
</style>
