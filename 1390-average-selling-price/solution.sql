Select dumb.product_id, sum(dumb.average_price) as average_price from (select p.product_id, (case when (u.units=0 or u.units is NULL) THEN 0 ELSE round(sum(p.price*u.units)/sum(u.units),2)  END) as average_price
from Prices as p 
left outer join UnitsSold as u
on p.product_id=u.product_id and u.purchase_date between p.start_date and p.end_date
group by p.product_id

union

select p.product_id, round(sum(p.price*u.units)/sum(u.units),2) as average_price
from Prices as p 
right outer join UnitsSold as u
on p.product_id=u.product_id and u.purchase_date between p.start_date and p.end_date
group by p.product_id) as dumb
group by dumb.product_id;
