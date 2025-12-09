import aiohttp
import asyncio
from __init__ import config


async def get_data(latitude, longitude):
    async with aiohttp.ClientSession() as session:
        response = await session.get(f'https://api.weatherapi.com/v1//current.json?key={config["api_token"]}&q={latitude},{longitude}')
        return await response.json()
            

