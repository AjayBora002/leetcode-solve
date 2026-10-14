/*
LeetCode 596. Classes With at Least 5 Students
Difficulty: Easy

QUESTION:
  Find all classes that have at least five students.

TABLES:
  Courses(student, class)
*/

-- MySQL Solution
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(DISTINCT student) >= 5;
