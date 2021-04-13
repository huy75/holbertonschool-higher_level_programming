#!/usr/bin/python3
"""
Users github api to list out 10 most recent commits
from specified repo and user
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 3:
        h = {'Accept': 'application/vnd.github.v3+json'}
        u = "https://api.github.com/repos/{}/{}/commits"\
            .format(sys.argv[2], sys.argv[1])
        r = requests.get(u, params={'per_page': 10}, headers=h)
        for i, k in enumerate(r.json()):
            s = r.json()[i]['sha']
            n = r.json()[i]['commit']['author']['name']
            print("{}: {}".format(s, n))
