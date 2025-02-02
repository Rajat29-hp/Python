#!/usr/bin/python3.12

import sys
import argparse

parser = argparse.ArgumentParser(prog="File Reader", description="Read the file")
parser.add_argument("filename",help="the path of the file to read")
parser.add_argument("--limit","-l",type=int,help="limit the lines of file")
parser.add_argument("--version","-v",action="version",version="1.0 by ower",help="check the version")
args = parser.parse_args()

# open file with filename
try:
        f = open(args.filename,"r")
        limit = args.limit
except FileNotFoundError:
        print("File not found. Please check the path.")
        sys.exit(1)
else:
        lines = f.readlines()
        if limit:
                lines = lines[0:limit] #line[0:3]
        for line in lines:
                print(line.strip())
        f.close()
