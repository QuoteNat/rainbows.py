from hasher import createHashedDatabase
from bruteforce import bruteforce
# For commandline args
import argparse

# Get command line arguments
inputFilePath = ""
dictionaryFilePath = ""
outputFilePath = "database.json"
rounds = 1

parser = argparse.ArgumentParser()

# Add arguments
parser.add_argument("-i", "--Input", help = "Input database file with plaintext passwords for hashing, or hashed password for brute forcing")
parser.add_argument("-d", "--Dictionary", help = "File path to the dictionary file used for a dictionary attack")
# Add arguments
parser.add_argument("-ha", "--Hash", help = "Tells rainbow.py to create a hashed password json file, if both this", action="store_true")
parser.add_argument("-r", "--Rainbow", help = "Tells rainbow.py to attempt to brute force database.json using the provided dicitonary", action="store_true")
parser.add_argument("-n", "--Rounds", help="Number of rounds to use for the hashing algorithm.")
args = parser.parse_args()

if args.Input:
    inputFilePath = args.Input
    print("Inputted " + args.Input)
else:
    inputFilePath = "input.json"
    print("No input provided, defaulting to input.json")

if args.Dictionary:
    dictionaryFilePath = args.Dictionary
    print("Inputted " + args.Input)
else:
    dictionaryFilePath = "dictionary.txt"
    print("No dictionary provided, defaulting to dictionary.txt")

# make sure the user hasn't entered 0 or negative rounds of hashing
if args.Rounds and int(args.Rounds) > 0:
    rounds = int(args.Rounds)

if args.Hash:
    createHashedDatabase(inputFilePath, outputFilePath, rounds)

if args.Rainbow:
    bruteforce("database.json", dictionaryFilePath, "pwned.txt", rounds)
