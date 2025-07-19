import pandas as pd
import os

def load_data(path="data/synthetic_delivery_data.csv"):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Dataset not found at {path}. Please run data_generator.py first.")
    return pd.read_csv(path, parse_dates=["order_time", "delivery_time"])

def get_avg_delivery_time(df):
    return df["delivery_duration_min"].mean()

def get_volume_by_location(df):
    return df["destination"].value_counts().reset_index().rename(columns={"index": "Location", "destination": "Order Volume"})

def get_delay_alerts(df, threshold=10):
    return df[df["delivery_duration_min"] > threshold]
