<template>
  <div :style="{color: colors[roomIndex%colors.length]}">
    <SessionTitle :title="session.sessionTitle" :speaker="session.sessionSpeaker" />
    <SessionInfo :hash-tag="session.hashTag" :period="session.period" />
    <TweetView />
  </div>
</template>

<script>
import setting from '../../assets/settings/Day1.json'

export default {
  asyncData ({ params }) {
    const room = params.room
    const period = setting.periods[params.period]

    const session = setting.sessions.filter(session => (session.room === room && session.period.since === period.since))[0]
    return { session, roomIndex: setting.rooms.indexOf(room) }
  },
  data () {
    return {
      colors: ['#6fa0e9', '#de6769', '#95c380', '#c17ca0', '#c58f69']
    }
  }
}
</script>
