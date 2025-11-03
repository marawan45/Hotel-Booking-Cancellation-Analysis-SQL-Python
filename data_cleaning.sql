-- تنظيف أولي للبيانات قبل التحليل

-- 1) توحيد نصوص ببعض الأعمدة
UPDATE hotel_bookings
SET hotel = INITCAP(TRIM(hotel)),
    meal = UPPER(TRIM(meal)),
    deposit_type = INITCAP(TRIM(deposit_type)),
    market_segment = INITCAP(TRIM(market_segment)),
    customer_type = INITCAP(TRIM(customer_type));

-- 2) تحويل قيم ناقصة أو نصية في adr أو children
-- لو ADR محفوظ كنص أو فاضي، حوّله للقيمة NULL أولا (مثال)
UPDATE hotel_bookings
SET adr = NULL
WHERE COALESCE(adr::text, '') = '';

-- 3) حذف الحجز اللي مفيهوش ليلتين (total_nights = 0) لأن ممكن يكون خطأ
DELETE FROM hotel_bookings
WHERE total_nights <= 0 OR total_nights IS NULL;

-- 4) حذف السجلات اللي فيها عدد بالغين أو أطفال سلبي
DELETE FROM hotel_bookings
WHERE adults < 0 OR children < 0;

-- 5) إزالة السجلات المكررة اعتمادًا على كل الحقول الأساسية
DELETE FROM hotel_bookings a
USING hotel_bookings b
WHERE a.ctid < b.ctid
  AND a.hotel = b.hotel
  AND a.arrival_date = b.arrival_date
  AND a.adults = b.adults
  AND a.children = b.children
  AND a.adr = b.adr;
