#!/bin/bash

# This script is to be run to remove "Digitally Imported - " from your stations' file names
# and remove spaces
# I am not responsible for what happens to the file names. BACK THEM UP BEFORE TRYING THIS

read -p "Input path to the directory of files to clean up: " path

cd $path

find -name "* *" -type f | rename 's/ /_/g'

for i in *.pls
do
	file=${i:21}
	mv $i ./$file
done
