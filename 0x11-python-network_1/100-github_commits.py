#!/usr/bin/python3

"""List first 10 commits of some repository."""


if __name__ == "__main__":
    import sys
    import requests

    repo = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    response = requests.get(url)
    commits = response.json()
    for commit in commits[0: 10]:
        print(f"{commit.get('sha')}: "
              f"{commit.get('commit').get('author').get('name')}")
