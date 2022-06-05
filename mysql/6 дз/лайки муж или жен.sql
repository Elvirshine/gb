select 
if((
	(select count(id) from vk.like where user_id in 
	(select user_id from vk.profiles where gender="m")) 
> 
	(select count(id) from vk.like where user_id in 
    (select user_id from vk.profiles where gender="f"))
), "m", "f") as result;