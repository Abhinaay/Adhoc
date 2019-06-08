
#Problem Statement : Write a program to list number of users present in a linux based OS

#Answer :
#!/usr/bin/python3
 
import pwd


for p in pwd.getpwall():
	print p[0]





