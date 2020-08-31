#!/usr/bin/env python3

import os, sys
from PIL import Image
directory = '/home/student-01-d317b321049b/images/'

for filename in os.listdir(directory):
       im = Image.open(directory + filename)
       newname = "/opt/icons/"
       im.rotate(-90).resize((128,128)).convert("RGB").save(newname + image + '.jpeg')
       im.close()