#安装 requests
#pip install requests

#url lib 网址 库
# request 请求库
#urlopen 打开网址
import requests

keyword=input("输入搜索关键字：")

url=f"https://www.sogou.com/web?query={keyword}"

userAgent={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
}

#获取网站data的一定是get
resp=requests.get(url,headers=userAgent)

print(resp.text) #获取页面源代码
resp.close()


