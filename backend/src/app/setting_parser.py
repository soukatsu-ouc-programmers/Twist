# 設定ファイルをクローラーように整形するためのスクリプト
import json

with open('/app/settings.json', mode='r', encoding='utf-8') as f:
    base_info = json.load(f)

# どのハッシュタグでどの範囲をクローリングしたらいいのかをまとめる
collect_info = []

for event_date in base_info['dates']:
    for session in event_date['sessions']:
        info = {
            'schedule': session['period'],
            'hashtags': [base_info['mainHashtag']] + session['hashTags']
        }
        collect_info.append(info)

with open('/app/src/collect_info.json', mode='w', encoding='utf-8') as f:
    json.dump(collect_info, f, ensure_ascii=False, indent=2)
