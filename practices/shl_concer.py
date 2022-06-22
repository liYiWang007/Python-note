# 综合练习 豆瓣影评抓取

from weakref import proxy
import requests
import re
import bs4
from bs4 import BeautifulSoup
import csv
import os
import time
import pandas as pd
from urllib import request
# csv 文件
# f=open('db-mhl.csv',mode='w',encoding='utf-8')
# csvWriter=csv.writer(f)
# 头
header={
    'Content-Type':'text/html;chast=utf-8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'
}
cookie={
    'Cookie':'抓你自己的'
}
# # 代理
# proxies={
#     'http':'http://211.139.26.16:80'
# }

i=0
while True:
    url=f'https://movie.douban.com/subject/35430794/comments?start={i*20}&limit=20&status=P&sort=time'
    # print(url)
    try:
        # 请求
        html=requests.get(url,headers=header,cookies=cookie)
        # print(html)
        # BeautifulSoup解析
        soup=BeautifulSoup(html.content,'lxml')
        # print(soup)
        # 时间
        comment_times=soup.find_all('span',attrs={'class':'comment-time'})
        if len(comment_times)==0:
            break
        # if i==1:
        #     break
        # 用户id
        comment_users=soup.find_all('span',attrs={'class':'comment-info'})
        # 评分
        comment_stars=soup.find_all('span',attrs={'class':re.compile(r'allstar(\s\w+)?')})
        #评论
        comment_list=soup.find_all('span',attrs={'class':'short'})
        # print(comment_times[0].get('title'))
        # print(comment_times[0].get('title'),comment_users[0].a.string)
        # print(comment_users[0].a.string)

        for jj in range(len(comment_times)):
            data1=[(comment_times[jj].get('title'),comment_users[jj].a.string,comment_list[jj].string,comment_stars[jj].get('class')[0],comment_stars[jj].get('title'))]
            data2=pd.DataFrame(data1)
            data2.to_csv('shl.csv',header=False,index=False,mode='a+')
    except:
        print('something is wrong')
    print('page'+str(i+1)+' has done')
    i=i+1
    time.sleep(2)