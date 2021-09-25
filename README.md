# Twist
オンラインイベントやカンファレンスでのハッシュタグ付きのツイートを，時間やルームで分割して見やすく公開できるサイトを簡単に作れるプロダクト

# スタートガイド

## 準備するもの
### ソフトウェア
- [Docker](https://docs.docker.com/get-docker/)
- [docker-compose](https://docs.docker.com/compose/install/)
### APIキー
- [Twitter API: Consumer Key，AccessToken (v1.1)](https://developer.twitter.com/en/docs/getting-started)
### セッション情報ファイル
[こちら](https://soukatsu-ouc-programmers.github.io/Twist/setting-maker/)から作れます。  
例）
![setting-maker](https://user-images.githubusercontent.com/38606036/134780504-2d165c34-3595-451f-820b-495e417988bd.png)  
※ハッシュタグには全て`#`をつけて下さい

## 環境構築
1. 以下の形式で`.env`というファイルを作成し，ローカルリポジトリのルートに置く。
```
MONGO_ROOT_PASSWORD=SECURE_PASSWORD
TWITTER_API_KEY=YOUR_TWITTER_API_KEY
TWITTER_API_SECRET=YOUR_TWITTER_API_SECRET_KEY
TWITTER_ACCESS_TOKEN=YOUR_TWITTER_ACCESS_TOKEN
TWITTER_ACCESS_SECRET=YOUR_TWITTER_ACCESS_SECRET_TOKEN
```
2. セッション情報ファイルを，ローカルリポジトリのルートに置く。
```
例） path/to/Twist/local/repository/settings.json
```
3. `docker-compose up`する。  
VSCode上の例）  
![vscode-composeup](https://user-images.githubusercontent.com/38606036/134780466-0dbf9542-ad26-447f-b94b-c007148f440f.png)


コマンドの例）
```[bash]
$ cd path/to/Twist/local/repository
$ docker-compose up -d --build
```
4. `http://localhost:3000`にアクセス
5. セッション情報ファイルの内容と同じサイトが表示されればOK

## ツイートの収集について
- ツイートの収集は各セッション終了後5分後から行われます。（終了後の感想ツイートも集めるため）  
- セッションの時間より後に起動した場合は，即時収集が行われます。
- APIの制限により，7日より前のツイートの収集はできません。

## 注意事項
- 動作を確認したのはWSL2上のみです。他の環境への対応はもう少しお待ちください。

## 本番環境へのデプロイ
お待ちください。

# Copyright
©2021 soukatsu-ouc-programmers

# License
This project is licensed under the MIT Licens

