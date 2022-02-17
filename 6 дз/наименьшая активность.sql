select user_id, CHP_uid,communities_uid, FR_sends, like_uid, media_uid, message_uid, post_uid,
(CHP_uid + communities_uid + FR_sends + like_uid + media_uid + post_uid + message_uid) as summ
from (SELECT *,
	(SELECT count(communities_has_profile.user_id) FROM vk.communities_has_profile where communities_has_profile.user_id = profiles.user_id) as CHP_uid,
	(SELECT count(communities.admin_id) FROM vk.communities where communities.admin_id = profiles.user_id) communities_uid,
	(SELECT count(friendship_requests.from_user_id) FROM vk.friendship_requests where friendship_requests.from_user_id = profiles.user_id) as FR_sends,
	(SELECT count(vk.like.user_id) FROM vk.like where vk.like.user_id = profiles.user_id) as like_uid,
	(SELECT count(media.user_id) FROM vk.media where media.user_id = profiles.user_id) as media_uid,
	(SELECT count(messages.from_user_id) FROM vk.messages where messages.from_user_id = profiles.user_id) as message_uid,
	(SELECT count(posts.user_id) FROM vk.posts where posts.user_id = profiles.user_id)  as post_uid
	
FROM vk.profiles) as t
order by summ 
limit 10
;