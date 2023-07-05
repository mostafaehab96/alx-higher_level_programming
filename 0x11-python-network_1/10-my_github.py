#!/usr/bin/python3

"""Gets an information about a github user."""

if __name__ == "__main__":
    import sys
    import requests

    username = sys.argv[1]
    password = sys.argv[2]

    url = f"https://api.github.com/users/{username}"
    headers = {"Authorization": f"Bearer {password}"}

    response = requests.get(url, headers=headers)
    data = response.json()
    print(data.get('id'))
