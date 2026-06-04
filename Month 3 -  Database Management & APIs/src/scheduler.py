import schedule
import time
from src.etl_pipeline import run_pipeline
from src.reporter import generate_report

def job():
    run_pipeline()
    generate_report()

def start_scheduler(interval_minutes=60):
    print(f"Starting Scheduler. ETL job will run every {interval_minutes} minutes.")
    # Run immediately first
    job()
    
    # Schedule subsequent
    schedule.every(interval_minutes).minutes.do(job)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    start_scheduler(interval_minutes=5)
