#!/bin/bash

if [ -z $3 ]; then
    echo "Usage: $0 iplist.txt sourcedir(./images) outputdir(./images-xp"
    exit 1 
fi

while read in; do
	cp $(find $2 -name "$in.png" -maxdepth 1) $3
done < $1
