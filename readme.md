# GPT-3(ChatGPT)をLINE BOTにするLambdaのコード

## 概要

このコードをLambdaでデプロイしてLINEのWebhookと紐付けると、LINEの友達となったGPT-3と会話できます。

## アーキ説明

- LINE：LINEDevelopersよりBOTのProviderとChannel(MessagingAPI)を設定ください
- コード実行：AWS Lambda (Python)
- レイヤー：pythonのモジュールのrequests、AWS ParameterStoreとの連携用レイヤーを設定ください
- API Endpoint：Amazon API Gatewayを設定し、LINEMessagingAPIのWebhookに設定ください
- パラメーター管理：AWS SystemsManager ParameterStoreにLINEとGPT-3のシークレットキーを設定ください。

## アーキのポイント

- AWS Parameters and Secrets Lambda Extension を採用しています。
    - 2022年10月に公開された拡張機能
    - LambdaからAWSで管理するParameterにアクセスするときに、キャッシュをよしなにやってくれる
- あとは普通のLINE BOT with Lambdaと同じです。

## GPT-3(ChatGPT)とは？

OpenAIが開発している自然に会話できるAI。コーディングの壁打ちなどに適しています。
