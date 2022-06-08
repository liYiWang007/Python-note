'''requests进阶：
1.抓取conId
2.获取videoStatus返回的json ->srcURL
3.调整srcURL
4.下载视频
'''

import requests
url = 'https://www.pearvideo.com/video_1757562'
# split() 切片url,获取id数字
conId = url.split('_')[1]
# print(conId)

videoStatus = f'https://www.pearvideo.com/videoStatus.jsp?contId={conId}&mrd=0.004681725344451326'
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
    # 防盗链 防盗链就是溯源，要追溯上一步的请求
    'Referer': url
}
# 出现’该文章已经下线！‘ 代表此网站有反扒手段，需要设置user-Agent
# 加了user-Agent 还是出现’该文章已经下线！‘，代表视频有防盗链Referer
resp = requests.get(videoStatus, headers=head)
# print(resp.text) #校验是否成功获取"videoInfo"数据
# 抓取videoInfo/videos/srcUrl的数据
dic=resp.json()
srcURL=dic['videoInfo']['videos']['srcUrl'] #->"srcUrl":"https://video.pearvideo.com/mp4/adshort/20220406/1654664813136-15856495_adpkg-ad_hd.mp4"
systemTime=dic['systemTime'] #->"systemTime": "1654664813136"
# 把srcURL中的时间改成contId
srcURL=srcURL.replace(systemTime,f'cont-{conId}')
# print(srcURL) 获取正确的视频链接

# 下载视频
with open('a.mp4',mode='wb') as f:
    f.write(requests.get(srcURL).content)
