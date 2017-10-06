#!/usr/bin/env python2

import os
bytes_threshold=805306368 # 768 Mb
#bytes_threshold=536870912 # 512 Mb
#bytes_threshold=15032385536 # 14Gb, for tests
logpath="/opt/SmartFoxServer_2X/SFS2X/logs"

files_dict = {}

statvfs_raw=os.statvfs(logpath)

bytes_free=statvfs_raw[4]*statvfs_raw[1]


if bytes_threshold > bytes_free:
	walk=os.walk(logpath)
	for currpath in walk:
		if (bool(currpath[2])==True):
			for currfile in currpath[2]:
				currfile_full=os.path.join(currpath[0],currfile)
				stat=os.stat(currfile_full)
				files_dict[stat[8]]=(stat[6],currfile_full)
	walk.close()
	sorted_timestamps=sorted(files_dict)
	to_free=bytes_threshold - bytes_free
	freed=0
	for i in sorted_timestamps:
		if (freed > to_free):
			break
		currstat=files_dict[i]
		print currstat[1]
		os.unlink(currstat[1])
		freed+=currstat[0]
