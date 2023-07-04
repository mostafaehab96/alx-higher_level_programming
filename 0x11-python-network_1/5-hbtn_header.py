#!/usr/bin/python3

"""Displays the value of the variable X-Request-Id in the response header."""

if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))
