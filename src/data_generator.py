import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_synthetic_data(n=500):
    locations = {
        'Andheri': 'Andheri West, Mumbai',
        'Bandra': 'Bandra West, Mumbai',
        'Borivali': 'Borivali East, Mumbai',
        'Dadar': 'Dadar, Mumbai',
        'Juhu': 'Juhu, Mumbai',
        'Powai': 'Powai, Mumbai',
        'Thane': 'Thane West, Mumbai',
        'Versova': 'Versova, Mumbai'
    }

    data = []

    for _ in range(n):
        origin = random.choice(list(locations.keys()))
        destination = random.choice(list(locations.keys()))
        while destination == origin:
            destination = random.choice(list(locations.keys()))

        order_time = datetime.now() - timedelta(minutes=random.randint(5, 120))
        delivery_time = order_time + timedelta(minutes=random.randint(7, 25))

        data.append({
            "order_id": f"OID{random.randint(1000, 9999)}",
            "origin": locations[origin],
            "destination": locations[destination],
            "order_time": order_time,
            "delivery_time": delivery_time,
            "distance_km": round(random.uniform(1, 7), 2)
        })

    df = pd.DataFrame(data)
    df["delivery_duration_min"] = (df["delivery_time"] - df["order_time"]).dt.total_seconds() / 60
    df.to_csv("data/synthetic_delivery_data.csv", index=False)
    print("✅ Synthetic delivery data generated!")

if __name__ == "__main__":
    generate_synthetic_data()
