#! /usr/bin/env python3

import os, requests

# Path to the data
path = "/data/feedback/"

keys = ["title", "name", "date", "feedback"]

directory = os.listdir(path)
for textfile in directory:
    keycount = 0
    feedback = {}
    with open(path + textfile) as file:
        for line in file:
            value = line.strip()
            feedback[keys[keycount]] = value
            keycount += 1
    print(feedback)
    response = requests.post("http://34.69.93.50/feedback/", json=feedback)
print(response.request.url)
print(response.request.body)
print(response.status_code)