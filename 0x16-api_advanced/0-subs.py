#!/usr/bin/python3
"""
Script to return number of subscribers
"""
import csv
import requests
import json


def number_of_subscribers(subreddit):
    """Return the number of subscribers of a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    try:
        response = requests.get(url, allow_redirects=False, headers=headers)
        
        if response.status_code != 200:
            return 0

        try:
            result = response.json().get("data", None)
            if result is None:
                return 0
            return result.get("subscribers", 0)
        except ValueError:
            # In case response.json() fails
            return 0

    except requests.RequestException:
        # Handle network-related errors
        return 0
