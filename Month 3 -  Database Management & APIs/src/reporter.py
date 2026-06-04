import os
from src.database import get_connection
from config.settings import THRESHOLDS, BASE_DIR

def generate_report():
    conn = get_connection()
    cursor = conn.cursor()
    
    report_lines = []
    report_lines.append("WEATHER DATA PIPELINE SYSTEM")
    report_lines.append("=============================\n")
    
    # SYSTEM STATUS
    cursor.execute("SELECT * FROM etl_logs ORDER BY execution_time DESC LIMIT 1")
    last_log = cursor.fetchone()
    
    report_lines.append("📊 SYSTEM STATUS: RUNNING")
    if last_log:
        report_lines.append(f"⏰ Last Run: {last_log['execution_time']}")
        report_lines.append(f"✅ Status: {last_log['status']}")
        report_lines.append(f"📈 Records Processed: {last_log['records_processed']} cities\n")
    else:
        report_lines.append("No ETL runs registered yet.\n")
        
    # CURRENT WEATHER SNAPSHOT
    report_lines.append("🌤️ CURRENT WEATHER SNAPSHOT:")
    report_lines.append("---------------------------------")
    cursor.execute('''SELECT c.city_name, w.temperature_c, w.humidity, w.weather_condition 
                      FROM weather_data w 
                      JOIN cities c ON w.city_id = c.city_id 
                      WHERE w.record_id IN (
                          SELECT MAX(record_id) FROM weather_data GROUP BY city_id
                      )''')
    snapshots = cursor.fetchall()
    for row in snapshots:
        report_lines.append(f"📍 {row['city_name']}: {row['temperature_c']}°C, {row['humidity']}% humidity, {row['weather_condition']}")
    report_lines.append("")
    
    # ALERTS
    report_lines.append("📅 TODAY'S ALERTS:")
    alert_count = 0
    for row in snapshots:
        if row['temperature_c'] > THRESHOLDS['MAX_TEMP_C']:
            report_lines.append(f"• High temperature alert: {row['city_name']} ({row['temperature_c']}°C > {THRESHOLDS['MAX_TEMP_C']}°C threshold)")
            alert_count += 1
        if row['humidity'] > THRESHOLDS['MAX_HUMIDITY']:
            report_lines.append(f"• High humidity alert: {row['city_name']} ({row['humidity']}% > {THRESHOLDS['MAX_HUMIDITY']}% threshold)")
            alert_count += 1
    if alert_count == 0:
        report_lines.append("• No critical alerts today.")
    report_lines.append("")
    
    # DATABASE STATS
    cursor.execute("SELECT COUNT(*) as tot FROM weather_data")
    total_records = cursor.fetchone()['tot']
    
    cursor.execute("SELECT COUNT(*) as tot FROM cities")
    total_cities = cursor.fetchone()['tot']
    
    report_lines.append("📊 DATABASE STATISTICS:")
    report_lines.append(f"• Total records: {total_records}")
    report_lines.append(f"• Cities tracked: {total_cities}")
    
    err_msg = last_log['error_message'] if last_log and last_log['error_message'] else 'None'
    report_lines.append(f"• Last error: {err_msg}")
    
    conn.close()
    
    full_report = "\n".join(report_lines)
    
    # Save Report
    report_path = os.path.join(BASE_DIR, 'reports', 'latest_report.txt')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(full_report)
        
    print(full_report)
    return full_report
