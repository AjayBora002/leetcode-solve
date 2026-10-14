/*
LeetCode 182. Duplicate Emails
Difficulty: Easy

QUESTION:
  Report all duplicate emails in the Person table (emails are never null). Output column:
  Email.

TABLES:
  Person(id, email)
*/

-- MySQL Solution
SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;
