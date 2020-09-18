#!/usr/bin/python3
"""Function that queries the Reddit API"""
import requests


def count_words(subreddit, word_list):
    """
    parses the title of all hot articles, and prints a sorted count
    """
    hotp = requests.get('https://www.reddit.com/r/{}/hot.json'
                        .format(subreddit),
                        headers={"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) ' \
                                                'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                                                'Chrome/51.0.2704.103 Safari/537.36'},
                        allow_redirects=False,
                        params={'limit': 100})
    if hotp.status_code != 200:
        return
    else:
        my_dict = {}
        hotp = hotp.json()
        for word in word_list:
            counter = 0
            for post in hotp['data']['children']:
                counter += post['data']['title'].count(word)
            if counter != 0:
                my_dict[word] = counter
        for word in sorted(my_dict.keys()):
            print("{}: {}".format(word, my_dict[word]))
