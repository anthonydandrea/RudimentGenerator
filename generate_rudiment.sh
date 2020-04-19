#!/bin/sh

echo $1
echo $2 > test.txt

echo "python3 main.py $2 > $1.ly && lilypond $1.ly" > test.txt

cd server
python3 main.py $2 > $1.ly && lilypond $1.ly
mv $1.pdf ../static/rudiments
rm $1.ly
