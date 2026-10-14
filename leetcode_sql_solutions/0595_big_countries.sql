/*
LeetCode 595. Big Countries
Difficulty: Easy

QUESTION:
  A country is big if its area is at least 3,000,000 km2 OR its population is at least
  25,000,000. Report name, population and area of big countries.

TABLES:
  World(name, continent, area, population, gdp)
*/

-- MySQL Solution
SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000;
