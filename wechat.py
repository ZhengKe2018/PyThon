 #coding=utf-8 
import requests
import json
response = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wx382d2e49831d65a7&corpsecret=Gc1Obkp-izvRoniN8rhzloZCbGfDjCcniefLp24DZ-o")

access_token = response.json()['access_token']

url = 'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token='+access_token

payload = {
    "userid": "zhangsan",
    "name": "张三",
    "mobile": "15913215421",
    "department": [4659221]
}

r = requests.post(url, data=json.dumps(payload))

print(r.json())
