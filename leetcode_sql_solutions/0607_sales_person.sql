/*
LeetCode 607. Sales Person
Difficulty: Easy

QUESTION:
  Find the names of all salespersons who did NOT have any orders related to the company
  named 'RED'.

TABLES:
  SalesPerson(sales_id, name, salary, commission_rate, hire_date)
  Company(com_id, name, city)
  Orders(order_id, order_date, com_id, sales_id, amount)
*/

-- MySQL Solution
SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT o.sales_id
    FROM Orders o
    JOIN Company c ON o.com_id = c.com_id
    WHERE c.name = 'RED'
);
