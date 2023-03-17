from multiprocessing import Process

def func(name):
    for i in range(1000):
        print(name, i)
    

if __name__ == '__main__':
    p1 = Process(target=func, args=("周杰伦", ))
    p2 = Process(target=func, args=("王富贵", ))
    p1.start()
    p2.start()