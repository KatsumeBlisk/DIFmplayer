#!/usr/bin/env python3

import os
import subprocess
import random

def clear():
	subprocess.call("clear")

def menu():
	print("[L]ist stations")
	print("[P]lay station")
	print("[R]andom station")
	print("[Q]uit")

def listStations():
	numStations = len(stations)
	for i in range(0, numStations):
		print("[", i + 1, "]", stations[i])
	print()

def startStation(toPlay):
	subprocess.call(["mplayer", "-quiet", "-playlist", toPlay])

def playStation():
	s = int(input("Input station to play: "))
	print("Press [p] to pause the station...")
	print("Press [q] to stop the station...")
	input("Press enter to continue. . .")
	startStation(path + "/" + stations[s - 1])
	

def randomStation():
	print("Press [p] to pause the station...")
	print("Press [q] to stop the station...")
	input("Press enter to continue. . .")
	startStation(path + "/" + stations[random.randint(0, len(stations) - 1)])

home = os.getenv("HOME")

if((os.path.isfile(home + "/.difmplayer.conf"))):
	conf = open(home + "/.difmplayer.conf")
	path = conf.read()
	conf.close()

else:
	path = input("Input your stations directory: ")
	save = input("Would you like to set this as the default directory? [y/n] ")
	if save.lower() == "y":
		conf = open(home + "/.difmplayer.conf", mode='w')
		conf.write(path)
		conf.close()

stations = os.listdir(path)

stations.sort()

choice = ""

clear()

while choice.lower() != "q":
	menu()
	choice = input("% ")
	
	if choice.lower() == "l":
		clear()
		listStations()

	elif choice.lower() == "p":
		playStation()
		clear()

	elif choice.lower() == "r":
		randomStation()
		clear()