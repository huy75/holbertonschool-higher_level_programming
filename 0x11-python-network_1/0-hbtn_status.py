#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""
if __name__ == "__main__":
    from urllib.request import Request, urlopen
    req = Request("https://intranet.hbtn.io/status")
    with urlopen(req) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(html.__class__))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode()))
