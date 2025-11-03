-- تحليل استكشافي بسيط

-- 1) إجمالي الحجوزات ونسبة الإلغاءات
SELECT
  COUNT(*) AS total_bookings,
  SUM(is_canceled) AS total_cancellations,
  ROUND(100.0 * SUM(is_canceled)::numeric / COUNT(*), 2) AS cancellation_rate_pct
FROM hotel_bookings;

-- 2) معدل الإلغاء حسب نوع الفندق
SELECT hotel,
       COUNT(*) AS total,
       SUM(is_canceled) AS cancellations,
       ROUND(100.0 * SUM(is_canceled)::numeric / COUNT(*), 2) AS cancel_rate_pct
FROM hotel_bookings
GROUP BY hotel
ORDER BY cancel_rate_pct DESC;

-- 3) معدل الإلغاء حسب الشهر
SELECT arrival_date_month,
       COUNT(*) AS total,
       SUM(is_canceled) AS cancellations,
       ROUND(100.0 * SUM(is_canceled)::numeric / COUNT(*), 2) AS cancel_rate_pct
FROM hotel_bookings
GROUP BY arrival_date_month
ORDER BY DATE_PART('month', TO_DATE(arrival_date_month, 'Month'));

-- 4) متوسط ADR للحجوزات الملغاة وغير الملغاة
SELECT is_canceled, COUNT(*) AS n, ROUND(AVG(adr),2) AS avg_adr
FROM hotel_bookings
GROUP BY is_canceled;
