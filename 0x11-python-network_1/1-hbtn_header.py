#!/usr/bin/python3

"""Gets the header value of url passed as argument."""

if __name__ == "__main__":
    import sys
    from urllib import request

    url = sys.argv[1]
    with request.urlopen(url) as response:
        headers = response.info()
        print(headers.get("X-Request-Id"))
