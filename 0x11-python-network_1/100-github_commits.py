#!/usr/bin/python3

"""List first 10 commits of some repository."""


if __name__ == "__main__":
    import sys
    import requests

    repo = sys.argv[1]
    owner = sys.argv[2]

    headers = {"Authorization":
               f"Bearer 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"}
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    response = requests.get(url, headers=headers)
    commits = response.json()
    for commit in commits[0: 10]:
        print(f"{commit.get('sha')}:
                {commit.get('commit').get('author').get('name')}")
