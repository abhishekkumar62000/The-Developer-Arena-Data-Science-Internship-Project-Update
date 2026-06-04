import sqlite3
import os
import sys

# Add root to python path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.settings import DB_PATH

def get_connection():
    """Establish and return a database connection."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Returns dict-like rows
    return conn

def setup_database():
    """Initialize the schema with 3 normalized tables: cities, weather_data, etl_logs."""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Table 1: cities
    cursor.execute('''CREATE TABLE IF NOT EXISTS cities (
                        city_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        city_name TEXT UNIQUE NOT NULL,
                        country TEXT,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )''')
    
    # Table 2: weather_data
    cursor.execute('''CREATE TABLE IF NOT EXISTS weather_data (
                        record_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        city_id INTEGER,
                        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        temperature_c REAL,
                        humidity INTEGER,
                        pressure_hpa REAL,
                        wind_speed_mps REAL,
                        weather_condition TEXT,
                        FOREIGN KEY (city_id) REFERENCES cities (city_id)
                    )''')
                    
    # Table 3: etl_logs
    cursor.execute('''CREATE TABLE IF NOT EXISTS etl_logs (
                        log_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        execution_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        status TEXT,
                        records_processed INTEGER,
                        error_message TEXT
                    )''')
    
    conn.commit()
    conn.close()

def get_or_create_city(city_name, country="Unknown"):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT city_id FROM cities WHERE city_name = ?", (city_name,))
    result = cursor.fetchone()
    
    if result:
        city_id = result['city_id']
    else:
        cursor.execute("INSERT INTO cities (city_name, country) VALUES (?, ?)", (city_name, country))
        conn.commit()
        city_id = cursor.lastrowid
        
    conn.close()
    return city_id

def insert_weather_data(city_id, data):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO weather_data 
                      (city_id, temperature_c, humidity, pressure_hpa, wind_speed_mps, weather_condition)
                      VALUES (?, ?, ?, ?, ?, ?)''', 
                   (city_id, data['temperature'], data['humidity'], data['pressure'], data['wind_speed'], data['condition']))
    conn.commit()
    conn.close()

def log_etl_run(status, records_processed, error_message=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO etl_logs (status, records_processed, error_message)
                      VALUES (?, ?, ?)''', (status, records_processed, error_message))
    conn.commit()
    conn.close()
