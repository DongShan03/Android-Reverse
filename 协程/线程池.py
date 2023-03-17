from concurrent.futures import ThreadPoolExecutor

def func(name):
    for i in range(10):
        print(name, i)

if __name__ == '__main__':
    with ThreadPoolExecutor(10) as t:
        for i in range(100):
            t.submit(func, f"周杰伦{i}")