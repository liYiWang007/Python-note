'''
项目需求：
1.定位到 2022必看热片
2.从 2022必看热片 中提取子页面链接
3.请求子页面的链接地址，拿到我们想要的下载地址...
'''
import requests
import re

domain="http://www.dytt89.com/"
resp=requests.get(domain,verify=False)#verify=False 去掉安全验证
resp.encoding='gb2312' #该网站用的时国标码（gb）
# print(resp.text)


obj1=re.compile(r'2022必看热片.*?<ul>(?P<ul>.*?)</ul>',re.S)
obj2=re.compile(r"<a href='(?P<link>.*?)'",re.S)

obj3=re.compile(r'◎片　　名(?P<movie>.*?)<br />.*?<td '
r'style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<movie_href>.*?)">',re.S)


# obj3=re.compile(r'【下载',re.S)

result1=obj1.finditer(resp.text)
child_link_list=[]

# 1.定位到 2022必看热片
for it in result1:
    ul=it.group('ul')
    # print(ul)

    # 2.从 2022必看热片 中提取子页面链接
    result2=obj2.finditer(ul)
    for itt in result2:
        child_link=domain+itt.group('link').strip("/")
        child_link_list.append(child_link)   
        # print(child_link_list)
# 3.请求子页面的链接地址，拿到我们想要的下载地址...
for link in child_link_list:
    child_resp=requests.get(link, verify=False) #verify=False 去掉安全验证
    child_resp.encoding='gb2312'
    result3=obj3.search(child_resp.text)
    
    print(result3.group("movie"))
    print(result3.group("movie_href"))
    
