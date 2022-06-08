# requests 进阶：proxy代理
import requests

# 代理地址=http://+地址+:+端口
proxies = {
    'http': 'http://39.130.150.44:80'
}

resp = requests.get('https://www.baidu.com',proxies=proxies)
resp.encoding = 'utf-8'

print(resp.text)
