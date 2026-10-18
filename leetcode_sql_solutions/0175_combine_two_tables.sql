/*
LeetCode 175. Combine Two Tables


QUESTION:
  Report the firstName, lastName, city and state of each person in Person. If a person has
  no address, report null for city and state.

TABLES:
  Person(personId, lastName, firstName)
  Address(addressId, personId, city, state)
*/

-- MySQL Solution
SELECT p.firstName, p.lastName, a.city, a.state
FROM Person p
LEFT JOIN Address a ON p.personId = a.personId;
