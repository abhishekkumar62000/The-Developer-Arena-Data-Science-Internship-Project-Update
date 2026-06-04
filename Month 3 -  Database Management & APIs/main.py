from src.etl_pipeline import run_pipeline
from src.reporter import generate_report
from src.scheduler import start_scheduler
import sys

def main():
    print("Welcome to the Weather Data ETL Pipeline System")
    print("-----------------------------------------------")
    print("Running Data ETL Pipeline Automatically...")
    run_pipeline()
    print("\nGenerating System Report Automatically...")
    generate_report()
    print("\n✅ Project Auto-Run Completed Successfully!")

if __name__ == "__main__":
    main()
