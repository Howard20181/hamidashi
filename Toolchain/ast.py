#!/usr/bin/env python3
import re
import sys

pattern = re.compile(r'(?<=ja={\s{\s)(\".*\",?\s?)?(?:{.*},?\s?)?'
                     r'(\".*\",?\s?)?(?:{.*},?\s?)?'
                     r'(\".*\",?\s?)?(?:{.*},?\s?)?'
                     r'(\".*\",?\s?)?(?:{.*},?\s?)?'
                     r'(\".*\",?\s?)?(?:{.*},?\s?)?'
                     r'(\".*\",?\s?)?(?:{.*},?\s?)?'
                     r'(\".*\",?\s?)?(?:{.*},?\s?)?'
                     r'(\".*\",?\s?)?(?:{.*},?\s?)?'
                     r'(\".*\",?\s?)?(?:{.*},?\s?)?(?=\s},)')

if len(sys.argv) < 2:
    exit()

f = open(sys.argv[1], encoding='utf-8')

content = f.read()
f.close()

lst = pattern.findall(content)
for i in lst:
    for t in i:
        if t != "":
            print(t)

exit()
