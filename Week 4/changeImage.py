#!/usr/bin/env python3

import os, sys
from PIL import Image

directory = '/home/student-01-d317b321049b/images/'
newname = "/opt/icons/"

for filename in os.listdir(directory):
       im = Image.open(directory + filename)
       im.resize((600,400)).convert("RGB").save(newname + filename + '.jpeg')
       im.close()