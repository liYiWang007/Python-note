'''
需求：
1.抓取主页，从中提取子页面的链接href
2.顺着子页面，抓取图片下载地址
3.下载图片
'''
from base64 import encode
import requests
import time
from bs4 import BeautifulSoup 
url="https://www.tusij.com/img3rd/index?c3=601"
# url="https://www.umei.cc/bizhitupian/weimeibizhi/"
resp=requests.get(url)
resp.encoding='utf-8'
# print(resp)


main_page=BeautifulSoup(resp.text,'html.parser')
aList=main_page.find("div",class_='barrel').find_all('a',class_='barrel-title')
# print(aList)

for a in aList:
    href=a.get('href').strip('/')
    # 抓取子页面源代码
    child_page_resp=requests.get('https://www.tusij.com/'+href)
    child_page_resp.encoding='utf-8'
    child_page_text=child_page_resp.text
    # print(child_page_text)

    # 抓取图片下载路径
    child_page=BeautifulSoup(child_page_text,'html.parser')
    img=child_page.find('div',class_='img-box').find('img')
    src=img.get('src')
    # 下载图片
    img_resp=requests.get(src)
#     # img_resp.content #拿到字节
    img_name=img.get('alt') #获取url中的最后一个‘/’以后的内容
    # img_name=src.split('/')[-1] #获取url中的最后一个‘/’以后的内容
    # print(img_name)

    # with open('images\\'+img_name,mode='wb+')as f: # wb+ 防止爬的数据成为乱码
        # f.write(img_resp.content)

    # print('over',img_name)
    # time.sleep(1)

    print(img_resp.content)
# print('all_over')

