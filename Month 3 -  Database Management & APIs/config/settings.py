import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Database configuration
DB_PATH = os.path.join(BASE_DIR, 'database', 'weather_data.db')

# API Configuration
# Note: In a real enterprise app, you should use environment variables (os.getenv)
OPENWEATHER_API_KEY = "YOUR_API_KEY_HERE"  # Replace with actual key for real execution
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# ETL Configuration
TARGET_CITIES = ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Kolkata', 'New York', 'London', 'Tokyo']

# Thresholds for alerts
THRESHOLDS = {
    'MAX_TEMP_C': 35.0,
    'MIN_TEMP_C': 0.0,
    'MAX_HUMIDITY': 85
}
