# 多线程

# def func():
#     for i in range(4):
#         print('func',i)

# print(__name__) #-> __main__
# if __name__=='__main__':
#     func()
#     for i in range(3):
#         print('hello',i)

# from threading import Thread

# def func():
#     for i in range(5):
#         print('func',i)


# if __name__=='__main__':
#     t=Thread(target=func) #创建线程并给线程安排任务
#     t.start() #多线程状态可以开始工作，具体执行时间有CPU决定
#     for i in range(3):
#         print('hello',i)

class MyThread(Thread):
    def run(self):
        for i in range(10):
            print('子线程',i)


if __name__=='__main__':
    t=MyThread()
    # t.run() # .run() 是单线程
    t.start() #开启多线程

    for i in range(5):
        print('方法2',i)
