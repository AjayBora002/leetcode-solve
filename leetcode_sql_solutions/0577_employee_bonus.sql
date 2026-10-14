/*
LeetCode 577. Employee Bonus
Difficulty: Easy

QUESTION:
  Report the name and bonus amount of each employee with a bonus less than 1000 (include
  employees with no bonus, i.e. null).

TABLES:
  Employee(empId, name, supervisor, salary)
  Bonus(empId, bonus)
*/

-- MySQL Solution
SELECT e.name, b.bonus
FROM Employee e
LEFT JOIN Bonus b ON e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL;
