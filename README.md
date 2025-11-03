# 🏨 Hotel Booking & Cancellation Analysis

## 📖 Overview
This project explores hotel booking data to analyze **cancellation patterns**, understand **customer behavior**, and identify **factors influencing cancellations**.  
It combines **SQL** for data cleaning and aggregation with **Python** for exploratory data analysis (EDA) and visualization.

The goal is to help hotels **reduce cancellation rates**, **improve revenue forecasting**, and **optimize booking strategies**.

---

## 📂 Dataset Description
The dataset contains booking information for city and resort hotels.  
Each record represents a single booking and includes details about the customer, booking duration, and cancellation status.

| Column Name | Description |
|--------------|-------------|
| `hotel` | Type of hotel (City Hotel or Resort Hotel) |
| `is_canceled` | 1 if the booking was canceled, 0 otherwise |
| `lead_time` | Number of days between booking and arrival |
| `arrival_date_month` | Month of arrival |
| `stays_in_weekend_nights` | Number of weekend nights booked |
| `stays_in_week_nights` | Number of weekday nights booked |
| `adults` | Number of adults |
| `children` | Number of children |
| `meal` | Type of meal plan |
| `country` | Country of origin |
| `market_segment` | Booking channel (e.g., Online TA, Corporate) |
| `deposit_type` | Type of deposit made (No Deposit, Non Refund, Refundable) |
| `adr` | Average Daily Rate (price per night) |
| `customer_type` | Type of customer (Transient, Contract, etc.) |
| `reservation_status_date` | Date the booking was completed or canceled |

---

## 🧹 SQL Data Cleaning & Preparation

SQL scripts were used for:
- Removing duplicates and invalid records
- Handling missing values (e.g., `adr`, `children`)
- Converting columns to the correct data types
- Calculating total stay duration (`total_nights`)
- Aggregating cancellation rates by month, hotel type, and deposit type

📁 **SQL Files:**
- `schema.sql` – Table creation  
- `data_cleaning.sql` – Data preprocessing  
- `data_exploration.sql` – Basic analysis queries  
- `advanced_analysis.sql` – Deep insights and ranking

---

## 🐍 Python Exploratory Data Analysis (EDA)

Python was used to visualize and interpret trends from the cleaned dataset.

### Key Steps:
1. **Data Cleaning:**
   - Filled missing values  
   - Removed zero-night bookings  
   - Added derived features (`total_nights`, `lead_bucket`)
2. **Exploratory Analysis:**
   - Overall and segmented cancellation rates  
   - ADR distribution  
   - Top countries by cancellations  
3. **Visualization:**
   - Seaborn and Matplotlib for static analysis

---

## 📊 Visualizations

| Visualization | Description |
|----------------|-------------|
| Cancellation Rate by Hotel Type | Compare city vs resort hotels |
![alt text](<لقطة شاشة 2025-11-03 150321.png>)
| Cancellation Rate by Month | Identify seasonal trends |
![alt text](<لقطة شاشة 2025-11-03 150337.png>)
| Cancellation Rate by Deposit Type | Understand payment effects |
![alt text](<لقطة شاشة 2025-11-03 150345.png>)
| Cancellation Rate by Lead Time | See how early bookings affect cancellations |
![alt text](<لقطة شاشة 2025-11-03 150353.png>)
| ADR Distribution | Explore price variations |
![alt text](<لقطة شاشة 2025-11-03 150403.png>)
| ADR by Cancellation Status | Compare average rates between canceled and non-canceled bookings |
![alt text](<لقطة شاشة 2025-11-03 150411.png>)
| Top 10 Countries | Show countries with most bookings and cancellations |
![alt text](<لقطة شاشة 2025-11-03 150422.png>)
---

## 🧠 Insights

- **City hotels** tend to have a **higher cancellation rate** than resort hotels.  
- **Bookings made far in advance (high lead time)** are more likely to be canceled.  
- **Non-refundable deposits** have **lower cancellation rates**, indicating payment policies influence customer behavior.  
- **Certain months** show peak cancellations — possibly due to seasonal travel patterns.  
- **Higher ADRs (prices)** correlate slightly with higher cancellation likelihood.

---

## ⚙️ How to Run the Project

### 1️⃣ Prerequisites
- Python 3.8+
- Libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`
- SQL Database if running SQL scripts

### 2️⃣ Run Python Analysis
```bash
pip install pandas numpy matplotlib seaborn
python hotel_analysis.py
