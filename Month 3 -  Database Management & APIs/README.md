# Month 3: Database Management & APIs
## Project: Complete Weather Data Pipeline System

### 📚 Project Overview
An end-to-end data engineering pipeline that extracts weather data from the OpenWeatherMap API, transforms and cleans the data, and loads it into a normalized SQLite Database. Features automated scheduling, data quality validation, and alert/report generation.

### 🛠️ Technical Implementation
- **Extract**: Reaches out to OpenWeatherMap API using `requests`. Handles timeouts and API keys cleanly.
- **Transform**: Filters data through `validators.py` to ensure weather metrics (temperature, humidity bounding) are physically possible before saving them.
- **Load**: Commits cleaned dictionaries into an optimized SQLite3 layout consisting of 3 normalized tables: `cities`, `weather_data`, and `etl_logs`.
- **Reporting**: Pulls SQL aggregations and JOINs to build a terminal/txt printed report with threshold Alerts.
- **Scheduler**: Allows running the workflow iteratively every N minutes autonomously. 

### 📁 Structure
- `config/settings.py` - Core parameters, api keys, targets.
- `src/database.py` - Core SQLite connection, schema instantiation, writes.
- `src/api_client.py` - Remote API integration logic.
- `src/validators.py` - Clean ETL transform validation gates.
- `src/etl_pipeline.py` - Orchestrates Extract -> Transform -> Load path.
- `src/reporter.py` - Query database and build `reports/latest_report.txt`.
- `src/scheduler.py` - Continuous operation scheduling loop.
- `main.py` - CLI menu entry point.

### 🚀 Setup Instructions
1. Install the dependencies using `pip install -r requirements.txt`.
2. Configure your OpenWeather API Key in `config/settings.py`. (The project works out of the box with a Mock Fetcher allowing evaluation without an API Key!).
3. Run the application via `python main.py`.
4. Choose option `1` to run a manual ETL pass, and option `2` to view the comprehensive Database statistical report.
