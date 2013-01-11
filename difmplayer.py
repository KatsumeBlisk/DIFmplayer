#!/usr/bin/python3

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

	
path = input("Input path to stations: ")

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
