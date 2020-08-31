#!/usr/bin/env python3

import requests, os

directory = '/home/student-04-5b621141c5eb/supplier-data/images/'
url = "http://localhost/upload/"

for filename in os.listdir(directory):
    if not filename.startswith('.') and 'jpeg' in filename:
        with open(directory + filename, 'rb') as opened:
            r = requests.post(url, files = {'file': opened})