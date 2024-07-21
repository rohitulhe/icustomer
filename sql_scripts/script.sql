-- Total Number of Interactions

SELECT
    DATE(timestamp) AS interaction_date,
    COUNT(*) AS total_interactions
FROM
    interactions
GROUP BY
    DATE(timestamp)
ORDER BY
    interaction_date;


-- Top 5 Users

SELECT
    user_id,
    COUNT(*) AS total_interactions
FROM
    interactions
GROUP BY
    user_id
ORDER BY
    total_interactions DESC
LIMIT 5;


-- Most Interacted Products
SELECT
    product_id,
    COUNT(*) AS total_interactions
FROM
    interactions
GROUP BY
    product_id
ORDER BY
    total_interactions DESC;

