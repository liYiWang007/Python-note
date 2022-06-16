# 异步协程练习：小说抓取（内容在xhr文件内）
# url 书本地址
# https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306340004"}

# 章节内容
# 第一章# https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306340004","cid":"4306340004|1568936898","need_bookinfo":1}

import requests
import asyncio
import aiohttp
import aiofiles
import json

# 同步操作：访问 getCatalog,拿到所有章节的cid和名称
# 异步操作：访问 getChapterContent 下载所有的文章内容

async def aioDownload(cid,b_id,title):
    data={
        'book_id':b_id,
        'cid':f'{b_id}|{cid}',
        'need_bookinfo':0
    }
    data=json.dumps(data)
    url=f'https://dushu.baidu.com/api/pc/getChapterContent?data={data}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic=await resp.json()
            #利用双斜杠把小说放进novels文件夹内
            async with aiofiles.open('novels\\'+title,mode='w',encoding='utf-8') as f:
                await f.write(dic['data']['novel']['content'])
            

async def getCatalog(url):
    resp=requests.get(url)
    resp.encoding='utf-8'
    dic=resp.json()
    tasks=[]
    for item in dic['data']['novel']['items']:
        title=item['title']
        cid=item['cid']
        print(title,cid)
        # 准备异步下载
        tasks.append(asyncio.create_task(aioDownload(cid,b_id,title)))
    await asyncio.wait(tasks)

if __name__=='__main__':
    b_id='4306340004'
    url='https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"'+b_id+'"}'
    asyncio.run(getCatalog(url))