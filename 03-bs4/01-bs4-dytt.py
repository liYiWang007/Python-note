import requests
# 导入bs4
from bs4 import BeautifulSoup
import csv

url='http://www.dytt89.com/'
resp=requests.get(url)
resp.encoding='gb2312'

f=open('电影名字.csv',mode='w',encoding='utf-8')
csv_file=csv.writer(f)
# 解析数据
# 1.把页面源代码交给BeautifulSoup处理
# html.parser 告诉处理器这就是html(不加也不影响程序运行)
page=BeautifulSoup(resp.text,"html.parser")
content_div=page.find_all('div',attrs={'class':'co_content222'})[1:] #从第二个开始抓取
# ul=content_div.find('ul')
# li=ul.find_all('li')
for it in content_div:
    uls=it.find('ul')
    lis=uls.find_all('li')[2]
    name=lis.find('a').text
    date=lis.find('span').text
    # print(date)
    csv_file.writerow([name,date])
f.close()
print("over")
