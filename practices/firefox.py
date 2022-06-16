# xpath练习 火狐浏览器主页新闻钻取 
import requests
from lxml import etree

import csv

f=open('火狐.csv','w',encoding='utf-8')
csvWriter=csv.writer(f)

def open_firefox(url):
    head={
        'Cookie':'Hm_lvt_dd4738b5fb302cb062ef19107df5d2e4=1654740960,1654747521,1654827266,1655083568; Hm_lpvt_dd4738b5fb302cb062ef19107df5d2e4=1655083568',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'
    }
    resp=requests.get(url,headers=head)
    resp.encoding='utf-8'
    # print(resp.text)
    html=etree.HTML(resp.text)
    ul=html.xpath('/html/body//div[@class="px-5 xinwen"]//div[@class="py-3 pl-6 pr-2 space-y-5"]/ul[@class="flex flex-col"]')[0]
    li=ul.xpath('./li/a/text()')
    # print(len(ul))
    # print(li)
    side=html.xpath('/html/body//div[@class="side"]//ul[@class="py-3 list-none"]')[0]
    side_li=side.xpath('./li/a/text()')
    for i in 
    print([li,side_li])




if __name__=='__main__':
    open_firefox('https://home.firefoxchina.cn/')