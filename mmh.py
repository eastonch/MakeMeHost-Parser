import requests
import os
import re
import string
from time import sleep
from Tkinter import *

#Def Vars 
outputGames = []
url = "http://makemehost.com/refresh/parse.php"
debug = True

def clearBox(listybox):
	for i, listboxentry in enumerate(listybox.get(0, END)):
		listybox.delete(0, END)

def countBox(listybox):
	count = 0
	for i in enumerate(listybox.get(0, END)):
		count = count + 1
	return int(count)
def doRefresh():
	print "Before clearing.... {}".format(countBox(lb))
	clearBox(lb)
	lb.update_idletasks()
	print "After Clearing.... {}".format(countBox(lb))
	refreshed = refresh()
	if not refreshed: 
		print "[!] Failed to connect, check net and try again"
	else: 
		resp = refreshed.split("\n")
		for line in resp:
			if line is "<br />":
				print "[#] Skipping break line"
				pass
			else:	
				linec = line.split(",")
				if len(linec) is 4:
					outputGames.append(linec)
	for game in outputGames:
		gameSplit = str(game).split(",")
		#print "{}{}".format(game[1], game[2])
		addToLB(game[1], game[2])
	addToLB("magical", "something==========================================================")

def refresh():
	print "[+] Refreshing available games"
	r = requests.get(url)
	if r.status_code == 200: 
		print "hello, refreshed" 
		return r.text
	else:
		print "[!] Could not Connect to MMH"
		return False

def UpdateGames():
	getGames()
	win.after(5000, UpdateGames)

def addToLB(game, players):
	lb.insert(END, "{} | {}".format(game, players))


def addToClipBoard(text):
	text.strip(' \t\n\r')
	text = text.split('|')
    #command = 'echo {}| clip'.format(text[1])
    #os.system(command)


def Main_Loop():
	print "[+] Starting...."
	outputGames = []
	r = requests.get(url)
	if r.status_code == 200:
		resp = r.text.split("\n")
		for line in resp: 
			if line is "<br />": 
				pass
			else:
				linec = line.split(",")
				if len(linec) is 4:
					outputGames.append(linec)
		for game in outputGames:
			if re.match("[0-9].*\/[0-9].",game[2]): 
					num = game[2].split('/')
					if int(num[0]) is 0: 
						pass

					else:
						print "{} ====== {}".format(game[1], game[2])



win=Tk()
refresbut = Button(win, command=doRefresh).pack()
lb = Listbox(win, height=15, width=60)
lb.pack()
lb.insert(END, "somenettry")
lb.insert(END, "somenettry1")
win.mainloop()
if __name__ == "__main__":
	while True: 
		print "[+] Begin!"
		Main_Loop()
		print "[+] Done, Sleeping 10..."
		print "="*25
		sleep(10)
'''
refreshed = refresh()
if !refreshed: 
	print "[!] Failed to connect, check net and try again"
else: 
	resp = refreshed.split("\n")
	for line in resp:
		if line is "<br />":
			if debug:
				print "[#] Skipping break line"
				pass
			else:
				linec = line.split(",")
				if len(linec) is 4:
					outputGames.append(linec)


def
''' 