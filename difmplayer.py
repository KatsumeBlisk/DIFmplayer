#!/usr/bin/env python3

import os
import subprocess

def clear():
	subprocess.call("clear")

def menu():
	print("[L]ist stations")
	print("[P]lay station")
	print("[Q]uit")

def listStations():
	numStations = len(stations)
	for i in range(0, numStations):
		print("[", i + 1, "]", stations[i])

	print()

def playStation():
	print("Press [q] to stop station...")
	s = eval(input("Input station number to play: "))
	toPlay = path + "/" + stations[s - 1]
	subprocess.call(["mplayer", "-playlist", toPlay])

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
