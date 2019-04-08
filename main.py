import config
import facebook
import json

graph = facebook.GraphAPI(access_token=config.page_token, version="3.0")

latest_posts = graph.get_object(id=config.page_id, fields='posts.fields(type, name, created_time, object_id)')
latest_posts = latest_posts['posts']['data']

def get_all_reactions(id):
    args = {}
    while True:
        objects = graph.request("{0}/{1}/reactions".format(graph.version, id), args)

        for object in objects['data']:
            yield object

        next = objects.get('paging', {}).get('next')

        if not next:
            return

        args['after'] = objects['paging']['cursors']['after']


post_reactions = {}

for post in latest_posts:
    reactions = get_all_reactions(post['id'])

    post_reactions[post['id']] = list(reactions)

print(json.dumps(post_reactions))