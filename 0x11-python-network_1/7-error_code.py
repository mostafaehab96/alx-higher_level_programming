#!/usr/bin/python3

"""Sends a request to the URL and displays the body of the response
with handling of error code."""


if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]

    response = requests.get(url)
    code = response.status_code

    if code >= 400:
        print(f"Error code: {code}")
    else:
        print(response.text)
