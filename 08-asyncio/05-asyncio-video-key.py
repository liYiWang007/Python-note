import requests
import re
import asyncio
import aiohttp
import aiofiles
import os #合并ts文件

from Crypto.Cipher import AES #解码

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

# 读取key.key
async def dec_ts(name,key):
    # 从URI="https://hey07.789zy.cc/20220611/BFpmTtxf/hls/key.key" 中:
    # 获取的key.key 为57d17982aec9bda8 ，共16位数，需要16个0
    #EXT-X-KEY:METHOD=AES-128, 格式为AES-128
    # print(type(key),key)
    aes=AES.new(key=key.encode("utf-8"),mode=AES.MODE_CBC,IV=b'0000000000000000')
    # rb:二进制读取； wb:二进制写入
    try:
        async with aiofiles.open(f'videoYy\{name}',mode='rb') as f1,\
            aiofiles.open(f'videoYy_temp\\temp_{name}',mode='wb') as f2:
            #1.读取源文件内容
            bs=await f1.read() 
            #2.把解密内容写入
            await f2.write(aes.decrypt(bs))
            # print(f'{name} 解密完毕')
            return ''
    except:
        print(name,'解码失败，重来')

# 解密key
async def aio_dec(key):
    # 解密
    tasks=[]
    # print(repr(second_m3u8_file))
    async with aiofiles.open(second_m3u8_file,mode='r',encoding='utf-8') as f:
        async for line in f:
            if line.startswith('#'):
                continue
            line=line.strip()
            line_name=line.rsplit('/',1)[1]
            # 创建异步任务
            task=asyncio.create_task(dec_ts(line_name,key))
            tasks.append(task)
        await asyncio.wait(tasks)


# 获取第一个m3u8地址
def get_first_m3u8(url):
    obj=re.compile(r'<script>var vid=".*?var now="(?P<m3u8_href>.*?)"',re.S)
    # 1.获取源代码：
    resp=requests.get(url)
    m3u8_href=obj.search(resp.text).group('m3u8_href')
    # print(m3u8_href)
    return m3u8_href

# 下载m3u8里的内容
def download_m3u8_file(url,name):
    header={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
    resp=requests.get(url,headers=header)
    with open(name,mode='wb') as f:
        f.write(resp.content)

# 下载第二层m3u8里的ts文件
async def download_ts(url,name,session):
    try:
        async with session.get(url) as resp:
            async with aiofiles.open(f'videoYy\{name}',mode='wb') as f:
                await f.write(await resp.content.read()) #把下载的内容放到文件中
        # print(f'{name} success')
        return ''
    except: #以防下载失败
        print(name,'下载失败，重来')
    
# 第二层m3u8
async def aio_download():
    tasks=[]
    # run_until_complete需要设置限时
    # timeout = aiohttp.ClientTimeout(total=1000)
    # async with aiohttp.ClientSession(timeout=timeout) as session: #提前准备session
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

# 合并ts视频
def merge_ts():
    lst=[]
    with open(second_m3u8_file,mode='r',encoding='utf-8') as f:
        for line in f:
            if line.startswith('#'):
                continue
            line=line.strip()
            line_name=line.rsplit('/',1)[1]
            lst.append(f'videoYy_temp\\temp_{line_name}')
        
        # s='+'.join(lst)
        # mac: cat 1.ts 2.ts 3.ts >xxx.mp4
        #os.system(f'cat{s}>move.mp4')

        # windows: copy /b 1.ts+2.ts+3.ts xxx.mp4
        # print(s)
        os.system(f'copy /B videoYy_temp\\temp_*.ts 越狱第一季第一集.mp4')
        print('成功合成mp4')


def main(url):
    #第一层m3u8文件
    first_m3u8=get_first_m3u8(url)  #第一层m3u8地址
    # print(first_m3u8) -> https://v4.cdtlas.com/20220611/BFpmTtxf/index.m3u8
    file_name='越狱第一季第一集_m3u8.txt'
    # download_m3u8_file(first_m3u8,file_name) #下载完就注释掉
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
                # print('第二层m3u8 搞定')
  
    # 异步协程 下载ts视频文件
    # 下载完毕请注释掉
    # asyncio.run(aio_download()) #容易报错Error: Event loop is closed
    # asyncio.get_event_loop也会报错 
    # loop=asyncio.get_event_loop()
    # loop.run_until_complete(aio_download())


    # 抓取密钥key.key
    kkey=get_key(second_m3u8_file)
    # print(kkey) #key.key:57d17982aec9bda8
    # asyncio.run(aio_dec(kkey)) #解密、下载文件

    # 合并ts文件为mp4
    # merge_ts()





if __name__=='__main__':
    url='https://www.kuyun.tv/play/14453-0-0.html'
    main(url)