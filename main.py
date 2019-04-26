import config
import facebook
import json
import sys

graph = facebook.GraphAPI(access_token=config.page_token, version="3.0")


def get_all(id, type, max = sys.maxsize):
    args = {}
    count = 0

    while True:
        objects = graph.request("{0}/{1}/{2}".format(graph.version, id, type), args)

        for object in objects['data']:
            yield object
            count += 1
            if count == max:
                return


        next = objects.get('paging', {}).get('next')

        if not next or type == 'posts':
            return

        args['after'] = objects['paging']['cursors']['after']


latest_posts = get_all(config.page_id, 'posts', 2)

post_reactions = {}

for post in latest_posts:
    reactions = get_all(post['id'], 'reactions')

    post_reactions[post['id']] = list(reactions)

print(json.dumps(post_reactions))