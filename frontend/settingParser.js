// 設定ファイルをフロント用に整形するためのスクリプト
const fs = require('fs')

const buff = fs.readFileSync('/app/settings.json', 'utf8')
const jsonSetting = JSON.parse(buff)

const sessionInfo = jsonSetting.dates.map(date => (
    {
        name: date.pageTitle,
        file: `${date.pageTitle}.json`
    }
))

// イベントの情報をまとめる
const settingObj = {
    eventName: jsonSetting.eventName,
    homePage: jsonSetting.homePage,
    hashTag: jsonSetting.mainHashtag,
    sessionInfo: sessionInfo
}

// ファイルとして保存
fs.writeFileSync('/app/src/assets/settings/setting.json', JSON.stringify(settingObj))
jsonSetting.dates.forEach(date => {
    date.periods.forEach(period => {
        period.since = period.since.match(/([0-9]{2}:[0-9]{2}):00/)[1]
        period.until = period.until.match(/([0-9]{2}:[0-9]{2}):00/)[1]
    })
    date.sessions.forEach(session => {
        session.period.since = session.period.since.match(/([0-9]{2}:[0-9]{2}):00/)[1]
        session.period.until = session.period.until.match(/([0-9]{2}:[0-9]{2}):00/)[1]
    })
    fs.writeFileSync(`/app/src/assets/settings/${date.pageTitle}.json`, JSON.stringify(date))
})