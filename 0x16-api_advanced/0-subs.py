#!/usr/bin/python3
"""Module for task 0"""


import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribersto the subreddit"""
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'} # Set a custom User-Agent to avoid getting blocked by Reddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json" # Construct the URL to fetch subreddit information
    info = requests.get(url, headers=headers, allow_redirects=False) # Send a GET request to the URL
    if info.status_code == 200: # If the request was successful
        data = info.json() # Parse the JSON response
        return data['data']['subscribers'] # Extract the number of subscribers from the response
    else: # If the request was unsuccessful
     return 0 # Return 0 as the number of subscribers
