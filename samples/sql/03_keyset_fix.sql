\set ON_ERROR_STOP on

-- First page.
SELECT id, customer_id, status, total_amount, created_at
FROM sample_orders
WHERE status = 'PAID'
ORDER BY created_at DESC, id DESC
LIMIT 50;

-- Demonstration cursor. In an application, use the created_at and id values
-- from the final row of the previous page.
WITH cursor_row AS (
    SELECT created_at, id
    FROM sample_orders
    WHERE status = 'PAID'
    ORDER BY created_at DESC, id DESC
    OFFSET 49
    LIMIT 1
)
EXPLAIN (ANALYZE, BUFFERS)
SELECT o.id, o.customer_id, o.status, o.total_amount, o.created_at
FROM sample_orders AS o
CROSS JOIN cursor_row AS cursor
WHERE o.status = 'PAID'
  AND (o.created_at, o.id) < (cursor.created_at, cursor.id)
ORDER BY o.created_at DESC, o.id DESC
LIMIT 50;
