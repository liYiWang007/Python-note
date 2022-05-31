import requests
# 导入bs4
from bs4 import BeautifulSoup, BeautifulStoneSoup

url='http://www.dytt89.com/'
resp=requests.get(url)
resp.encoding='gb2312'

# 解析数据
# 1.把页面源代码交给BeautifulSoup处理
# html.parser 告诉处理器这就是html(不加也不影响程序运行)
page=BeautifulSoup(resp.text,"html.parser")
content_div=page.find_all('div',attrs={'class':'co_content222'})[1:] #从第二个开始抓取
for it in content_div:
    uls=it.find('ul')
    # print(uls)

    
    for itt in uls:
        lis=itt.find_all('li')
        print(lis)




# lis=ul.find_all('li')[3]
# print(lis)

# ul=content_div.find('ul')
# for itt in lis:
#     fonts=itt.find_all('font')
#     print(fonts[0].text)