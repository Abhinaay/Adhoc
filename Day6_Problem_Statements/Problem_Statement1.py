
#Problem Statement : Write a program to create 100 files and 200 directories

#Answer :
#!/usr/bin/python3
 
from pathlib import Path

#To create 100 empty files
for i in range(100):
	Path("file%s.txt"%i).touch()


#To create 200 directories
for j in range(200):
	Path("dir%s"%i).mkdir()




