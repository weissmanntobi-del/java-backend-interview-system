\set ON_ERROR_STOP on

EXPLAIN (ANALYZE, BUFFERS)
SELECT id, customer_id, status, total_amount, created_at
FROM sample_orders
WHERE status = 'PAID'
ORDER BY created_at DESC, id DESC
LIMIT 50 OFFSET 100000;
