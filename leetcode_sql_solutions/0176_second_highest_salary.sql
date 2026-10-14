/*
LeetCode 176. Second Highest Salary
Difficulty: Medium

QUESTION:
  Return the second highest DISTINCT salary as SecondHighestSalary. If there is no second
  highest salary, return null.

TABLES:
  Employee(id, salary)
*/

-- MySQL Solution
SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary;
