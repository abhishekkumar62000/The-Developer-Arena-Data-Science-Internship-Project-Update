import pandas as pd
import os
import sqlite3

def analyze_dataset():
    """
    Requested secondary task: Analyzing the house_prices.csv dataset
    using Month 3 DB / Data quality principles.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, 'house_prices.csv')
    
    if not os.path.exists(csv_path):
        print(f"Dataset not found at {csv_path}. Please place house_prices.csv in the Month 3 root folder.")
        return
        
    print(f"Loading '{csv_path}' for Data Engineering Analysis...")
    df = pd.read_csv(csv_path)
    
    # Simulating data validation / quality checks (Month 3 concepts)
    print("\n--- Data Quality Checks ---")
    null_counts = df.isnull().sum()
    columns_with_nulls = null_counts[null_counts > 0]
    if not columns_with_nulls.empty:
        print(f"Found missing values in {len(columns_with_nulls)} columns.")
        print(columns_with_nulls.head())
    else:
        print("No missing values found.")
        
    print("\n--- Data Dictionary / Schema Info ---")
    print(df.info())
    
    print("\n--- Saving to SQLite Analytics DB ---")
    db_path = os.path.join(base_dir, 'database', 'house_prices_analytics.db')
    conn = sqlite3.connect(db_path)
    df.to_sql('house_prices', conn, if_exists='replace', index=False)
    
    print(f"Successfully ran ETL process on house_prices.csv into {db_path} database.")
    
    # Query test
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM house_prices")
    print(f"Total verified records loaded: {cursor.fetchone()[0]}")
    conn.close()

if __name__ == "__main__":
    analyze_dataset()
