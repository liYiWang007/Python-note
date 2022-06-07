import requests
from lxml import etree

url='https://beijing.zbj.com/search/f/?kw=saas'
resp=requests.get(url)
# print(resp) #测试网络是否通畅 <Response [200]>
# print(resp.text) 

html=etree.HTML(resp.text)
# 原本的xpath: /html/body/div[6]/div/div/div[2]/div[5]/div[1]/div[1]
divs=html.xpath('/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div')
# divs=html.xpath('/html/body//div[@class="item-wrap"]')
for card in divs:
    #'saas'.join() 把搜索的关键字塞回标题内
    card_title='saas'.join(card.xpath('./div/div/a[2]/div[2]/div[2]/p/text()')) 
    # card_title=card.xpath('./div[@class="grid-box"]//p[@class="title"]/text()')
    # 粗略简化
    card_price=card.xpath('./div[@class="witkey-item grid-box"]//span[@class="price"]/text()')[0].strip('¥')
    # card_price=card.xpath('./div/div/a[2]/div[2]/div[1]/span[1]/text()')[0].strip('¥')
    print(card_title)
    print(card_price)

