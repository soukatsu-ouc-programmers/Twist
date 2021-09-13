<template>
  <div>
    <h1 class="page-title">
      {{ title }}
    </h1>
    <table>
      <thead>
        <tr>
          <td />
          <td v-for="room in rooms" :key="room">
            <ColumnTitle :name="room" />
          </td>
        </tr>
      </thead>
      <tbody>
        <tr v-for="period in periods" :key="period.since">
          <td>
            <Time :since="period.since" :until="period.until" />
          </td>
          <td v-for="room in rooms" :key="room" class="session-cell">
            <Session :info="sessionFilter(room, period.since)" />
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import setting from '../assets/settings/timetable.json'

export default {
  data () {
    return {
      title: '',
      sessions: [],
      rooms: [],
      periods: []
    }
  },
  mounted () {
    this.init()
  },
  methods: {
    init () {
      this.title = setting.day
      this.sessions = setting.sessions
      this.rooms = setting.rooms
      this.periods = setting.periods
    },
    sessionFilter (room, since) {
      return this.sessions.filter(session => (session.room === room && session.since === since))[0]
    }
  }
}
</script>

<style lang="scss" scoped>
  .page-title{
    margin-top: 2rem;
    margin-bottom: 2rem;
    margin-left: 2rem;
  }
  table{
    margin: 0 0 275px 0;
  }
  td{
    padding: 10px 20px;
    white-space: pre-wrap;
  }
</style>
