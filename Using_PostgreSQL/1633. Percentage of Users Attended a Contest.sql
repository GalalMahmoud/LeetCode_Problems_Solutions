-- PostgreSQL query

select r.contest_id , round((count(r.user_id::decimal)/(select count(users.user_id::decimal)::decimal from users))*100::decimal,2) as percentage 
from Register r 
group by r.contest_id 
order by percentage desc, r.contest_id asc