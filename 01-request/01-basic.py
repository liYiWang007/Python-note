#爬虫

#url lib 网址 库
# request 请求库
#urlopen 打开网址
from urllib.request import urlopen

url="https://blog.csdn.net/weixin_39840606/article/details/111179862?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-0-111179862-blog-110560998.pc_relevant_paycolumn_v3&spm=1001.2101.3001.4242.1&utm_relevant_index=3"
resp=urlopen(url)
# resp.encoding='gb2312'

# with open("whywb.html","wb") as f:

with open("test.html",mode="w",encoding="utf-8") as f:
    f.write(resp.read().decode("utf-8"))
print('over')
resp.close()