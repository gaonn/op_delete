import os
file_path = "C:\\Program Files (x86)\\Origin Games\\Apex\\media\\respawn.bik"

if(os.path.isfile(file_path) == True):
	os.remove(file_path)
