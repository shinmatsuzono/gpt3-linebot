import json
import requests
import os


def lambda_handler(event, context):
    message_event = json.loads(event['body'])['events'][0]
    message = message_event['message']['text']
    body = {
        'replyToken': message_event['replyToken'],
        'messages': [{
            "type": "text",
            "text": '',
        }]
    }
    body['messages'][0]['text'] = answer_phrase(message)
    url = 'https://api.line.me/v2/bot/message/reply'
    token = get_store_parameter('line_token')
    
    post_api(url, body, token)

    return return_code(200)
    
    
def get_store_parameter(key):
    end_point = 'http://localhost:2773'
    path = '/systemsmanager/parameters/get/'
    query = '?withDecryption=true&name=' + key
    url = end_point + path + query
    headers = headers = {
        'X-Aws-Parameters-Secrets-Token': os.environ['AWS_SESSION_TOKEN']
    }

    res = requests.get(url, headers=headers)
    res_json = res.json()

    return res_json['Parameter']['Value']

    
def answer_phrase(message):
    if 'ありがと' in message:
        return 'どういたしまして'
    else:
        return answer_ai(message)


def answer_ai(question):
    url = 'https://api.openai.com/v1/completions'
    token = get_store_parameter('gpt_token')
    body = {
      "model": "text-davinci-003",
      "prompt": question,
      "max_tokens": 4000
    }

    res = post_api(url, body, token)
    answer = res['choices'][0]['text']

    return answer.replace("\n\n", "", 1)


def post_api(url, body, token):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }
    res = requests.post(
        url,
        json.dumps(body),
        headers=headers
    )
    
    return res.json()
    
    
def return_code(status):
    return {
        'statusCode': status,
        'body': json.dumps('OK')
    }
