#!/usr/bin/python3
"""a function that queries the Reddit
API and prints the titles of the first
10 hot posts listed for a given subreddit.
"""
import requests as r


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed
    """
    endpoint = 'https://reddit.com/r/{}.json?sort=hot&limit=10'
    headers = {'User-Agent': 'reese'}
    subs = r.get(endpoint.format(subreddit), headers=headers)

    if subs.status_code != 200:
        print(None)
        return 0

    subs = subs.json()
    subs = subs.get('data')
    subs = subs.get('children')

    for key in subs:
        print(key.get('data').get('title'))
