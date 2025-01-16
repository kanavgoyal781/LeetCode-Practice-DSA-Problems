# Write your MySQL query statement below
-- select x.cus, count(x.trans) as transac from
select x.cus as customer_id, count(*) as count_no_trans from
(select v.customer_id as cus, t.transaction_id as trans
from Visits as v
left join Transactions as t
on v.visit_id=t.visit_id) as x
where x.trans is NULL
group by x.cus
-- group by cus
-- having t.transaction_id is NULL
-- as x
-- group by x.cus
-- having count(x.trans)=0
