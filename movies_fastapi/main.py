import logging

import aiohttp
import aioredis
import uvicorn
from elasticsearch import AsyncElasticsearch
from fastapi import FastAPI, Request
from fastapi.responses import ORJSONResponse, Response
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from api.v1 import films, genres, persons
from core.config import settings
from db import elastic, redis

app = FastAPI(
    title=settings.project_name,
    docs_url='/movies_fastapi/api/openapi',
    openapi_url='/movies_fastapi/api/openapi.json',
    default_response_class=ORJSONResponse,
)


@app.on_event('startup')
async def startup():
    # Мы отказались от фабричных функций create_redis(),
    # create_redis_pool(), create_pool()и т. д. после того,
    # как сделали проект совместимым с redis-py.
    # https://aioredis.readthedocs.io/en/latest/migration/
    redis.redis = await aioredis.from_url(
        f'redis://{settings.redis_host}:{settings.redis_port}',
        decode_responses=True, max_connections=20)
    elastic.es = AsyncElasticsearch(
        hosts=[f'{settings.elastic_host}:{settings.elastic_port}'],
        timeout=10)
    # Смотрим тут, если чего: https://pypi.org/project/fastapi-cache2/
    FastAPICache.init(RedisBackend(redis.redis), prefix='fastapi-cache')


@app.on_event('shutdown')
async def shutdown():
    redis.redis.close()
    await redis.redis.close()
    await elastic.es.close()

app.include_router(films.router, prefix='/movies_fastapi/api/v1/films',
                   tags=['films'])
app.include_router(genres.router, prefix='/movies_fastapi/api/v1/genres',
                   tags=['genres'])
app.include_router(persons.router, prefix='/movies_fastapi/api/v1/persons',
                   tags=['persons'])


@app.middleware('http')
async def check_user(request: Request, call_next):
    request_url = request.url
    logging.error('INFO MIDDLEWARE request - %s', request.url)
    if 'http://127.0.0.1/movies_fastapi/api/openapi' == request.url or 'http://127.0.0.1/movies_fastapi/api/openapi.json' == request.url:
        return await call_next(request)
    headers = request.headers
    async with aiohttp.ClientSession() as client:
        resp = await client.get(settings.check_user_url, headers=headers)
        logging.error('INFO MIDDLEWARE status_code - %s', resp.status)
        if resp.status == 200:
            response = await call_next(request)
            return response
        return Response(status_code=401)

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000,)
