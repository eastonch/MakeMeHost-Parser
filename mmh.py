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
debug = True

def clearBox():
#	for i in countBox(listybox):
	lb.delete(0, countBox(lb))
	lbFull.delete(0, countBox(lbFull))
	#return listybox

def sortList(someGameSet):
	unorderset = set()


def countBox(listybox):
	count = 0
	for i in enumerate(listybox.get(0, END)):
		count = count + 1
	print count
	return int(count)

def doRefresh():
	print "Before clearing.... {}".format(countBox(lb))
	clearBox()
	print "After Clearing.... {}".format(countBox(lb))
	refreshed = refresh()
	lb.update_idletasks()
	lbFull.update_idletasks()
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

def refresh():
	print "[+] Refreshing available games"
	r = requests.get(url)
	if r.status_code == 200: 
		print "hello, refreshed" 
		return r.text
	else:
		print "[!] Could not Connect to MMH"
		return False



def addToLB(game, players):
	result = 0
	if re.match("[0-9]?[0-9]\/[0-9]?[0-9]", players):
		in1 = players.split("/")
		num1 = float(in1[0])
		num2 = float(in1[1])
		result = num1 / num2 * 100
		#if debug:
			#print "[#]EVAL {} / {} * 100 == {}".format(num1, num2, result)
	else:
		print "Major Error..."
		pass
	lb.insert(END, "{} | {}".format(game, players))
	if result > 80:
		lb.itemconfig(END, bg="green") 
		lbFull.insert(END, "{} | {}".format(game, players))
	elif result > 60:
		lb.itemconfig(END, bg="yellow")  
	elif result > 30:
	 	lb.itemconfig(END, bg="teal") 

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





#debug 




if __name__ == "__main__":
	refreshButton = Button(win, text="Refresh!", command=doRefresh).pack()
	l1 = Label(win, text="All Games")
	l1.pack()
	lb = Listbox(win, height=30, width=60)
	lb.pack()
	
	l2 = Label(win, text="Games Almost Full")
	l2.pack()
	lbFull = Listbox(win, height=30, width=60)
	lbFull.pack()
	lb.insert(END, "FOO")
	lb.insert(END, "BAR")
	win.mainloop()