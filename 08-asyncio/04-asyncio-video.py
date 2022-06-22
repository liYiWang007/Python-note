# <video src='视频链接.mp4'></video>

# 一般视频网站都会压缩视频，切片，用户播放时一段一段预下载，

# 抓取思路:
# 视频播放顺序；视频存放路径；M3U8 txt json =>文本

# 1.找到M3U8
# 2.通过M3U8下载到ts文件
# 3.把ts文件合并为MP4

import requests
import re
# obj =re.compile(r"url: '(?P<url>.*?)',",re.S) #提取video的链接
# url='https://www.91kanju2.com/vod-play/15968-5-1.html'
# head={
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
# }
# resp=requests.get(url,headers=head)
# # 获取m3u8地址
# m3u8_url=obj.search(resp.text).group("url")
# # print(m3u8_url)
# resp.close()


# # 下载m3u8
# resp2=requests.get(m3u8_url,headers=head)
# # resp2.encoding='utf-8'
# # print(resp2.content)
# with open('知否.m3u8',mode='wb+') as f:
#     f.write(resp2.content)

# resp2.close()
# print('下载完了')

# 获取完文件源后上面的内容都注释掉
# 解析m3u8文件
n=1
with open('知否.m3u8',mode='r',encoding='utf-8') as f:
    for line in f:
        line=line.strip()
        if line.startswith('#'): #不要#号开头的那行
            continue
        # print(line)

        # 单线程下载文件法
        resp3=requests.get(line)
        f=open(f"videoTs\{n}.ts",mode='wb+')
        f.write(resp3.content)
        n +=1


