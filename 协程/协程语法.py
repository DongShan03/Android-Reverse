import asyncio


async def func():
    print("shabi")


if __name__ == "__main__":
    f = func()

    # event_loop = asyncio.get_event_loop()
    # event_loop.run_until_complete(f)

    asyncio.run(f)