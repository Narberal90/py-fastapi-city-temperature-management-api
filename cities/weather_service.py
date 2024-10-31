import os

import httpx
from dotenv import load_dotenv

load_dotenv()


async def fetch_weather(city_name: str):
    api_key = os.getenv("WEATHER_API_KEY")
    url = (
        f"http://api.weatherapi.com/v1/current.json?"
        f"key={api_key}&q={city_name}&aqi=no"

    )
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            return data["current"]["temp_c"]
        except httpx.HTTPStatusError as e:
            print(f"Error fetching weather for {city_name}: {e}")
            return None
