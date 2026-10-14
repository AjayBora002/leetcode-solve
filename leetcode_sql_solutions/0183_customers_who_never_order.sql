/*
LeetCode 183. Customers Who Never Order
Difficulty: Easy

QUESTION:
  Find all customers who never placed an order. Output column: Customers.

TABLES:
  Customers(id, name)
  Orders(id, customerId)
*/

-- MySQL Solution
SELECT c.name AS Customers
FROM Customers c
LEFT JOIN Orders o ON o.customerId = c.id
WHERE o.id IS NULL;
