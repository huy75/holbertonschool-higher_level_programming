#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""
if __name__ == "__main__":
    import requests
    req = requests.get('https://intranet.hbtn.io/status')
    response = req.text
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
