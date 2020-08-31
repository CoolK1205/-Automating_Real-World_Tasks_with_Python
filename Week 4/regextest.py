import re

text = '300 lbs'

m = re.search(r"^(\d*)", text)
if m:
    found = m.group(1)
print(m[1])