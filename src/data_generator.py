import pandas as pd
import random
from datetime import datetime, timedelta

def generate_data(n=500):
    locations = ['Connaught Place, Delhi', 'Andheri West, Mumbai', 'BTM Layout, Bangalore',
                 'Salt Lake, Kolkata', 'Gachibowli, Hyderabad', 'Baner, Pune', 'Sector 18, Noida']

    data = []
    for _ in range(n):
        origin = random.choice(locations)
        destination = random.choice([loc for loc in locations if loc != origin])
        start_time = datetime.now() - timedelta(minutes=random.randint(0, 1440))
        delivery_duration = random.randint(5, 25)  # in minutes
        end_time = start_time + timedelta(minutes=delivery_duration)
        data.append({
            "origin": origin,
            "destination": destination,
            "start_time": start_time,
            "end_time": end_time,
            "delivery_duration_min": delivery_duration
        })

    df = pd.DataFrame(data)
    df.to_csv("data/delivery_data.csv", index=False)

if __name__ == "__main__":
    generate_data()
