#!/bin/bash

if [[ $# -eq 0 ]] ; then
    echo 'Pass filename where iplist exists (one ip per line)'
    exit 0
fi

if [ ! -d ./images ]; then
  mkdir -p ./images;
fi

LIMIT=2
for i in $(cat $1); do
	sem -j $LIMIT "./stickyKeysHunter.sh ${i}; echo ${i} > lastip.txt"
done
sem --wait
