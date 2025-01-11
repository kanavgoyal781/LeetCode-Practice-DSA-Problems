# Write your MySQL query statement below
select Euni.unique_id,E.name
from Employees as E
left outer join EmployeeUNI as Euni
on E.id=Euni.id
