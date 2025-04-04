#!/usr/bin/python3
# python script that fetches 'https://alu-intranet.hbtn.io/status'
"""making request to provided url"""
import urllib.request

url = "https://alu-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    content = response.read()
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print("\t- utf8 content:", content.decode("utf-8"))
