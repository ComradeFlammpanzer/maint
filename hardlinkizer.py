#!/usr/bin/env python2
# this script converts duplicated files from fdupes output to hardlinks
import os

fd=open("dupes.txt","r") # stdout of fdupes program :)

templist=[]


def hardlinks(filelist):
	for i in range(len(filelist)-1,0,-1):
		os.unlink(filelist[i])
		os.link(filelist[0],filelist[i])
	

for line in fd:
	sline=line.rstrip()
	if sline!="":
		templist.append(sline)
	else:
		hardlinks(templist)
		templist=[]


