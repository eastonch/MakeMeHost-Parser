import requests
import os
import re
import string
from time import sleep
from Tkinter import *

#Def Vars 
win=Tk()
outputGames = []
url = "http://makemehost.com/refresh/parse.php"
debug = False

allGames = StringVar()

def version():
	print "<<< MakeMeHost-Parser v0.1 Christopher Easton @_ChrisTux, eastonch@gmail.com >>>"

def countBox(givenLb):
	count = 0
	print count
	for i in enumerate(givenLb.get(0, END)):
		if debug:
			print "found one"
		count = count + 1
	if debug: 
		print count
	return int(count)

def doRefresh():
	lb.delete(0, END)
	ClearL()
	ClearF()
	lbFull.delete(0, END)
	refreshed = refresh()
	if not refreshed: 
		print "[!] Failed to connect, check net and try again"
		lb.insert(START, "Failure to connect...")
	else: 
		resp = refreshed.split("\n")
		for line in resp:
			linec = line.split(",")
			if len(linec) is 4:
				outputGames.append(linec)
		for game in outputGames:
			gameSplit = str(game).split(",")
			#print "{}{}".format(game[1], game[2])
			addToLB(game[1], game[2])
	allGames.set("Current Games: {}".format(countBox(lb)))

def refresh():
	print "[+] Refreshing available games"
	r = requests.get(url)
	if r.status_code == 200: 
		print "hello, refreshed" 
		return r.text
	else:
		print "[!] Could not Connect to MMH"
		return False

def ClearL():
	lb.delete(0, END)

def ClearF():
	lbFull.delete(0, END)

def addToLB(game, players):
	result = 0
	if re.match("[0-9]?[0-9]\/[0-9]?[0-9]", players):
		in1 = players.split("/")
		num1 = float(in1[0])
		num2 = float(in1[1])
		result = num1 / num2 * 100
		if debug:
			print "[#]EVAL {} / {} * 100 == {}".format(num1, num2, result)
	else:
		print "Major Error..."
		pass
	lb.insert(END, "{} | {}".format(game, players))
	care = False
	if result > 80:
		lb.itemconfig(END, bg="green") 
		care = True
	elif result > 60:
		lb.itemconfig(END, bg="yellow")
		care = True
	elif result > 30:
	 	lb.itemconfig(END, bg="teal") 

	if care:
		lbFull.insert(END, "{} | {}".format(game, players))

def addToClipBoard(text):
	text.strip(' \t\n\r')
	text = text.split('|')
	command = 'echo {}| clip'.format(text[1])
	os.system(command)


if __name__ == "__main__":
	version()
	if debug:
		print "DEBUG MODE ENABLED"
	refreshButton = Button(win, text="Refresh!", command=doRefresh).pack()
	Clearer = Button(win, text="Clear!", command=ClearL).pack()
	l1 = Label(win, textvariable=allGames).pack()
	lb = Listbox(win, height=30, width=60)
	lb.pack()
	
	l2 = Label(win, text="Games Of Interest")
	l2.pack()
	lbFull = Listbox(win, height=30, width=60)
	lbFull.pack()
	if not debug: # change this 
		lb.insert(END, "FOO")
		lb.insert(END, "OOF")
		lbFull.insert(END, "BAR")
		lbFull.insert(END, "RAB")
	else:
		lb.insert(END, "Press Refresh!")
		lbFull.insert(END, "Waiting for refresh...")
	win.mainloop()



	# DEPRECATED
# def Main_Loop():
# 	print "[+] Starting...."
# 	outputGames = []
# 	r = requests.get(url)
# 	if r.status_code == 200:
# 		resp = r.text.split("\n")
# 		for line in resp: 
# 			if line is "<br />": 
# 				pass
# 			else:
# 				linec = line.split(",")
# 				if len(linec) is 4:
# 					outputGames.append(linec)
# 		for game in outputGames:
# 			if re.match("[0-9].*\/[0-9].",game[2]): 
# 					num = game[2].split('/')
# 					if int(num[0]) is 0: 
# 						pass

# 					else:
# 						print "{} ====== {}".format(game[1], game[2])


def clearBox():
#	for i in countBox(listybox):
	for i in enumerate(lb.get(0, END)): 
		lb.delete(0, END)
		print i
		lb.update_idletasks()
	for i in enumerate(lbFull.get(0, END)):
		lbFull.delete(0, END)
		print i
		lbFull.update_idletasks()
	#return listybox

def countBox(listybox):
	count = 0
	for i in enumerate(lb.get(0, END)):
		print "Found one"
		count = count + 1
	print count
	return int(count)


def sortList(someGameSet):
	unorderset = set()

