import asyncio
import logging
import time

import aiohttp
from config import settings


async def ahttp_test(ua: int):
    async with aiohttp.ClientSession() as client:
        user_agent = f'UserAgent - {ua}'
        headers = {'User-Agent': user_agent, 'CONTENT-TYPE': 'application/json',
                   'Authorization': f'Bearer {settings.JWT}'
                   }
        await client.get(settings.TEST_URL, headers=headers)


async def main():
    start_time = time.time()
    # error = 0
    tasks = [asyncio.ensure_future(
             ahttp_test(ua)) for ua in range(settings.REQUESTS_COUNT)]
    await asyncio.wait(tasks)
    logging.error('INFO - All ok - hz error, time - %s seconds', (time.time() - start_time))


loop = asyncio.new_event_loop()
loop.run_until_complete(main())
loop.close()
