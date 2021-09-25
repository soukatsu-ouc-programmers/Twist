<template>
  <div>
    <div v-for="date, dateIndex in dates" :id="date.pageTitle" :key="dateIndex" class="day-block">
      <h1 class="page-title">
        {{ date.pageTitle }}
      </h1>
      <div class="table-wrap">
        <table>
          <thead>
            <tr>
              <td />
              <td v-for="room, roomIndex in date.rooms" :key="roomIndex" :style="{color: colors[roomIndex%colors.length]}">
                <ColumnTitle :name="room" />
              </td>
            </tr>
          </thead>
          <tbody>
            <tr v-for="period, periodIndex in date.periods" :key="period.since">
              <td>
                <Time :since="period.since" :until="period.until" class="time" />
              </td>
              <td v-for="room, roomIndex in date.rooms" :key="roomIndex" class="session-cell" :style="{color: colors[roomIndex%colors.length]}">
                <Session :info="sessionFilter(dateIndex, room, period.since)" @move="moveTweetPage(dateIndex, room, periodIndex)" />
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import setting from '../assets/settings/setting.json'

export default {
  data () {
    return {
      dates: [],
      colors: ['#6fa0e9', '#de6769', '#95c380', '#c17ca0', '#c58f69']

    }
  },
  mounted () {
    this.init()
  },
  methods: {
    init () {
      this.dates = setting.dates
    },
    sessionFilter (dateIndex, room, since) {
      const sessions = this.dates[dateIndex].sessions
      return sessions.filter(session => (session.room === room && session.period.since === since))[0]
    },
    moveTweetPage (dateIndex, room, periodIndex) {
      this.$router.push(`/${this.dates[dateIndex].date}/${room}/${periodIndex}`)
    }
  }
}
</script>

<style lang="scss" scoped>
  .day-block{
    margin-top: -50px;
    padding-top: 50px;
  }
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
