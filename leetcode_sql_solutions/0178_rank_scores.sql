/*
LeetCode 178. Rank Scores
Difficulty: Medium

QUESTION:
  Rank the scores from highest to lowest. Ties share the same rank, and the next rank is the
  next consecutive integer (no gaps = dense rank).

TABLES:
  Scores(id, score)
*/

-- MySQL Solution
SELECT score,
       DENSE_RANK() OVER (ORDER BY score DESC) AS `rank`
FROM Scores;
