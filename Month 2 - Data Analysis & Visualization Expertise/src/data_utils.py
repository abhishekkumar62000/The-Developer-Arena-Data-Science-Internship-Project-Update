import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_explore(filename):
    """Loads a dataset from the data folder and prints basic exploratory info."""
    filepath = os.path.join("data", filename)
    if not os.path.exists(filepath):
        print(f"File {filename} not found in the data directory!")
        return None
        
    df = pd.read_csv(filepath)
    print(f"--- Dataset Info for {filename} ---")
    print(f"Shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    print("\nFirst 5 rows:")
    print(df.head())
    print("\nMissing values:")
    print(df.isnull().sum())
    return df

def save_visualization(fig, filename):
    """Saves a matplotlib figure into the visualizations folder."""
    os.makedirs(os.path.join("visualizations"), exist_ok=True)
    filepath = os.path.join("visualizations", filename)
    fig.savefig(filepath, bbox_inches="tight", dpi=300)
    print(f"Saved visualization to {filepath}")

def generate_report_markdown(title, sections, filename):
    """Generates a structured markdown report saving it to the reports folder."""
    os.makedirs(os.path.join("reports"), exist_ok=True)
    filepath = os.path.join("reports", filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n")
        f.write("==================================\n\n")
        for heading, content in sections.items():
            f.write(f"## {heading}\n")
            f.write(f"{content}\n\n")
    print(f"Report saved to {filepath}")
