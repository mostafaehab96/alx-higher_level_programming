#!/usr/bin/python3

"""Making a POST request to a passed url with email."""

if __name__ == "__main__":
    import sys
    from urllib import request
    from urllib import parse

    url = sys.argv[1]
    email = sys.argv[2]
    variables = {"email": email}
    data = parse.urlencode(variables)
    data = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        data = response.read()
        print(data.decode('utf-8'))
