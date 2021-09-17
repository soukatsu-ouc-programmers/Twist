<template>
  <div>
    <SessionTitle :title="session.sessionTitle" :speaker="session.sessionSpeaker" />
    <SessionInfo :hash-tag="session.hashTag" :period="session.period" />
    <TweetView />
  </div>
</template>

<script>
import setting from '../../assets/settings/timetable.json'

export default {
  asyncData ({ params }) {
    const room = params.room
    const period = setting.periods[params.period]

    const session = setting.sessions.filter(session => (session.room === room && session.period.since === period.since))[0]
    return { session }
  }
}
</script>
