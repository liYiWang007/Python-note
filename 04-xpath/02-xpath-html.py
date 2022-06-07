from lxml import etree

tree=etree.parse('./02-xpath.html')
#li[1]只获取第一个li 的内容['百度']
# result=tree.xpath('/html/body/ul/li[1]/a/text()') 

#a[@属性='xxx']只获取href包含 bing 字符串的a
result=tree.xpath('/html/body/ul/li/a[@id="bing"]/text()') 
print(result)