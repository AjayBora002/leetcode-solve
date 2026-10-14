/*
LeetCode 180. Consecutive Numbers
Difficulty: Medium

QUESTION:
  Find all numbers that appear at least three times consecutively in the Logs table (by id).

TABLES:
  Logs(id, num)
*/

-- MySQL Solution
SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1
JOIN Logs l2 ON l2.id = l1.id + 1 AND l2.num = l1.num
JOIN Logs l3 ON l3.id = l1.id + 2 AND l3.num = l1.num;
