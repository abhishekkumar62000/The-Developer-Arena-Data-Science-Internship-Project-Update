# 🌥️ Complete Weather Data Pipeline System 
**Month 3: Database Management & APIs Internship Documentation**

---

## 1. 🎯 Project Overview
The **Complete Weather Data Pipeline System** is an end-to-end Data Engineering (ETL) pipeline created to extract real-time weather information from external APIs, transform and clean the data based on quality constraints, and load it securely into a normalized relational database (SQLite). 

**Primary Goals & Objectives:**
- Automate data extraction using HTTP API calls.
- Enforce strict Data Quality Checks (validating realistic temperature and humidity ranges).
- Learn and implement Database Normalization (3 tables with Primary/Foreign keys).
- Build automated job scheduling for persistent data collection and daily report generation with threshold alerts.

---

## 2. ⚙️ Setup Instructions
Follow these steps to configure and run the pipeline on your local machine.

### Prerequisites
- Python 3.8+ installed.
- SQLite3 (comes built-in with Python).

### Installation Steps
1. **Clone the Directory:** Ensure you are in the `Month 3 - Database Management & APIs` folder.
2. **Install Dependencies:** Run the following command in your terminal to install the necessary libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configuration:** 
   - Open `config/settings.py`.
   - Update `OPENWEATHER_API_KEY` with your actual OpenWeatherMap API key (If left unchanged, the system automatically uses a Mock API generator for safe testing).
4. **Run the Project:**
   - Execute the main automatic sequence:
     ```bash
     python main.py
     ```
   - To run the persistent background scheduler:
     ```bash
     python src/scheduler.py
     ```

---

## 3. 📂 Code Structure
The repository is modular and structured according to Data Engineering best practices:

```text
Month 3 - Database Management & APIs/
│
├── config/
│   └── settings.py         # System thresholds and API configurations
├── database/               # Houses the SQLite .db files
├── docs/                   # System documentation
├── scripts/
│   └── analyze_house_prices.py # Additional dataset analyzer script
├── src/
│   ├── api_client.py       # API connection and data extraction logic
│   ├── database.py         # Schema creation and DB connection logic
│   ├── etl_pipeline.py     # Main ETL execution flow
│   ├── reporter.py         # SQL aggregation and reporting logic
│   ├── scheduler.py        # Automated loop handling
│   └── validators.py       # Data quality constraints
├── logs/                   # System execution logs
├── reports/                # Output generated markdown/txt reports
├── main.py                 # Application entry point
├── requirements.txt        # Python external dependencies
└── README.md               # Quick setup overview
```

---

## 4. 🧠 Technical Details & ETL Workflow
**Architecture Overview:**
The pipeline follows a strict **Extract**, **Transform**, and **Load** (ETL) architecture:

1. **Extract (`api_client.py`)**: 
   Iterates through a configured list of targeting cities (`config/settings.py`). It uses the `requests` library to fetch JSON payloads. Timeout handling and Connection Exceptions are strictly dealt with to prevent pipeline crashes.
2. **Transform (`validators.py`)**: 
   The raw JSON is mapped into structured Python dictionaries. A data validation layer drops records that physically cannot exist (e.g., negative humidity or temperatures exceeding Earth's boundaries).
3. **Load (`database.py`)**: 
   Validated records are securely INSERTED into `cities` (if new) and `weather_data` using `SQLAlchemy/sqlite3`. Primary and Foreign keys secure the relationships.
4. **Report/Monitor (`reporter.py` & `scheduler.py`)**: 
   The system queries the latest runs, generates threshold alerts, outputs a formatted TXT report, and sets a timer to repeat every 60 minutes.

---

## 5. 🔌 API Documentation
**Service:** OpenWeatherMap API (Current Weather Data Endpoint)

- **Endpoint:** `GET http://api.openweathermap.org/data/2.5/weather`
- **Parameters:**
  - `q` (string, required): City name (e.g., "Mumbai").
  - `appid` (string, required): Developer's unique API Key.
  - `units` (string, optional): Use "metric" to return Celsius instead of Kelvin.
  
**Sample JSON Response:**
```json
{
  "weather": [{"description": "clear sky"}],
  "main": {
    "temp": 28.5,
    "pressure": 1012,
    "humidity": 65
  },
  "wind": {"speed": 4.1},
  "sys": {"country": "IN"},
  "name": "Mumbai"
}
```

---

## 6. 🗄️ Database Schema
The database uses a 3-table normalized relational layout.

### Table Relationships (ER Mapping)
1. **`cities`**: Core dimension table.
   - `city_id` (INTEGER, Primary Key)
   - `city_name` (TEXT, Unique)
   - `country` (TEXT)
   - `created_at` (TIMESTAMP)

2. **`weather_data`**: The Main Fact Table. Tracks temporal metrics.
   - `record_id` (INTEGER, Primary Key)
   - `city_id` (INTEGER, Foreign Key -> `cities.city_id`)
   - `timestamp` (TIMESTAMP)
   - `temperature_c` (REAL)
   - `humidity` (INTEGER)
   - `pressure_hpa` (REAL)
   - `wind_speed_mps` (REAL)
   - `weather_condition` (TEXT)

3. **`etl_logs`**: System monitoring table.
   - `log_id` (INTEGER, Primary Key)
   - `execution_time` (TIMESTAMP)
   - `status` (TEXT)
   - `records_processed` (INTEGER)
   - `error_message` (TEXT)

---

## 7. 🧪 Testing Evidence
**Data Validation Implementation:**
The `validators.py` file applies unit-test-like logic bounds against the extracted variables before database loading.
*Examples of implemented validation checks:*
- `Temperature`: Must be strictly between `-60°C` and `60°C`.
- `Humidity`: Must be between `0%` and `100%`.
- `Condition string`: Must not be null/empty.

Records that fail these conditional blocks are intentionally "dropped," triggering an `Exception skip` in the logs to prevent database poisoning. Mock JSON data is used during development to simulate and test edge-case failures.

---

## 8. 🖼️ Visual Documentation (Screenshots)

*(Add your screenshots here for submission)*

1. **Successful Terminal Execution (Auto Run)**
   > `[Insert Screenshot of the terminal output displaying the final Auto-Report with Alerts]`

2. **Database View**
   > `[Insert Screenshot of DB Browser or SQLite viewer showing table schemas]`

3. **Analyzed Output Report**
   > `[Insert Screenshot of the generated "reports/latest_report.txt" showing tracked metrics]`

---
*End of Documentation*