# 🚚 Delivery IQ – Food Delivery Analytics System

🚀 An end-to-end data analytics project focused on analyzing food delivery performance, identifying delays, and uncovering operational insights using data.

---

## 🔥 Live Demo
🌐 Streamlit App: *https://delivery-iq-059.streamlit.app/*
📁 Power BI Dashboard: Available in `/dashboard/powerbi.pbix`

---

## 📌 Project Overview

This project analyzes food delivery data to understand:

- ⏱ Delivery performance and delays  
- 🚗 Impact of traffic and weather  
- 🕒 Time-based delivery patterns  
- 🚴 Efficiency across vehicle types  

It demonstrates a complete analytics workflow from **raw data → feature engineering → insights → dashboards**.

---

## 🛠️ Tech Stack

- **Python** (Pandas, NumPy)  
- **Streamlit** (Web App)  
- **Power BI** (Dashboarding – Analysis in progress)  
- **Plotly & Matplotlib** (Visualization)  

---

## 📂 Project Structure

```

Food-Delivery-Analytics-System/
┣ data/
┃ ┣ food_delivery_times.csv
┃ ┗ cleaned_data.csv
┣ notebooks/
┃ ┣ data_cleaning.ipynb
┃ ┣ feature_engineering.ipynb
┃ ┗ eda_analysis.ipynb
┣ app/
┃ ┣ app.py
┃ ┣ utils.py
┃ ┗ config.py
┣ dashboard/
┃ ┗ powerbi.pbix
┣ images/
┃ ┣ kpi_cards.png
┃ ┣ delay_trend.png
┃ ┣ rider_performance.png
┃ ┗ dashboard_preview.png
┣ requirements.txt
┗ README.md

```

---

## ⚙️ Data Pipeline

1. **Data Cleaning**
   - Removed missing values  
   - Handled duplicates  
   - Ensured correct data types  

2. **Feature Engineering**
   - Created `delay_flag` (late vs on-time deliveries)  
   - Generated `distance_category` (Short / Medium / Long)  
   - Computed efficiency metrics (time per km)  

3. **Final Dataset**
   - Saved as `cleaned_data.csv`  
   - Used across Streamlit & Power BI  

---

## 📊 Analysis Highlights

- 📈 Delivery time increases significantly with higher traffic levels  
- ⚠️ Peak time periods show higher delay rates  
- 🚗 Distance plays a major role in delivery delays  
- 🚴 Vehicle type impacts delivery efficiency  

---

## 📊 Power BI Dashboard

Planned features:

- KPI Cards (Total Orders, Avg Delivery Time, % Delayed)  
- Delay Analysis by Time of Day  
- Traffic & Distance Impact  
- Vehicle Performance Insights  
- Interactive Filters (Time, Traffic, Vehicle Type)  

---

## 🌐 Streamlit Web App

### Features:
- Interactive filters (Time of Day, Traffic Level, Vehicle Type)  
- Dynamic KPI metrics  
- Delivery time vs distance visualization  
- Delay trend analysis  
- Traffic and vehicle performance insights  

### Run Locally:

```bash
pip install -r requirements.txt
streamlit run app/app.py
```

---

## 💡 Key Insights

- High traffic conditions significantly increase delivery time  
- Orders during peak hours show higher delay percentages  
- Longer distances lead to increased delivery delays  
- Vehicle choice impacts overall delivery efficiency  

---

## 🧠 Skills Demonstrated

- Data Cleaning & Preprocessing  
- Feature Engineering  
- Exploratory Data Analysis (EDA)  
- Data Visualization  
- Dashboard Design  
- Web App Deployment  
- Business Insight Generation  

---

## 👤 Author

**Rajarshi Saha**