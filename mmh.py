import requests
from Tkinter import Tk
import os
import sys

#from ui import Ui_Form 

from lxml import etree
import re
import string
from urllib2 import Request, urlopen, URLError
from TableParser import TableParser
from time import sleep

def addToClipBoard(text):
    command = 'echo ' + text.strip(' \t\n\r') + '| clip'
    os.system(command)




def Main_Loop():
	outputGames = []
	url = "http://makemehost.com/refresh/parse.php"
	r = requests.get(url)
	resp = r.text.split("\n")
	for line in resp: 
		#print line
		if line is "<br />": 
			pass
		else:
			#print line
			linec = line.split(",")
			#print "[~] DEBUG {}".format(len(linec))
			if len(linec) is 4:
				outputGames.append(linec)
	for game in outputGames:
		if re.match("[0-9].*\/[0-9].",game[2]): 
				num = game[2].split('/')
				#print num[0]
				if int(num[0]) is 0: 
						pass#	print "skipping"
				else:
					print "{} ====== {}".format(game[1], game[2])
			#len 





def Magic():
	outputGames = "1"
	url_addr ='http://makemehost.com/refresh/divGames-table-all.php'
	req = Request(url_addr)
	url = urlopen(req)
	tp = TableParser()
	tp.feed(url.read())
	prefGames = set()
	outputGames = set()
	for gamesList in tp.get_tables(): 
		
		for game in gamesList: 
			#print game[2]
			if re.search("[0-9].*\/[0-9].",game[2]): 
				num = game[2].split('/')
				result = int(num[0]) * int(num[1])
				#print result
				if result == 100: 
					pass
				if result > 80:
					outputGames.add("GAME, {}, >>>  {}  <<<".format(game[1].strip(' '), game[2].strip(' ')))
					pass
				if result > 60: 
					outputGames.add("GAME, {}, *  {}  *".format(game[1].strip(' '), game[2].strip(' ')))
					pass
				if result > 40: 
					outputGames.add("GAME, {}, {}".format(game[1].strip(' '), game[2].strip(' ')))
					pass 
					#print "[+] Game Found! Name: {}  || {}".format(game[1], game[2])

	for game in outputGames: 
		gameSplit = game.split(',')
		print "{}           {}".format(gameSplit[1], gameSplit[2])
		if "green" in gameSplit[1].lower(): 
				clip = gameSplit[1].strip()
				addToClipBoard(clip) 
				

				######
				# Some weird characters in this is causing battlenet coneection failures. 
				# uinsure what is going on right now, trying to investigate
				# Hex value = 09   HT ( Horizontal Tab ) temp fix placed in (' \t\n\r') split function

				#

				if re.search(".*green td.*", gameSplit[1].lower()):
						prefGames.add("{}{}".format(game[1].strip("\r\n\t"), game[2].strip(' ')))
		

				if re.search(".*legion td.*", gameSplit[1]):
						prefGames.add("{}{}".format(game[1].strip("\r\n\t"), game[2].strip(' ')))
				print "="*30
				print "The Following Preferred Games Were Found:"
				print "="*30
				for pref in prefGames: 
					print pref

if __name__ == "__main__":
	while True: 
		Main_Loop()
		sleep(10)
		#r = requests.get('http://makemehost.com/refresh/divGames-table-all.php')
		#print r.text
