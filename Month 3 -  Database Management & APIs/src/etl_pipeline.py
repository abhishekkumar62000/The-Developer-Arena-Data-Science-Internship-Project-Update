from src.api_client import fetch_weather_data
from src.validators import validate_weather_data
from src.database import setup_database, get_or_create_city, insert_weather_data, log_etl_run
from config.settings import TARGET_CITIES
from datetime import datetime

def run_pipeline():
    """Main ETL Workflow."""
    print(f"\n[{datetime.now()}] Starting ETL Pipeline Run...")
    setup_database() # Ensure tables exist
    
    extracted_data = []
    
    # 1. EXTRACT
    for city in TARGET_CITIES:
        data = fetch_weather_data(city)
        if data:
            extracted_data.append(data)
            
    # 2. TRANSFORM (Validate & Clean)
    valid_data = []
    for data in extracted_data:
        if validate_weather_data(data):
            valid_data.append(data)
        else:
            print(f"Skipping {data['city']} due to validation failure.")
            
    # 3. LOAD
    success_count = 0
    try:
        for data in valid_data:
            city_id = get_or_create_city(data['city'], data.get('country', 'Unknown'))
            insert_weather_data(city_id, data)
            success_count += 1
            
        # Log success
        log_etl_run(status="Successful", records_processed=success_count)
        print(f"[{datetime.now()}] Pipeline finished successfully. {success_count} records loaded.")
    except Exception as e:
        # Log failure
        log_etl_run(status="Failed", records_processed=success_count, error_message=str(e))
        print(f"[{datetime.now()}] Pipeline failed: {e}")

if __name__ == "__main__":
    run_pipeline()
