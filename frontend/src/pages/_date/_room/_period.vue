<template>
  <div :style="{color: colors[roomIndex%colors.length]}">
    <SessionTitle :title="session.sessionTitle" :speaker="session.sessionSpeaker" />
    <SessionInfo :hash-tag="session.hashTag" :period="session.period" />
    <TweetView :hashtags="session.hashTags" :period="fullPeriod" />
  </div>
</template>

<script>
import setting from '../../../assets/settings/setting.json'

export default {
  asyncData ({ params }) {
    const dateIndex = setting.dates.findIndex(({ date }) => date === params.date)
    const room = params.room
    const period = setting.dates[dateIndex].periods[params.period]

    const fullPeriod = {
      since: `${params.date}T${period.since}`,
      until: `${params.date}T${period.until}`
    }

    const session = setting.dates[dateIndex].sessions.filter(session => (session.room === room && session.period.since === period.since))[0]
    return { session, roomIndex: setting.dates[dateIndex].rooms.indexOf(room), fullPeriod }
  },
  data () {
    return {
      colors: ['#6fa0e9', '#de6769', '#95c380', '#c17ca0', '#c58f69']
    }
  }
}
</script>
