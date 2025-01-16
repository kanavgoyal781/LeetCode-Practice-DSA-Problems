# Write your MySQL query statement below

select id from (
Select id, recordDate, temperature,
lag(temperature) over(order by recordDate) as meow,
lag(recordDate) over(order by recordDate) as date_k
from Weather
) AS X
-- as meow
--  from Weather) as x
where x.temperature>x.meow and DATEDIFF(x.recordDate, x.date_k) =1
