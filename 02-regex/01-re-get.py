import re

# # 查找所有数字
# lst=re.findall(r"\d+", "他的电话号：10000，隔壁电话是10086")
# print(lst)

# # finditer:匹配字符串中的所有内容(迭代器)，需用用.group(0转化
# it=re.finditer(r"\d+", "他的电话号：10000，隔壁电话是10086")
# for i in it:
#     print(i.group())

# # search 找到一个结果就返回
# s=re.search(r"\d+", "他的电话号：10000，隔壁电话是10086")
# print(s.group())

# # match 从头开始匹配，相当于 r^"\d+"
# m=re.search(r"\d+", "他的电话号：10000，隔壁电话是10086")
# print(m.group())

# # 预加载正则，用于提高效率
# obj=re.compile(r"\d+")

# ret=obj.finditer("他的电话号：10000，隔壁电话是10086")
# for i in ret:
#     print(i.group())

# obj=re.compile(r'\d+')
# ret=obj.finditer("他的电话号：10，隔壁电话是10086,小陈家的是3000")

# for i in ret:
#     print(i.group())

s='''<div class="jay"><span id="1">周杰伦</span></div>
<div class="jolin"><span id="2">蔡依林</span></div>
<div class="jj"><span id="3">林俊杰</span></div>
<div class="simon"><span id="4">龚俊</span></div>
<div class="tony"><span id="5">李华</span></div>
'''

'''
我是
多行
注释
'''

# re.S =让 .也能匹配换行符
# obj=re.compile(r'<div class=".*?"><span id="(?P<id>\d+)">(?P<test>.*?)</span></div>',re.S)

# result=obj.finditer(s)
# for i in result:
#     # print(i.group('id'))
#     print(i.group('test'))

a='''
iamtesting
theentercode
howtowork
'''

b=re.findall('a(.*?)code',a)
c=re.findall('a(.*?)code',a,re.S)
print(b) # →[]
print(c) # →['mtesting\ntheenter']


