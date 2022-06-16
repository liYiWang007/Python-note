# 混合练习：小说免费章节抓取（内容在网页上）

import requests
import time
from lxml import etree
import re
# import os.path

# 正则匹配章节跟内容
re_novel=re.compile(r'<div align="center" style="float:left;width:713px;padding-left: 0px; padding-top:14px;font-size:16px;">.*?<h2>(?P<novel_title>.*?)</h2>.*?<div style="clear:both;">'
        r'</div>(?P<novel_txt>.*?)<div id="favoriteshow_3"',re.S)

# 获取免费章节和链接
url='http://www.jjwxc.net/onebook.php?novelid=5660519'
r=requests.get(url)
r.encoding='gb18030'
html=etree.HTML(r.text)
table=html.xpath('//*[@id="oneboolt"]/tbody')[0]
# print(len(table))
txt_name=table.xpath('./tr[1]/td/div/span/h1/span[@itemprop="articleSection"]/text()')[0]
f=open(f'{txt_name}.txt',mode='w',encoding='utf-8')
tr_list=table.xpath('./tr')[3:]
# print(len(tr_list))
for tr in tr_list:
    chapter_hrefs=tr.xpath('./td[2]//a/@href')
    if(len(chapter_hrefs)==0):
        print('收工')
        exit()
    chapters=tr.xpath('./td[2]//a/text()')
    # print(chapter_hrefs)
    for href in chapter_hrefs:
        child_resp=requests.get(href)
        child_resp.encoding='gb18030'
        # child_html=etree.HTML(child_resp.text)
        result=re_novel.search(child_resp.text)
        chapter_name=result.group('novel_title')
        novel_content=result.group('novel_txt').replace('<br>','\n')
        novel=chapter_name+novel_content+'\n'
        f.write(novel)
        print('over',chapter_name)
        time.sleep(1)
f.close()



    