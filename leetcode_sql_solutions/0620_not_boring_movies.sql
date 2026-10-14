/*
LeetCode 620. Not Boring Movies
Difficulty: Easy

QUESTION:
  Report movies with an odd-numbered id and a description that is not 'boring'. Order by
  rating descending.

TABLES:
  Cinema(id, movie, description, rating)
*/

-- MySQL Solution
SELECT *
FROM Cinema
WHERE id % 2 = 1 AND description <> 'boring'
ORDER BY rating DESC;
