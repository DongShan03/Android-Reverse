import aiohttp, aiofiles, asyncio


async def download(url):
    file_name = url.split("/")[-1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            # await resp.text()
            content = await resp.content.read()
            # 写文件
            async with aiofiles.open(file_name, mode="wb") as f:
                await f.write(content)

async def main():
    url_list = [
        "1",
        "2",
        "3",
    ]
    tasks = []
    for url in url_list:
        t = asyncio.create_task(download(url))
        tasks.append(t)
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())
