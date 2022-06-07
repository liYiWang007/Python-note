from lxml import etree
parser = etree.HTMLParser(encoding='utf-8')
tree=etree.parse('./mhl0-499.html',parser=parser)

result=tree.xpath('/html/body//div[@id="comments"]/div[@class="comment-item "]//span[@class="allstar10 rating"]/text()')
print(result)