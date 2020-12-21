#!/usr/bin/python3

import os

targetdir = "/dev/shm/testremove"

alldirs = []

walk = os.walk(targetdir)


for currdir in walk:
    path,dirs,files = currdir
    alldirs.append(path)
    if len(files) != 0 :
        for F in files:
            os.unlink(os.path.join(path,F))

while alldirs:
    os.rmdir(alldirs.pop())


