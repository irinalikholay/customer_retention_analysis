import pandas as pd
from pathlib import Path 

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "raw" / "online_retail_II.csv"

# Load and Explore Data

def explore_data():
    print("Loading dataset...\n")

    df = pd.read_csv(DATA_PATH, encoding="ISO-8859-1")

    print("Dataset loaded.\n")

    print("--- SHAPE ---")
    print(df.shape)

    print("\n--- FIRST 5 ROWS ---")
    print(df.head())

    print("\n--- DATA INFO ---")
    print(df.info())

    print("\n--- MISSING VALUES ---")
    print(df.isna().sum())

    print("\n--- NEGATIVE QUANTITY ---")
    print((df["Quantity"] <= 0).sum())

    print("\n--- ZERO OR NRGATIVE PRICE ---")
    print((df["Price"] <= 0).sum())

    print("\n--- CANCELLED INVOICES ---")
    print(df["Invoice"].astype(str).str.startswith("C").sum())

if __name__ == "__main__":
    explore_data()