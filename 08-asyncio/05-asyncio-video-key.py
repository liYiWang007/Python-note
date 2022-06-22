import requests
import re
import asyncio
import aiohttp
import aiofiles

from Crypto.Cipher import AES

# 文件名字
second_m3u8_file='越狱_第二层_m3u8.txt'

#获取key.key链接
def get_key(file_name):
    with open(file_name,mode='r',encoding='utf-8') as f:
        obj2=re.compile(r',URI="(?P<key_key>.*?)"',re.S)
        result=obj2.finditer(f.read())
        for i in result:
            kkey=i.group('key_key').rstrip()
            # print(kkey)
        # 获取key.key的内容
        resp=requests.get(kkey)
        # print(resp.text)
        return resp.text

def dec_ts(name):
    pass

async def aio_dec(key):
    # 解密
    tasks=[]
    async with open('second_m3u8_file',mode='r',encoding='utf-8') as f:
        async for line in f:
            if line.startswith('#'):
                continue
            line=line.strip()
            # 创建异步任务
            task=asyncio.create_task(dec_ts(line.key))
            tasks.append(task)
        await asyncio.wait(tasks)



# 下载m3u8里的内容
def download_m3u8_file(url,name):
    header={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
    resp=requests.get(url,headers=header)
    with open(name,mode='wb') as f:
        f.write(resp.content)

# 获取第一个m3u8地址
def get_first_m3u8(url):
    obj=re.compile(r'<script>var vid=".*?var now="(?P<m3u8_href>.*?)"',re.S)
    # 1.获取源代码：
    resp=requests.get(url)
    m3u8_href=obj.search(resp.text).group('m3u8_href')
    # print(m3u8_href)
    return m3u8_href

# 下载第二层m3u8里的ts文件
async def download_ts(url,name,session):
    async with session.get(url) as resp:
        async with aiofiles.open(f'videoYy\{name}',mode='wb') as f:
            await f.write(await resp.content.read()) #把卸载的内容放到文件中
    print(f'{name} 下载完成')
    
# 第二个m3u8
async def aio_download():
    tasks=[]
    async with aiohttp.ClientSession() as session: #提前准备session
        async with aiofiles.open(second_m3u8_file,mode='r',encoding='utf-8') as f:
            async for line in f:
                if line.startswith('#'):
                    continue
                else:
                    line=line.rstrip() #去掉尾部空白符
                    line_name=line.rsplit('/',1)[1]
                    # print(line_name)
                    # 创建任务
                    task=asyncio.create_task(download_ts(line,line_name,session)) #创建协程人物
                    tasks.append(task)
            await asyncio.wait(tasks)



def main(url):
    # get_first_m3u8(url) #第一层m3u8文件
    first_m3u8=get_first_m3u8(url)  #第一层m3u8地址
    # print(first_m3u8) # https://v4.cdtlas.com/20220611/BFpmTtxf/index.m3u8
    file_name='越狱第一季第一集_m3u8.txt'
    # download_m3u8_file(first_m3u8,file_name)
    link_start=first_m3u8.split('m/')[0]+'m' #切割获取链接头
    # print(link_start)

    # 获取第二层的u3m8文件
    with open(file_name,mode='r',encoding='utf-8') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                line=line.rstrip() # .rstrip()去掉结尾 空白符or换行符 \n
                second_m3u8_href=f'{link_start}{line}' #拼接链接头+获取的m3u8地址
                # download_m3u8_file(second_m3u8_href,second_m3u8_file)
                print('第二层m3u8 搞定')
  
    # 异步协程 下载ts视频文件
    # 下载完毕请注释掉
    # asyncio.run(aio_download())

    # 抓取密钥key.key
    kkey=get_key(second_m3u8_file)
    # print(kkey)




if __name__=='__main__':
    url='https://www.kuyun.tv/play/14453-0-0.html'
    main(url)