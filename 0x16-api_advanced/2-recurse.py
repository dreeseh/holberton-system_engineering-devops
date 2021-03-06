#!/usr/bin/python3
"""a recursive function that queries the
Reddit API and returns a list containing
the titles of all hot articles for a given
subreddit
"""
import requests as r


def recurse(subreddit, hot_list=[], key=''):
    """queries the Reddit API and returns a list
    """
    endpoint = 'http://reddit.com/r/{}/hot.json'
    headers = {"User-Agent": "reese"}
    params = {'after': key}
    subs = r.get(endpoint.format(subreddit), headers=headers, params=params)

    if subs.status_code != 200:
        return None

    subs = subs.json().get('data')
    after = subs.get('after')
    subs = subs.get('children')

    for key in subs:
        hot_list.append(key.get('data').get('title'))

    if after:
        recurse(subreddit, hot_list, after)

    return(hot_list)
