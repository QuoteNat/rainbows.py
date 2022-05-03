# For hashing
import hashlib
# For databases
import json
# For commandline args
import sys
import argparse

# Get command line arguments
inputFilePath = ""

parser = argparse.ArgumentParser()

# Add arguments
parser.add_argument("-i", "--Input", help = "Input database file with plaintext passwords")
args = parser.parse_args()

if args.Input:
    inputFilePath = args.Input
    print("Inputted " + args.Input)
else:
    inputFilePath = "input.json"
    print("No input provided, defaulting to input.json")

