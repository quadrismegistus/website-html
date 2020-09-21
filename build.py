#!/usr/bin/env python
import os
os.system('markdown README.md > content.html')

with open('theme.html') as theme_f,open('content.html') as content_f,open('index.html','w') as of:
    theme = theme_f.read()
    content = content_f.read()
    total = theme.replace('[[CONTENT]]',content)
    of.write(total)

