# -*- coding: utf-8 -*-
import base64
code = raw_input("plz input some thing")
count = 0
try:
    print "\nTEST\n"
    while True:
        code = base64.decodestring(code)
        count += 1
except:
    print code, count