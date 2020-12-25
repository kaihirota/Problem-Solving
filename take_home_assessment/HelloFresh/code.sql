-- a. Total number of boxes shipped to 'Offline' customers in week 2019-W10
WITH customers AS (
    SELECT sk_customer
    FROM customer_dimension
    WHERE acquisition_channel = 'Offline'
),
shipment AS (
    SELECT box_id, fk_customer
    FROM boxes_shipped
    WHERE week = '2019-W10'
)
SELECT COUNT(DISTINCT box_id) AS box_count_2019W10
FROM shipment
JOIN customers ON customers.sk_customer = shipment.fk_customer

-- b. Total box value (gross revenue) shipped to WA in 2019
WITH date_filter AS (
    SELECT *
    FROM date_dimension
    WHERE Year = 2019
),
shipment AS (
    SELECT box_id, fk_box_sku
    FROM boxes_shipped
    JOIN date_filter ON date_filter.sk_date = shipment.delivery_date
)
SELECT SUM(box_dimension.box_price) AS gross_revenue_WA_2019
FROM shipment
JOIN box_dimension ON box_dimension.sk_box_sku = shipment.fk_box_sku

-- c. The actual box count for every customer since 2019-W01
WITH date_filter AS (
    SELECT *
    FROM date_dimension
    WHERE year >= 2019
),
customer AS (
    SELECT sk_customer, customer_id
    FROM customer_dimension
    JOIN date_filter ON date_filter.sk_date = customer_dimension.acquisition_date
)
SELECT customer.sk_customer
    , COUNT(DISTINCT boxes_shipped.box_id) AS cumsum_boxcount_since2019
FROM boxes_shipped
JOIN customer ON customer.sk_customer = boxes_shipped.fk_customer
GROUP BY 1
ORDER BY 2 DESC

-- d. The number of boxes sold and the gross revenue for every month since 2019
WITH date_filter AS (
    SELECT *
    FROM date_dimension
    WHERE year >= 2019
),
shipment AS (
    SELECT box_id, fk_box_sku
        , date_filter.Month AS delivery_month
        , box_dimension.box_price
    FROM boxes_shipped
    JOIN date_filter ON date_filter.sk_date = shipment.delivery_date
    JOIN box_dimension ON box_dimension.sk_box_sku = shipment.fk_box_sku
),
SELECT shipment.delivery_month
    , COUNT(DISTINCT shipment.box_id) AS boxes_sold
    , SUM(shipment.box_price) AS gross_revenue
FROM shipment
GROUP BY 1
ORDER BY 1

-- e. The number of new customers since 2019-W01 for each week
WITH date_filter AS (
    SELECT sk_date, Week
    FROM date_dimension
    WHERE year >= 2019
),
customer AS (
    SELECT customer_dimension.sk_customer
        , customer_dimension.customer_id
        , date_filter.Week AS acquisition_week
    FROM customer_dimension
    JOIN date_filter ON date_filter.sk_date = customer_dimension.acquisition_date
)
SELECT customer.acquisition_week
    , COUNT(DISTINCT customer.sk_customer) AS user_acquisition
FROM customer
GROUP BY 1

-- f. The box count for every customer at every week the customer ordered
SELECT fk_customer, week, COUNT(DISTINCT box_id) AS box_count
FROM boxes_shipped
GROUP BY 1, 2
ORDER BY 1, 2
