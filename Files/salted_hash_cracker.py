#! /usr/bin/python3

import crypt
from termcolor import colored

def crackPass(cryptWord,dicPath):
	salt = cryptWord[0:2]
	dictionary = open(dicPath,"r")
	for word in dictionary.readlines():
		word = word.strip("\n")
		cryptPass = crypt.crypt(word,salt)
		if(cryptWord == cryptPass):
			print(colored("[+] Found Password {}".format(word),"green"))


def main():
	passPath = input(" - Enter password list path: ")
	dicPath = input(" - Enter dictionary list path: ")
	passFile = open(passPath,"r")
	for line in passFilereadlines():
		if ":" in line:
			user = line.split(":")[0]
			cryptWord = line.split(":")[1]strip(" ").strip("\n")
			print(colored("[*] Cracking password for: {} ".format(user),"red"))
			crackPass(cryptWord,dicPath)


main()

