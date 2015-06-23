#!/usr/bin/env python3

"""Example analysis script.

Author: Stian Soiland-Reyes

https://github.com/ResearchObject/ro-tutorials/
"""

import csv

earliest=None
latest=None

for row in csv.reader(open("rawdata5.csv")):
    name = row[0]
    start = int(row[1])
    stop = int(row[2])

    if earliest is None or start < earliest[1]:
        earliest = (name, start)
    if latest is None or stop> latest[1]:
        latest = (name, stop)

print("Earliest:", earliest)
print("Latest:", latest)

