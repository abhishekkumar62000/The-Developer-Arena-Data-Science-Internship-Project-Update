import requests
from config.settings import BASE_URL, OPENWEATHER_API_KEY
from datetime import datetime

def fetch_weather_data(city):
    """Fetch real-time weather data from OpenWeatherMap API."""
    # Since we don't have a real API key, we will mock the response if the specific 'YOUR_API_KEY_HERE' is used
    if OPENWEATHER_API_KEY == "YOUR_API_KEY_HERE":
        return _mock_fetch(city)

    params = {
        'q': city,
        'appid': OPENWEATHER_API_KEY,
        'units': 'metric'
    }
    
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        return {
            'city': city,
            'country': data['sys']['country'],
            'timestamp': datetime.now(),
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'wind_speed': data['wind']['speed'],
            'condition': data['weather'][0]['description']
        }
    except requests.exceptions.RequestException as e:
        print(f"API Error for {city}: {e}")
        return None

def _mock_fetch(city):
    """Mock API response for safely testing the pipeline locally."""
    import random
    return {
        'city': city,
        'country': 'IN' if city in ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Kolkata'] else 'US',
        'timestamp': datetime.now(),
        'temperature': round(random.uniform(15.0, 38.0), 1),
        'humidity': random.randint(40, 90),
        'pressure': random.randint(1000, 1020),
        'wind_speed': round(random.uniform(1.0, 15.0), 1),
        'condition': random.choice(['Clear sky', 'Partly cloudy', 'Light rain', 'Sunny', 'Cloudy', 'Thunderstorm'])
    }
