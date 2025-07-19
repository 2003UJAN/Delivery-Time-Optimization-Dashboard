import pandas as pd

def load_data(path="data/synthetic_delivery_data.csv"):
    return pd.read_csv(path, parse_dates=["order_time", "delivery_time"])

def get_avg_delivery_time(df):
    return df["delivery_duration_min"].mean()

def get_volume_by_location(df):
    return df["location"].value_counts().reset_index().rename(columns={"index": "Location", "location": "Order Volume"})

def get_delay_alerts(df, threshold=10):
    return df[df["delivery_duration_min"] > threshold]

