def validate_weather_data(data):
    """
    Perform data validation and quality checks on extracted data.
    Ensures that values fall within realistic boundaries.
    """
    if not data:
        return False
        
    try:
        # Check Temperature ranges (Earth limits)
        if not (-60 <= data['temperature'] <= 60):
            print(f"Validation failed: Invalid temperature {data['temperature']}")
            return False
            
        # Check Humidity (0-100%)
        if not (0 <= data['humidity'] <= 100):
            print(f"Validation failed: Invalid humidity {data['humidity']}")
            return False
            
        # Check Pressure (extreme weather bounds generally 800 - 1080 hPa)
        if not (800 <= data['pressure'] <= 1100):
            print(f"Validation failed: Invalid pressure {data['pressure']}")
            return False
            
        # Check proper formatting
        if not isinstance(data['condition'], str) or len(data['condition']) == 0:
            return False
            
        return True
        
    except KeyError as e:
        print(f"Validation failed: Missing key {e}")
        return False
