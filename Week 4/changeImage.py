#!/usr/bin/env python3

import os, sys
from PIL import Image

directory = '/home/student-04-5b621141c5eb/supplier-data/images/'

for filename in os.listdir(directory):
       if not filename.startswith('.') and 'tiff' in filename:
              im = Image.open(directory + filename)
              im.resize((600,400)).convert("RGB").save(directory + filename.split(".")[0] + '.jpeg')
              im.close()