-- # Write your MySQL query statement below

-- with meow as (
-- (select query_name, count(rating) as loda
-- from queries 
-- where rating<3
-- group by query_name))
-- select q.query_name, 
-- round(((sum(q.rating/q.position)/count(q.query_name))),2) as quality,
-- Case when meow.loda is NULL then 0 else 
-- round(((meow.loda)/count(q.query_name))*100,2) END as poor_query_percentage
-- from queries as q
-- left outer join meow
-- on q.query_name=meow.query_name
-- group by q.query_name

SELECT query_name, ROUND(AVG(rating/position),2) AS quality, ROUND(AVG(rating<3)*100,2) AS poor_query_percentage
FROM Queries
GROUP BY query_name;
