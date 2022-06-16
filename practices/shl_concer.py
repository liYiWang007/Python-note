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
    'Cookie':'bid=4aAl0pQql7Y; ll="118281"; __utmc=30149280; __utmz=30149280.1655091572.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=223695111; __utmz=223695111.1655091577.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; __gads=ID=9a66b95befe643c9-22d03d285bd4008b:T=1655091584:RT=1655091584:S=ALNI_MZuhHBsi3tHZBw2RhIPEO7aQ52eaw; __gpi=UID=0000069999b91614:T=1655091584:RT=1655091584:S=ALNI_MZyMfaV3SBUAVGYfq4tNEgCCCtGRA; _vwo_uuid_v2=DF76ED4C8ECD43BB18E0ED8C3EF017DA5|7ee991e1cfa2b7f24b2896676ef80946; _pk_ref.100001.4cf6=["","",1655106027,"https://www.douban.com/search?q=%E6%A2%A6%E5%8D%8E%E5%BD%95"]; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.963912721.1654848340.1655101933.1655106028.4; __utmb=30149280.0.10.1655106028; __utma=223695111.202106543.1654848340.1655101933.1655106028.4; __utmb=223695111.0.10.1655106028; _pk_id.100001.4cf6=e3413ceb6bf88a32.1654848340.4.1655108233.1655101933.; dbcl2="60510864:kJqgeiJV1uQ"'
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