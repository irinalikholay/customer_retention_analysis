import pandas as pd
from pathlib import Path 
import sqlite3

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

    return df


def clean_data(df):
    print("Starting data cleaning...\n")

    initial_shape = df.shape
    print(f"Initial shape: {initial_shape}")
    
    #Remove missing Customer ID
    df =df.dropna(subset=["Customer ID"])
    print(f"After removing missing Customer ID: {df.shape}")
    
    #Remove cancelled invoices
    df = df[~df["Invoice"].astype(str).str.startswith("C")]
    print(f"After removing cancelled invoices: {df.shape}")
    
    #Remove negatibe quantity
    df = df[df["Quantity"] > 0]
    print(f"After removing negative quantity: {df.shape}")
    
    #Remove zero or negative price
    df = df[df["Price"] > 0]
    print(f"After removing zero/negative price: {df.shape}")

    #Convert InvoiceDate to datatime
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    
    #Create revenue column
    df["Revenue"] = df["Quantity"] * df["Price"]

    print(f"\nFinal cleaned shape: {df.shape}")

    return df


def save_to_database(df):
    print("\nSaving to SQLite database...\n")

    db_path = BASE_DIR / "database" / "customer_retention.db"

    conn = sqlite3.connect(db_path)

    df.to_sql(
        "orders",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    print("Data successfully saved to database.")


if __name__ == "__main__":
    df = explore_data()
    df_clean = clean_data(df)
    save_to_database(df_clean)