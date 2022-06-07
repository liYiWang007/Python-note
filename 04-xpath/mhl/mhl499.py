from lxml import etree
parser = etree.HTMLParser(encoding='utf-8')
tree=etree.parse('./mhl0-499.html',parser=parser)

stars_list=tree.xpath('/html/body//div[@id="comments"]/div[@class="comment-item "]')
for star in stars_list:
    result=star.xpath('//span[@class="allstar10 rating"]/text()')
    print(result)

