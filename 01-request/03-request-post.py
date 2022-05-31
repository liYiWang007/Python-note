from ast import keyword
import requests

url="https://fanyi.baidu.com/sug" #detail-oriented

keyword=input("输入要要翻译的内容：")
dat={
    "kw":keyword
}

#发送post请求

resp=requests.post(url,data=dat)
print(resp.json()) #将返回的内容直接转化为json