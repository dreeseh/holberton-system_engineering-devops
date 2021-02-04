#!/usr/bin/python3
""" a function that queries the Reddit API
and returns the number of subscribers
"""
import requests as r


def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'reese'}
    endpoint = 'https://reddit.com/r/{}/about.json'

    subs = r.get(endpoint.format(subreddit), headers=headers)

    if subs.status_code is not 200:
        return 0
    else:
        return subs.json().get('data').get('subscribers')
