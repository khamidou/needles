#!/usr/bin/env python
import sys
import csv
from collections import defaultdict
from dateutil.parser import parser as date_parser


lines = defaultdict(list)

with open(sys.argv[1]) as fd:
    reader = csv.reader(fd)
    parser = date_parser()
    for row in reader:
        try:
            if row[14] == '0' and row[15] == '0':
                continue

            creation_time = parser.parse(row[1])
            coords = "{}, {}".format(row[14], row[15])
            lines[creation_time.year].append(coords)
        except IndexError:
            continue
        except ValueError:
            continue

for year in lines:
    with open("{}.csv".format(year), 'w+') as fd:
        for line in lines[year]:
            fd.write(line)
            fd.write('\n')
