#!/usr/bin/python3
"""
Script to return number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers of a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    response = requests.get(url, allow_redirects=False, headers=headers)
    if response.status_code != 200:
        return 0

    result = response.json().get("data")
    return result.get("subscribers")
