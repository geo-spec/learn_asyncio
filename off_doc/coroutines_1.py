import asyncio

async def main():
    print('one')
    await asyncio.sleep(10)
    print('two')

asyncio.run(main())