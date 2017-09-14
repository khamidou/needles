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
            month = "{}-{}".format(creation_time.year, str(creation_time.month).zfill(2))
            coords = "{}, {}".format(row[14], row[15])
            lines[month].append(coords)
        except IndexError:
            continue
        except ValueError:
            continue

for month in lines:
    with open("{}.csv".format(month), 'w+') as fd:
        for line in lines[month]:
            fd.write(line)
            fd.write('\n')
