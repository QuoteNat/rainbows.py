from hasher import createHashedDatabase
# For commandline args
import argparse

# Get command line arguments
inputFilePath = ""
dictionaryFilePath = ""
outputFilePath = "database.json"

parser = argparse.ArgumentParser()

# Add arguments
parser.add_argument("-i", "--Input", help = "Input database file with plaintext passwords for hashing, or hashed password for brute forcing")
parser.add_argument("-d", "--Dictionary", help = "File path to the dictionary file used for a dictionary attack")
# Add arguments
parser.add_argument("-ha", "--Hash", help = "Tells rainbow.py to create a hashed password json file, if both this", action="store_true")
parser.add_argument("-r", "--Rainbow", help = "Tells rainbow.py to attempt to brute force database.json using the provided dicitonary", action="store_true")
args = parser.parse_args()

if args.Input:
    inputFilePath = args.Input
    print("Inputted " + args.Input)
else:
    inputFilePath = "input.json"
    print("No input provided, defaulting to input.json")

if args.Dictionary:
    dictionaryFilePath = args.Dictionary
    print("Inputted " + args.Dictionary + " as dictionary")
if args.Hash:
    createHashedDatabase(inputFilePath, outputFilePath)

