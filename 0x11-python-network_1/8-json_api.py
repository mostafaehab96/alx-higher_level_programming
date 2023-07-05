#!/usr/bin/python3

"""script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

if __name__ == "__main__":
    import sys
    import requests

    q = sys.argv[1] if len(sys.argv) > 1 else None
    url = "http://0.0.0.0:5000/search_user"
    params = {"q": q}

    if q:
        response = requests.post(url, data=params)
    else:
        response = requests.post(url)
    try:
        data = response.json()
        if len(data) == 0:
            print("No result")
        else:
            print(f"[{data.get('id')}] {data.get('name')}")
    except Exception:
        print("Not a valid JSON")
