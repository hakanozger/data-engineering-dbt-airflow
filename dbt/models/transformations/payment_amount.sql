WITH staged AS (
    SELECT * FROM {{ ref('stg_payment_amount') }}
)
SELECT 
    customer_id, 
    SUM(payment_amount) AS total_payment_amount
FROM staged
GROUP BY customer_id