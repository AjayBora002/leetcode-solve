/*
LeetCode 584. Find Customer Referee
Difficulty: Easy

QUESTION:
  Find the names of the customers that are NOT referred by the customer with id = 2
  (referee_id can be null).

TABLES:
  Customer(id, name, referee_id)
*/

-- MySQL Solution
SELECT name
FROM Customer
WHERE referee_id IS NULL OR referee_id <> 2;
