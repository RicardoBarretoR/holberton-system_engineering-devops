#!/usr/bin/python3
"""Function that queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    returns a list containing the titles of all hot articles
    """
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    user_agent_header = 'Mozilla/5.0 (X11; Linux x86_64) ' \
                        'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                        'Chrome/51.0.2704.103 Safari/537.36'
    limit_posts = 100
    r = requests.get(url, allow_redirects=False,
                     headers={'User-Agent': user_agent_header},
                     params={'limit': limit_posts, 'after': after})
    if r.status_code == 200:
        try:
            data = r.json()
            list_hot_posts = data.get('data', None).get('children', None)
            after = data.get('data', None).get('after', None)
            for post in list_hot_posts:
                hot_list.append(post.get('data').get('title'))
            if after:
                hot_list = recurse(subreddit, hot_list, after)
        except:
            pass
        return hot_list
