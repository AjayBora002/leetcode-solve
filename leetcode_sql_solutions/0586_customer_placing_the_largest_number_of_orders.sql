/*
LeetCode 586. Customer Placing the Largest Number of Orders
Difficulty: Easy

QUESTION:
  Find the customer_number for the customer who has placed the largest number of orders.

TABLES:
  Orders(order_number, customer_number)
*/

-- MySQL Solution
SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;
