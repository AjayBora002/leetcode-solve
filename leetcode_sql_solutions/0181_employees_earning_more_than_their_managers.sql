/*
LeetCode 181. Employees Earning More Than Their Managers
Difficulty: Easy

QUESTION:
  Find the employees who earn more than their managers. Output column: Employee.

TABLES:
  Employee(id, name, salary, managerId)
*/

-- MySQL Solution
SELECT e.name AS Employee
FROM Employee e
JOIN Employee m ON e.managerId = m.id
WHERE e.salary > m.salary;
