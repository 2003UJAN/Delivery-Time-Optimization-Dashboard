import pandas as pd
import os
from src.data_generator import generate_synthetic_data

def load_data():
    path = "data/delivery_data.csv"
    if not os.path.exists(path):
        print("⚠️ Data file not found. Generating synthetic delivery data...")
        generate_synthetic_data()
    return pd.read_csv(path, parse_dates=["start_time", "end_time"])

def get_avg_delivery_time(df):
    df["delivery_time"] = (df["end_time"] - df["start_time"]).dt.total_seconds() / 60
    return df.groupby("location")["delivery_time"].mean().reset_index()

def get_volume_by_location(df):
    return df["location"].value_counts().reset_index().rename(columns={"index": "location", "location": "order_count"})

def get_delay_alerts(df):
    return df[df["delay"] == 1]

