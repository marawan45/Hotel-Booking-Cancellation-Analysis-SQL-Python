-- تحليلات متقدمة: lead time, deposit type, segmentation و ranking

-- 1) توزيع معدل الإلغاء حسب deposit_type
SELECT deposit_type,
       COUNT(*) AS total,
       SUM(is_canceled) AS cancellations,
       ROUND(100.0 * SUM(is_canceled)::numeric / COUNT(*), 2) AS cancel_rate_pct
FROM hotel_bookings
GROUP BY deposit_type
ORDER BY cancel_rate_pct DESC;

-- 2) تجزئة lead_time (باكت) ومعدل الإلغاء
WITH buckets AS (
  SELECT *,
    CASE
      WHEN lead_time < 7 THEN '0-6'
      WHEN lead_time BETWEEN 7 AND 30 THEN '7-30'
      WHEN lead_time BETWEEN 31 AND 90 THEN '31-90'
      WHEN lead_time BETWEEN 91 AND 180 THEN '91-180'
      ELSE '181+'
    END AS lead_bucket
  FROM hotel_bookings
)
SELECT lead_bucket,
       COUNT(*) AS total,
       SUM(is_canceled) AS cancellations,
       ROUND(100.0 * SUM(is_canceled)::numeric / COUNT(*), 2) AS cancel_rate_pct
FROM buckets
GROUP BY lead_bucket
ORDER BY array_position(ARRAY['0-6','7-30','31-90','91-180','181+'], lead_bucket);

-- 3) أعلى 10 دول فيها حجز وعدد الإلغاءات
SELECT country,
       COUNT(*) AS total_bookings,
       SUM(is_canceled) AS cancellations,
       ROUND(100.0 * SUM(is_canceled)::numeric / COUNT(*), 2) AS cancel_rate_pct
FROM hotel_bookings
GROUP BY country
ORDER BY total_bookings DESC
LIMIT 10;

-- 4) Rank hotels by average ADR and cancellation rate together (composite score)
WITH agg AS (
  SELECT hotel,
         AVG(adr) AS avg_adr,
         ROUND(100.0 * SUM(is_canceled)::numeric / COUNT(*), 2) AS cancel_rate_pct
  FROM hotel_bookings
  GROUP BY hotel
)
SELECT hotel, avg_adr, cancel_rate_pct,
       RANK() OVER (ORDER BY (avg_adr - cancel_rate_pct) DESC) AS performance_rank
FROM agg
ORDER BY performance_rank
LIMIT 50;
