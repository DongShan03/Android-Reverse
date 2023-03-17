import asyncio

async def func1():
    print("func1")

async def func2():
    print("func2")

async def func3():
    print("func3")

async def download(url):
    print("download" + url)
    await asyncio.sleep(1)
    print("finished downloading" + url)

async def main():
    urls = [
        "1",
        "2",
        "3",
    ]
    tasks = []
    for url in urls:
        task = asyncio.create_task(download(url))
        tasks.append(task)
    # await asyncio.wait(tasks)  #wait无序
    await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    # f1 = func1()
    # f2 = func2()
    # f3 = func3()
    # tasks = [f1, f2, f3]

    # asyncio.run(asyncio.wait(tasks)) 

    asyncio.run(main())