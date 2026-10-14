/*
LeetCode 177. Nth Highest Salary
Difficulty: Medium

QUESTION:
  Write a function getNthHighestSalary(N) that returns the Nth highest DISTINCT salary from
  Employee. If there is no Nth highest salary, return null.

TABLES:
  Employee(id, salary)
*/

-- MySQL Solution
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N = N - 1;
    RETURN (
        SELECT DISTINCT salary
        FROM Employee
        ORDER BY salary DESC
        LIMIT 1 OFFSET N
    );
END
