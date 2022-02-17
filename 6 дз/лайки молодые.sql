select 
sum(c_like)
from (SELECT 
*,
(SELECT count(*) FROM vk.like where 
media_id in (SELECT id FROM vk.media where media.user_id = profiles.user_id) or
post_id in (SELECT id FROM vk.posts where posts.user_id = profiles.user_id) or
message_id in (SELECT id FROM vk.messages where messages.from_user_id = profiles.user_id)) as c_like
FROM vk.profiles
order by birthday desc
limit 10) t
;