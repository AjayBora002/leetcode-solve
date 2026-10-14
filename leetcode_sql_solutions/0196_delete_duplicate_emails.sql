/*
LeetCode 196. Delete Duplicate Emails
Difficulty: Easy

QUESTION:
  Delete all duplicate emails from Person, keeping only the row with the smallest id for
  each email. (Write a DELETE statement, not a SELECT.)

TABLES:
  Person(id, email)
*/

-- MySQL Solution
DELETE p1
FROM Person p1
JOIN Person p2
  ON p1.email = p2.email AND p1.id > p2.id;
