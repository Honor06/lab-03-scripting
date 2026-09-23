#!/usr/bin/env python3
import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'

def retrieve_events(url):

    """"downloads data from url resulting in a JSON text string which it passes to json.loads(...) and returns that Python object"""

    request = requests.get(url).text
    return json.loads(request)

def print_events(events, n=5):
    """"prints the first n events in the list in the form type :: repo"""
    for x in events[:n]:
         event = x['type'] + ' :: ' + x['repo']['name']
    print(event)

def main():
    print(GHUSER)
    print(url)
    events = retrieve_events(url)
    print_events(events)

if __name__ == "__main__":
    main()