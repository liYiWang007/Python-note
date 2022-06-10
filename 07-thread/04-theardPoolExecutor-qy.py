# 1.提取单个页面数据
# 2.上线程池，多个页面同时抓取
import requests
from lxml import etree
import csv

from concurrent.futures import ThreadPoolExecutor

f=open('data.csv',mode='w',encoding='utf-8')
csvWriter=csv.writer(f)

def download_one_page(url):
    resp=requests.get(url)
    resp.encoding='utf-8'
    html=etree.HTML(resp.text)
    table=html.xpath('/html/body/div[4]/div[1]/div[2]/table')[0]
    tr_list=table.xpath('//tr')[1:]
    # tr_list=table.xpath('//tr[position()>1]') #效果跟[1:]差不多，但只适用于同个父级内
    # print(len(tr_list)) #len() .length:获取数据的数量
    # 拿到每个tr
    for tr in tr_list:
        txt=tr.xpath('./td//text()')
        txt=(item.replace('统片','统').replace('统','统片') for item in txt)
        # print(list(txt))
        csvWriter.writerow(txt)
print('提取完毕')

# 单线程
#if __name__=='__main__':
    # download_one_page('https://www.kmzyw.com.cn/jiage/today_price.html')

# 上多线程
if __name__=='__main__':
    with ThreadPoolExecutor(20) as t: #配置20个线程
        for i in range(1,56): #共56页
            t.submit(download_one_page,f'https://www.kmzyw.com.cn/jiage/today_price.html?pageNum={i}')
    print('success')           