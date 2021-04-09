#!/usr/bin/python3
"""
script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""
if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    from sys import argv

    user = argv[1]
    pswd = argv[2]
    r = requests.get('https://api.github.com/users/{}'.format(user),
                     auth=HTTPBasicAuth(user, pswd))
    print(r.json().get('id'))
