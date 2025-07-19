# 🚚 Delivery Time Optimization Dashboard

This dashboard helps analyze delivery efficiency and delays using synthetic data. It uses **free mapping tools (folium + OpenStreetMap)** — no API key needed.

---

## 🔧 Features

- 📊 KPIs: Average delivery time, delayed orders
- 📍 Interactive bar chart by destination
- ⏱️ Histogram of delivery durations
- 🗺️ Free route map using Folium (OpenStreetMap)
- 📄 Sample data view

---

## 📁 Project Structure

delivery-time-optimization/
├── .streamlit/
├── data/
├── src/
└── requirements.txt


---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/2003UJAN/Delivery-Time-Optimization-Dashboard.git
cd delivery-time-optimization

### 2. Install Dependencies

pip install -r requirements.txt

### 3. Generate Data

python src/data_generator.py

### 4. Run the Dashboard

streamlit run src/dashboard.py
