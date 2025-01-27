-- PostgreSQL query
select s.user_id , coalesce(round(avg(case when a.action = 'confirmed' then 1 else 0 end),2),0) as confirmation_rate  from Signups s
left join Confirmations a on s.user_id =a.user_id 
group by s.user_id