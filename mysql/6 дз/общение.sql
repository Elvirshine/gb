SELECT -- запрос считает количество отправленных сообщений конкретным пользователем.
count(*) as count, to_user_id, from_user_id
FROM vk.messages 
where 
	(from_user_id=48 and to_user_id in (SELECT from_user_id as user_id FROM vk.friendship_requests WHERE to_user_id=48 and status=1
union
SELECT to_user_id as user_id FROM vk.friendship_requests WHERE from_user_id=48 and status=1
)) 
or
	(to_user_id=48 and from_user_id in (SELECT from_user_id as user_id FROM vk.friendship_requests WHERE to_user_id=48 and status=1
union
SELECT to_user_id as user_id FROM vk.friendship_requests WHERE from_user_id=48 and status=1
))
	
group by from_user_id
order by count desc;