/*
LeetCode 511. Game Play Analysis I
Difficulty: Easy

QUESTION:
  Write a query to report the first login date for each player.

TABLES:
  Activity(player_id, device_id, event_date, games_played)
*/

-- MySQL Solution
SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;
