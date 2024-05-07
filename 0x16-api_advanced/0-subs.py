#!/usr/bin/python3
"""Module that queries the Reddit API and returns the number of subscribers
for a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    for a given subreddit.

    If not a valid subreddit, return 0.
    Invalid subreddits may return a redirect to search results. Ensure
    that you are not following redirects.

    Args:
        subreddit (str): subreddit

    Returns:
        int: number of subscribers or 0 if subreddit is invalid
    """
    base_url = 'https://www.reddit.com'
    url = '{}/r/{}/about.json'.format(base_url, subreddit)
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
    }
    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0

