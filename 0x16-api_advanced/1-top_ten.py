#!/usr/bin/python3
"""Function that queries the Reddit API"""
import requests


def top_ten(subreddit):
    """
    The first 10 hot posts listed
    """
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    user_agent_header = 'Mozilla/5.0 (X11; Linux x86_64) ' \
                        'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                        'Chrome/51.0.2704.103 Safari/537.36'
    limit_posts = 10
    r = requests.get(url, allow_redirects=False,
                     headers={'User-Agent': user_agent_header},
                     params={'limit': limit_posts})
    if r.status_code == 200:
        try:
            data = r.json()
            list_hot_posts = data.get('data', None).get('children', None)
            for post in list_hot_posts:
                print(post.get('data').get('title'))
        except:
            print(None)
    else:
        print(None)
