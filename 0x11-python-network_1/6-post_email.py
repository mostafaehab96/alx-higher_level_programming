#!/usr/bin/python3

"""sends a POST request to the passed URL with the email as a parameter,
and print the body of the response.
"""

if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    email = sys.argv[2]
    params = {"email": email}

    response = requests.post(url, data=params)
    print(response.text)
