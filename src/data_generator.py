# src/data_generator.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

def generate_synthetic_data(n=500):
    locations = ['Mumbai', 'Delhi', 'Bengaluru', 'Hyderabad', 'Pune']
    data = []

    for _ in range(n):
        location = random.choice(locations)
        start_time = datetime.now() - timedelta(days=random.randint(1, 10), hours=random.randint(0, 23))
        duration_minutes = random.randint(5, 45)
        end_time = start_time + timedelta(minutes=duration_minutes)
        delay = random.choices([0, 1], weights=[0.8, 0.2])[0]  # 20% chance of delay

        data.append({
            'location': location,
            'start_time': start_time,
            'end_time': end_time,
            'delay': delay
        })

    df = pd.DataFrame(data)
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/delivery_data.csv", index=False)

if __name__ == "__main__":
    generate_synthetic_data()
