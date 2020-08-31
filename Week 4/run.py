#! /usr/bin/env python3

import os, requests, json

directory = '/home/student-04-5b621141c5eb/supplier-data/descriptions/'
keys = ["name", "weight", "description", "image_name"]

for filename in os.listdir(directory):
    if filename.endswith('txt'):
        keycount = 0
        description = {}
        with open(directory + filename) as file:
            for line in file:
                if keycount != 1:
                    description[keys[keycount]] = line.strip()
                    keycount += 1
                else:
                    description[keys[keycount]] = line.strip()[:-4]
                    keycount += 1
        description["image_name"] = filename.split(".")[0] + ".jpeg"
        r = requests.post("http://localhost/fruits/", json=description)