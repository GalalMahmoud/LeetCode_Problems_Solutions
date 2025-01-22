-- PostgreSQL query
WITH CTE AS (
    SELECT num, COUNT(*) as num_quantity
    FROM MyNumbers
    GROUP BY num
)

SELECT MAX(num) as num
FROM CTE
WHERE num_quantity = 1;