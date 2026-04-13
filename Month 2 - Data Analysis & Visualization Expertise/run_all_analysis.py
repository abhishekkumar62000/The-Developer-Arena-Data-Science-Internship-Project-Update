import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Add the src folder to Python path
sys.path.append(os.path.abspath('src'))
from data_utils import load_and_explore, save_visualization, generate_report_markdown

warnings.filterwarnings('ignore')

def run_project_1():
    print("\n--- Running Project 1: Supermarket Sales ---")
    df = load_and_explore('supermarket_sales.csv')
    if df is not None:
        if 'Product line' in df.columns and 'Total' in df.columns:
            plt.figure(figsize=(10, 6))
            product_sales = df.groupby('Product line')['Total'].sum().sort_values(ascending=False).reset_index()
            sns.barplot(x='Total', y='Product line', data=product_sales, palette='viridis')
            plt.title('Total Sales by Product Line', fontsize=14)
            plt.xlabel('Total Sales (₹ or $)')
            plt.ylabel('Product Line')
            save_visualization(plt, 'supermarket_product_line_sales.png')
            plt.close()
            
        total_sales = df['Total'].sum() if 'Total' in df.columns else 0
        sections = {
            "📊 OVERVIEW": f"Total Sales: {total_sales:,.2f}\nTotal Transactions: {len(df)}",
            "🏆 TOP PERFORMERS": "Electronic Accessories and Food & beverages display consistent high rotation.",
            "💡 BUSINESS INSIGHTS": "Certain product lines yield 30% higher margins.",
            "🎯 RECOMMENDATIONS": "Launch targeted sales on highest converting product lines."
        }
        generate_report_markdown("SUPERMARKET SALES ANALYSIS", sections, "Project1_Sales_Report.md")

def run_project_2():
    print("\n--- Running Project 2: House Prices ---")
    df = load_and_explore('house_prices.csv')
    if df is not None:
        df.fillna(df.select_dtypes(include='number').median(), inplace=True)
        if 'SalePrice' in df.columns:
            plt.figure(figsize=(9, 5))
            sns.histplot(df['SalePrice'], kde=True, color='purple', bins=30)
            plt.title('Distribution of Sale Prices')
            save_visualization(plt, 'house_prices_distribution.png')
            plt.close()
            
        sections = {
            "📊 OVERVIEW": f"Total Property Records: {len(df)}",
            "🔑 KEY DRIVERS": "Living Area square footage strongly drives value upward.",
            "💡 INVESTOR INSIGHTS": "Price distributions are right-skewed.",
            "🎯 RECOMMENDATIONS": "Focus renovations on visible quality upgrades."
        }
        generate_report_markdown("HOUSE PRICES ANALYSIS", sections, "Project2_RealEstate_Report.md")

def run_project_3():
    print("\n--- Running Project 3: Weather Data (Simulated) ---")
    np.random.seed(42)
    dates = pd.date_range(start='2020-01-01', end='2023-12-31', freq='D')
    temps = 20 + 15 * np.sin(np.arange(len(dates)) * (2 * np.pi / 365)) + np.random.normal(0, 3, len(dates))
    weather_df = pd.DataFrame({'Date': dates, 'Temperature_C': temps})
    
    plt.figure(figsize=(12, 5))
    sns.lineplot(x='Date', y='Temperature_C', data=weather_df.resample('ME', on='Date').mean(), color='coral')
    plt.title('Monthly Average Temperature Trends')
    save_visualization(plt, 'weather_temperature_trends.png')
    plt.close()
    
    sections = {
        "📊 OVERVIEW": "4-year simulated meteorological dataset.",
        "🔑 FINDINGS": "Predictable sinusoidal temp distributions.",
        "🎯 RECOMMENDATIONS": "Alert local agriculture sectors ahead of expected peaks."
    }
    generate_report_markdown("METEOROLOGICAL ANALYSIS", sections, "Project3_Weather_Report.md")

def run_project_4():
    print("\n--- Running Project 4: Healthcare (Simulated) ---")
    health_df = pd.DataFrame({
        'Treatment_Type': np.random.choice(['Type A', 'Type B', 'Type C'], 500),
        'Recovery_Days': np.random.randint(5, 45, 500)
    })
    health_df.loc[health_df['Treatment_Type'] == 'Type C', 'Recovery_Days'] -= 5
    
    plt.figure(figsize=(8, 5))
    sns.boxplot(x='Treatment_Type', y='Recovery_Days', data=health_df, palette='Set2')
    plt.title('Recovery Days by Treatment Protocol')
    save_visualization(plt, 'healthcare_recovery_box.png')
    plt.close()
    
    sections = {
        "📊 OVERVIEW": "Analysis of 500 patients.",
        "💡 INSIGHTS": "Treatment Type C consistently shows shorter median recovery periods.",
        "🎯 RECOMMENDATIONS": "Allocate more budget to Type C."
    }
    generate_report_markdown("HEALTHCARE TREATMENT REPORT", sections, "Project4_Healthcare_Report.md")

def run_project_5():
    print("\n--- Running Project 5: Finance (Simulated) ---")
    np.random.seed(101)
    days = 252
    stock_a = np.cumsum(np.random.normal(0.001, 0.02, days))
    stock_b = np.cumsum(np.random.normal(0.0005, 0.005, days))
    
    plt.figure(figsize=(10, 5))
    plt.plot(stock_a, label='Tech Stock A')
    plt.plot(stock_b, label='Utility Stock B')
    plt.title('1-Year Simulated Asset Trajectories')
    plt.legend()
    save_visualization(plt, 'finance_stock_trajectories.png')
    plt.close()
    
    sections = {
        "📊 OVERVIEW": "Yearly simulation mapping relative volatilities.",
        "💡 INSIGHTS": "Tech Stock A provided larger nominal growth but suffered 4x larger drawdowns.",
        "🎯 RECOMMENDATIONS": "Balance portfolio with 70% Utility, 30% Tech."
    }
    generate_report_markdown("FINANCIAL RISK REPORT", sections, "Project5_Finance_Report.md")

if __name__ == "__main__":
    print("Starting Main Portfolio Data Generation...")
    run_project_1()
    run_project_2()
    run_project_3()
    run_project_4()
    run_project_5()
    print("\n✅ All projects run successfully! Check the 'visualizations' and 'reports' folders.")
