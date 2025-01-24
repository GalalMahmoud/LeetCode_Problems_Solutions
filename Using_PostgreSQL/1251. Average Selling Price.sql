-- PostgreSQL query
select p.product_id, coalesce(round(sum(u.units::decimal*p.price::decimal)/sum(u.units::decimal),2),0) as average_price  
from  prices p 
left join 
    unitssold u on p.product_id = u.product_id 
    and u.purchase_date  between p.start_date and p.end_date   
group by p.product_id  