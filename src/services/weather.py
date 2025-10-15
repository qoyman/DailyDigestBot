import os
import httpx

OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

async def get_weather_text(city: str) -> str:
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return "OpenWeather API key not configured. Set OPENWEATHER_API_KEY in .env"

    params = {"q": city, "appid": api_key, "units": "metric"}
    async with httpx.AsyncClient(timeout=15) as client:
        try:
            r = await client.get(OPENWEATHER_URL, params=params)
            r.raise_for_status()
            data = r.json()
        except httpx.HTTPError as e:
            return f"Weather lookup failed: {e}"

    name = data.get("name", city)
    main = data.get("weather", [{}])[0].get("main", "N/A")
    desc = data.get("weather", [{}])[0].get("description", "").title()
    temp = data.get("main", {}).get("temp", "N/A")
    feels = data.get("main", {}).get("feels_like", "N/A")

    return f"Weather in {name}: {main} ({desc}) | {temp}°C (feels {feels}°C)"