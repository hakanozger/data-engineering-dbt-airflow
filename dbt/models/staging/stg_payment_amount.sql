WITH raw_data AS (
    SELECT 
           customers.customer_id AS customer_id, 
           payments.amount as payment_amount
    FROM customers
    INNER JOIN subscriptions ON customers.customer_id=subscriptions.customer_id
    INNER JOIN payments ON subscriptions.subscription_id =payments.subscription_id 
)
SELECT 
    customer_id, 
    payment_amount
FROM raw_data