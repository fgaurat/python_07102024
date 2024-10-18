import asyncio
import time

async def add(a,b):
    await asyncio.sleep(1)
    return a+b

async def main():
    # print('Hello ...')
    # await asyncio.sleep(1)
    # print('... World!')    
    start = time.perf_counter()
    # a = await add(2,3)
    # print(a)
    # a = await add(2,3)
    # print(a)
    
    all = [add(2,3),add(2,3),add(2,3),add(2,3)]
    r = await asyncio.gather(*all)
    print(r)
    end = time.perf_counter()
    print(f"{end-start:.2}s")

asyncio.run(main())