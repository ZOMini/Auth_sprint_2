import asyncio
import logging
import time

import aiohttp
from config import settings

REQUEST_COUNT = 500


async def ahttp_test(i):
    async with aiohttp.ClientSession() as client:
        user_agent = f'UserAgent - {i}'
        headers = {'User-Agent': user_agent, 'CONTENT-TYPE': 'application/json',
                   'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3NDg0NTY0MywianRpIjoiOTFhMjA1YzUtMzgxZS00NWYyLTgyNjAtOGRlMzM2ZmI4M2VhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjA0Y2E4ZDAwLTIwNjEtNGQ3MS05OGZiLTBiZGYwYjhkNDI0ZiIsIm5iZiI6MTY3NDg0NTY0MywiZXhwIjoxNjc0ODQ5MjQzLCJ1YSI6MzI2NzI1NzMsImVtYWlsIjoiZWUtMTJAeWEucnUiLCJyb2xlcyI6W119.j4iKlFx3cAzTmnywvrW3Qje_dnrvlvWvIYD9CqsmM0Y'
                   }
        await client.get(settings.test_host, headers=headers)


async def main():
    start_time = time.time()
    # error = 0
    tasks = [asyncio.ensure_future(
             ahttp_test(i)) for i in range(1, REQUEST_COUNT)]
    await asyncio.wait(tasks)
    logging.error('INFO - All ok - hz error, time - %s seconds', (time.time() - start_time))


loop = asyncio.new_event_loop()
loop.run_until_complete(main())
loop.close()
