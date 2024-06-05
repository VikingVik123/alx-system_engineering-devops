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

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        if "data" in data and "children" in data["data"]:
            posts = data["data"]["children"]
            for post in posts:
                print(post["data"]["title"])
        else:
            print("No posts found in the subreddit '{}'.".format(subreddit))

    except requests.RequestException as e:
        print("An error occurred:", e)
