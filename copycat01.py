#!/usr/bin/env python3

import shutil
#This module provides a portable way of using operating system dependent functionality.
#Where shutil allows for higher-level file manipulation, os is more targeted at the operating system.
import os

#force our Python program to 'start' in the home user directory
#This will allow the user to run the program from any location on the system, and our scriptstill always start at /home/student/mycode/
os.chdir("/home/student/mycode/")

#will copy the file at the path source to the folder at the path destination
#This function returns a string of the path of the copied file.
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

shutil.copytree("5g_research/", "5g_research_backup/")


