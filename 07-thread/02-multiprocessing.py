from multiprocessing import Process

# def func():
#     for i in range(1000): #数值够大才能看出来多进程
#         print('子进程',i)

# if __name__=='__main__':
#     p=Process(target=func)
#     p.start()
#     for i in range(1000):
#         print('main',i)

class MyProcess(Process): 
    def run(self):
        for i in range(100): #数值够大才能看出来多进程
            print('子进程', i)

if __name__=='__main__':
    p=MyProcess()
    p.start()
    for i in range(50):
        print('main',i)


