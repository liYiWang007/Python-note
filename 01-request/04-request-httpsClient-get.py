import requests


# 问号？后面的都是参数：'type=24&interval_id=100:90&action=&start=0&limit=20'
url="https://movie.douban.com/j/chart/top_list"

# 重新封装参数param
param={
 'type':24,
 'interval_id':'100:90',
 'action':'',
 'start':0,
 'limit':100
}
head={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
}
resp=requests.get(url=url,params=param,headers=head)

# print(resp.request.url)#检查param参数是否替换成功
# print(resp.request.headers)#无法获取数据时，检查user Agent
print(resp.json())
resp.close()