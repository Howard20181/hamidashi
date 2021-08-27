#!/usr/bin/env python3
import re
import sys

pattern = re.compile(r'ja=\{\n\{\n"([^\n]{1,200})"')

if len(sys.argv)<2:
    exit()

f = open(sys.argv[1])

content = f.read()
f.close()

lst = pattern.findall(content)
for i in lst:
    print(i)

exit()