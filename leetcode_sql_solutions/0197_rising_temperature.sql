/*
LeetCode 197. Rising Temperature
Difficulty: Easy

QUESTION:
  Find the ids of all dates where the temperature was higher than the previous day
  (yesterday).

TABLES:
  Weather(id, recordDate, temperature)
*/

-- MySQL Solution
SELECT w1.id
FROM Weather w1
JOIN Weather w2 ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature > w2.temperature;
