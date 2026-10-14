/*
LeetCode 184. Department Highest Salary
Difficulty: Medium

QUESTION:
  Find the employees who have the highest salary in each department. Output: Department,
  Employee, Salary. Include all employees tied for the top salary.

TABLES:
  Employee(id, name, salary, departmentId)
  Department(id, name)
*/

-- MySQL Solution
SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Employee e
JOIN Department d ON e.departmentId = d.id
WHERE (e.departmentId, e.salary) IN (
    SELECT departmentId, MAX(salary)
    FROM Employee
    GROUP BY departmentId
);
