# 异步操作aiohttp

import asyncio
import aiohttp
from aiohttp import TCPConnector



# 1.发送请求
# 2.获取图片内容
# 3.保存图片
# print(url)

urls=[
    'http://kr.shanghai-jiuxin.com/file/2020/1031/6b72c57a1423c866d2b9dc10d0473f27.jpg',
    'http://kr.shanghai-jiuxin.com/file/2022/0414/ba34fff6a58897cc5362b79e477c06d8.jpg',
    'http://kr.shanghai-jiuxin.com/file/2022/0608/e70378f07e8ca51e86d3ac0c1a2b5224.jpg'
]

async def aioDownload(url):
    # with open('file.csv','w')as f:
    #     f.write()
    #     f.close()
    name=url.rsplit('/',1)[1] #抓取最后一个/斜杠后的内容
    # 加上 with 会自动补上.close()
    # aiohttp.ClientSession() #->相当于requests 
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            # resp.text() #对比requests 需要+括号 json()/text()
            with open(name,mode='wb') as f:
                f.write(await resp.content.read())

    print(name,'success')

async def main():
    tasks=[]
    for url in urls:
        tasks.append(asyncio.create_task(aioDownload(url)))

    await asyncio.wait(tasks)

if __name__=='__main__':
    asyncio.run(main())
    

