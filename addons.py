# API Docs: https://reqable.com/docs/capture/addons

from reqable import *
import os
import requests
import json
def onRequest(context, request):
  # print("111")
  return request

def onResponse(context, response):
  # print("收到请求")
  # print(response.body.type)
  if response.body.isNone:
    print('Http body is none')
  elif response.body.isText:
    print('Http body is text')
  elif response.body.isBinary:
    print('Http body is binary')
  elif response.body.isMultipart:
    print('Http body is multipart')

  # 打印Body的类型
  # print(response.body.type)
  jsons=json.loads(response.body.payload)
  print('匹配到',jsons['otherUser']["userName"])
  # jsons['examVO']["questionCnt"]=1
  # jsons['examVO']["questions"]=[{
  #   "id": 0,
  #   "examId": 608977381113270368,
  #   "content": "12\\circle3",
  #   "answer": ">",
  #   "userAnswer": None,
  #   "answers": [">"],
  #   "status": 0,
  #   "script": None,
  #   "wrongScript": None,
  #   "ruleType": "COMPARE",
  # }]
  for i in range(jsons['examVO']["questionCnt"]):
    jsons['examVO']["questions"][i]["content"]="12\\circle3"
    jsons['examVO']["questions"][i]["answer"]=">"
    jsons['examVO']["questions"][i]["answers"]=[">"]
  response.body.text(json.dumps(jsons))

  # 打印Body的数据
  # print(response.body.payload)
  # with open(r'E:\HB_WuChang\code\小猿口算\data.json', 'w', encoding='utf-8') as f:
  #   f.write(response.body.payload)
  requests.post('http://127.0.0.1:24101/',json=json.loads(response.body.payload))
  return response