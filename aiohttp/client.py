import asyncio

import aiohttp


async def get_google():
    async with (aiohttp.ClientSession() as session):
        async with session.get('http://0.0.0.0:8080/popular') as response:
            response_json = await response.json()
            for movie in response_json.get('movies', []):
                print(f"Title: {movie['title']}, Rating: {movie['rating']}, Year: {movie['year']}, Genre: {movie['genre']}")


asyncio.run(get_google())


