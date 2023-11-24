#!/usr/bin/env python3.11

import sys
import argparse

# Handle comandline arguments
parser = argparse.ArgumentParser(description="Create slice of mT basing on submitted trascript_ids.",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("transcipt_ids_path", help="transcript_ids file path")
args = parser.parse_args()
config = vars(args)

# Collect the transcripts_ids from file
transcript_ids = []
with open(config['transcript_ids_path']) as file:
    for line in file.readline():
        transcript_ids.append(line.split()[11].strip('";'))


# Filter out content of masterTable basing on provided transcript_ids
for line in sys.stdin:
    if line[0] != "#":   # If line is not a header do:
        transcript_id = line.split()[11].strip('";')
        if transcript_id in transcript_ids:
            sys.stdout.write(line)
        else:
            pass  
    else:
        sys.stdout.write(line)    # Keep masterTable header lines


