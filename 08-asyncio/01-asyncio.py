# 协程 IO操作

from asyncio import tasks
import time

# def func():
#     print('黄桃罐头')
#     time.sleep(2) #阻塞线程，此时cpu暂停此任务
#     print('过期了')

# if __name__=='__main__':
#     func()

# '''
# 其他阻塞状态:
# input()
# requests.get()
# IO操作:input/output，这个可以通过协程解决
# '''

import asyncio


# async def func():
#     print('你好')

async def func1():
    # time.sleep(2) #程序出现同步操作后，异步会被中断
    print('黄桃罐头')
    # await=挂起异步操作
    await asyncio.sleep(3)  # 异步操作，提醒切换操作
    print('我是asyncio:黄桃操作延迟3秒')


async def func2():
    print('咖啡')
    # time.sleep(3)
    await asyncio.sleep(3)
    print('我是asyncio:咖啡操作延迟3秒')


async def func3():
    print('果茶')
    await asyncio.sleep(2)
    print('asyncio:果茶好喝延迟2秒')

# if __name__ == '__main__':
#     g = func()
#     asyncio.run(g)

# 基础写法（不推荐）
# if __name__ == '__main__':
#     f1 = func1()
#     f2 = func2()
#     f3 = func3()
#     tasks = [f2, f3, f1]
#     t1 = time.time()  # 程序开始执行时间
#     # 倒序执行
#     asyncio.run(asyncio.wait(tasks))
#     t2 = time.time()
#     print(t2-t1)  # 程序执行完毕时间

# # 推荐写法
# async def main():
#     # 写法1：
#     # f1=func1()
#     # await f1
#     # 写法2：
#     tasks=[func1(),func2(),func3()]
#     await asyncio.wait(tasks)

# if __name__ == '__main__':
#     t1 = time.time()    # 程序开始执行时间
#     asyncio.run(main())
#     t2 = time.time()    # 程序执行完毕时间
#     print(t2-t1) 

async def download():
    print('准备下载')
    await asyncio.sleep(2) #假装网络请求
    print('下载完成')

async def main():
    urls=[
        "http://www.baidu.com",
        'https://www.sougou.com',
        'https://www.bing.com'
    ]
    tasks=[]
    for url in urls:
        d=download(url)
        tasks.append(d)
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())
