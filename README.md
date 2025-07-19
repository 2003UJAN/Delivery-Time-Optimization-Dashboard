# 🚀 Delivery Time Optimization Dashboard

This dashboard helps visualize delivery performance for Blinkit using synthetic data.

## Features

- Track average delivery time
- View order volume by location
- Identify delayed deliveries
- Optional: Google Maps API integration

## Run it

```bash
pip install -r requirements.txt
python src/data_generator.py
streamlit run src/dashboard.py


---

### 🛰️ Google Maps API (Optional Setup)

1. Go to: https://console.cloud.google.com/
2. Enable **Distance Matrix API**
3. Generate API key
4. Use `maps_utils.py` in future extensions to compare **estimated** vs **actual delivery**.

---

### 🧪 Live Demo Option (Streamlit Cloud)

- Push repo to GitHub
- Create a Streamlit Cloud app with:streamlit run src/dashboard.py
