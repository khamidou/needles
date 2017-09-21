#!/usr/bin/env python
import os
import sys
import glob

for file in glob.glob(os.path.join(sys.argv[1], '*.csv')):
    filename, file_extension = os.path.splitext(file)
    cmd = "python heatmap --filetype csv -o {}.png -b black -r 30 -W 600 --osm {} -e 37.813852,-122.519188,37.704467,-122.370186".format(filename, file)
    print cmd
    os.system(cmd)

    naked_filename = os.path.basename(filename)
    cmd2 = "convert -background '#0008' -fill white -gravity center -size 600x30 -pointsize 40 caption:{} {}.png +swap -gravity south -composite {}-watermark.png".format(naked_filename, filename, filename)
    print cmd2
    os.system(cmd2)
