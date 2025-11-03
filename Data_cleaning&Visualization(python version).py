


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette('viridis')


# لو عندك ملف hotel_bookings.csv على جهازك غير المسار ده حسب مكانه
df = pd.read_csv("hotel_bookings.csv")

# نبص على أول كام صف
print(" أول 5 صفوف من الداتا:")
print(df.head())


# نطبع شكل البيانات وعدد القيم الفاضية
print("\n شكل الداتا وعدد القيم الفاضية:")
print(df.info())
print(df.isnull().sum())

# نحول الأعمدة الرقمية اللي ممكن فيها نصوص
df['children'] = pd.to_numeric(df['children'], errors='coerce')
df['adr'] = pd.to_numeric(df['adr'], errors='coerce')

# نملأ القيم الفاضية
df['children'].fillna(0, inplace=True)
df['adr'].fillna(df['adr'].median(), inplace=True)

# نضيف عمود total_nights (مجموع الليالي)
df['total_nights'] = df['stays_in_weekend_nights'] + df['stays_in_week_nights']

# نشيل الحجوزات اللي عدد الليالي فيها 0 أو أقل
df = df[df['total_nights'] > 0]

# نحول بعض الأعمدة لتاريخ
date_cols = ['reservation_status_date']
for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors='coerce')

# نطبع شكل الداتا بعد التنظيف
print("\n بعد التنظيف:")
print(df.info())


#  تحليل استكشافي (EDA)


# معدل الإلغاء العام
cancel_rate = df['is_canceled'].mean() * 100
print(f"\n نسبة الإلغاءات العامة: {cancel_rate:.2f}%")

# معدل الإلغاء حسب نوع الفندق
cancel_by_hotel = df.groupby('hotel')['is_canceled'].mean().reset_index()
cancel_by_hotel['is_canceled'] *= 100

# معدل الإلغاء حسب الشهر
cancel_by_month = df.groupby('arrival_date_month')['is_canceled'].mean().reset_index()
cancel_by_month['is_canceled'] *= 100

# معدل الإلغاء حسب نوع الإيداع
cancel_by_deposit = df.groupby('deposit_type')['is_canceled'].mean().reset_index()
cancel_by_deposit['is_canceled'] *= 100




# تقسيم lead_time لفئات (bins)
bins = [0, 7, 30, 90, 180, 365, df['lead_time'].max()]
labels = ['0-6', '7-30', '31-90', '91-180', '181-365', '365+']
df['lead_bucket'] = pd.cut(df['lead_time'], bins=bins, labels=labels, include_lowest=True)

lead_time_analysis = df.groupby('lead_bucket')['is_canceled'].mean().reset_index()
lead_time_analysis['is_canceled'] *= 100

# معدل الإلغاء حسب الدولة
top_countries = (
    df.groupby('country')['is_canceled']
    .agg(['count', 'mean'])
    .reset_index()
    .sort_values(by='count', ascending=False)
    .head(10)
)
top_countries['mean'] *= 100


plt.figure(figsize=(12,6))
sns.barplot(x='hotel', y='is_canceled', data=cancel_by_hotel)
plt.title('Cancellation Rate by Hotel Type', fontsize=14)
plt.ylabel('Cancellation Rate (%)')
plt.xlabel('Hotel Type')
plt.show()

plt.figure(figsize=(12,6))
sns.barplot(x='arrival_date_month', y='is_canceled', data=cancel_by_month)
plt.title('Cancellation Rate by Month', fontsize=14)
plt.ylabel('Cancellation Rate (%)')
plt.xlabel('Month')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10,5))
sns.barplot(x='deposit_type', y='is_canceled', data=cancel_by_deposit)
plt.title('Cancellation Rate by Deposit Type', fontsize=14)
plt.ylabel('Cancellation Rate (%)')
plt.xlabel('Deposit Type')
plt.show()

plt.figure(figsize=(10,5))
sns.lineplot(x='lead_bucket', y='is_canceled', data=lead_time_analysis, marker='o')
plt.title('Cancellation Rate by Lead Time Bucket', fontsize=14)
plt.ylabel('Cancellation Rate (%)')
plt.xlabel('Lead Time (Days)')
plt.show()

plt.figure(figsize=(12,6))
sns.histplot(df['adr'], bins=40, kde=True)
plt.title('Distribution of Average Daily Rate (ADR)', fontsize=14)
plt.xlabel('ADR')
plt.ylabel('Number of Bookings')
plt.show()

plt.figure(figsize=(10,5))
sns.barplot(x='is_canceled', y='adr', data=df)
plt.title('Average ADR for Canceled vs Non-Canceled Bookings', fontsize=14)
plt.ylabel('ADR')
plt.xlabel('Is Canceled (0=No, 1=Yes)')
plt.show()

plt.figure(figsize=(12,6))
sns.barplot(x='country', y='mean', data=top_countries)
plt.title('Top 10 Countries by Number of Bookings and Cancellation Rate', fontsize=14)
plt.ylabel('Cancellation Rate (%)')
plt.xlabel('Country')
plt.xticks(rotation=45)
plt.show()





df.to_csv("hotel_bookings_cleaned.csv", index=False)
print("\n تم حفظ نسخة من الداتا بعد التنظيف في ملف hotel_bookings_cleaned.csv")
