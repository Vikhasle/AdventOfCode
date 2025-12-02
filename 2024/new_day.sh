#!/bin/bash

day=$(find ./* -maxdepth 0 -type d | wc -l)
day=$((day + 1))
echo "Making $day directory"
mkdir "Day$day"
cp template.py "Day$day/day$day.py"
