import requests
import re

domain="http://www.dytt89.com/"
resp=requests.get(domain,verify=False)#verify=False 去掉安全验证
resp.encoding='gb2312' #该网站用的时国标码（gb）
print(resp.text)


obj1=re.compile(r'2022新片精品.*?<ul>.*?<li>.*?<a </ul>',re.S)
result1=obj1.finditer(resp.text)
for it in result1:
    print(it.group('ul'))
