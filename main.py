import config
import facebook


graph = facebook.GraphAPI(access_token=config.page_token, version="3.0")


latest_posts = graph.get_object(id=config.page_id, fields='posts.fields(type, name, created_time, object_id)')

post_1 = latest_posts['posts']['data'][1]


post_1_data = graph.get_object(post_1['id'], fields="reactions")

print(post_1_data)
