'''
1.登录获得cookie;
2.利用cookie请求书架url-> 书架内容
  把1、2的操作连接起来
  利用session进行请求，操作过程保留cookies
'''
import requests

# 会话
session = requests.session()
data = {
    'loginName':'test',#登录信息
    'password':'****'
}

# 1.登录
url='https://passport.17k.com/ck/user/login'
session.post(url,data=data)
# print(resp.text)
# print(resp.cookies) #重点

# 2.获取书架数据
# resp=session.get('https://user.17k.com/ck/author/shelf?page=1&appKey=24***919')
# print(resp.json())


# 不用session获取书架内容
resp=requests.get('https://user.17k.com/ck/author/shelf?page=1&appKey=24***919',headers={
"Cookie": "GUID=****"
})
print(resp.text)