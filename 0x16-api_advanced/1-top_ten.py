#!/usr/bin/python3
"""
Script to return top ten reddits
"""
import requests
import json


def top_ten(subreddit):
    """
    Func to fetch the data
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    params = {
        "limit": 10
    }
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=params)
    if response.status_code == 404:
        return None

    result = response.json()
    if "data" in result and "children" in result["data"]:
        posts = result["data"]["children"]
        for post in posts:
            print(post["data"]["title"])
    else:
        print("None")
