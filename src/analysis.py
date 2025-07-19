import pandas as pd

def load_data():
    return pd.read_csv("data/delivery_data.csv", parse_dates=["start_time", "end_time"])

def get_avg_delivery_time(df):
    return df["delivery_duration_min"].mean()

def get_volume_by_location(df):
    return df["destination"].value_counts().reset_index().rename(columns={"index": "Location", "destination": "Order Volume"})

def get_delay_alerts(df, threshold=10):
    return df[df["delivery_duration_min"] > threshold]
