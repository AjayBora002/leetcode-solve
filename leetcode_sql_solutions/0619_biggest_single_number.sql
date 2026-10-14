/*
LeetCode 619. Biggest Single Number
Difficulty: Easy

QUESTION:
  A single number appears only once in MyNumbers. Report the largest single number, or null
  if there is none.

TABLES:
  MyNumbers(num)
*/

-- MySQL Solution
SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) t;
