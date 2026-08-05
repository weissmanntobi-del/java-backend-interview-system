\set ON_ERROR_STOP on

DROP TABLE IF EXISTS sample_orders;

CREATE TABLE sample_orders (
    id BIGSERIAL PRIMARY KEY,
    customer_id BIGINT NOT NULL,
    status VARCHAR(30) NOT NULL,
    total_amount NUMERIC(12, 2) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL
);

INSERT INTO sample_orders(customer_id, status, total_amount, created_at)
SELECT
    1 + (g % 500),
    CASE WHEN g % 7 = 0 THEN 'REVIEW_REQUIRED' ELSE 'PAID' END,
    round((20 + random() * 500)::numeric, 2),
    now() - ((g % 129600) || ' minutes')::interval
FROM generate_series(1, 200000) AS g;

CREATE INDEX idx_sample_orders_status_created_id
ON sample_orders(status, created_at DESC, id DESC);

ANALYZE sample_orders;
