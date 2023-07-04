#!/usr/bin/python3

"""Sends request to url passed and checks for errors."""

if __name__ == "__main__":
    import sys
    from urllib import request
    from urllib.error import HTTPError

    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            data = response.read()
            print(data.decode('utf-8'))
    except HTTPError as e:
        print(f"Error code:{e.code}")
