#!/usr/bin/python3
"""
Users github api to list out 10 most recent commits
from specified repo and user
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    repo = argv[1]
    owner = argv[2]
    u = "http://api.github.com/repos/{}/{}/commits".format(owner, repo)

    response = requests.get(url=u, params={'per_page': 10})
    if response.status_code != 200:
        print("None")
    else:
        commits = response.json()
        try:
            for each in commits:
                print("{}: {}".format(
                    each.get("sha"),
                    each.get("commit").get("author").get("name")))
        except IndexError:
            pass
