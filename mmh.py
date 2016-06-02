import requests
import os
import re
import string
from time import sleep

def addToClipBoard(text):
    command = 'echo ' + text.strip(' \t\n\r') + '| clip'
    os.system(command)


def Main_Loop():
	print "[+] Starting...."
	outputGames = []
	url = "http://makemehost.com/refresh/parse.php"
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


if __name__ == "__main__":
	while True: 
		print "[+] Begin!"
		Main_Loop()
		print "[+] Done, Sleeping 10..."
		print "="*25
		sleep(10)
