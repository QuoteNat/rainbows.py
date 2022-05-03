# For hashing
import hashlib
# For databases
import json
# For commandline args
import argparse

# Get command line arguments
inputFilePath = ""
outputFilePath = "database.json"
salt = "noSaltYet :)"

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

# open the plaintext file as read only
plaintextFile = open(inputFilePath)
# read it into a dictionary
plaintext = json.loads(plaintextFile.read())
print(json.dumps(plaintext, indent=2))

# hashed dictionary
hashed = {
    "accounts": []
}
hashedTemplate = {
        "username": "",
        "salt": "",
        "hash": ""
}

# for each account in accounts
for account in plaintext["accounts"]:
    newAccount = hashedTemplate.copy()
    newAccount["username"] = account["username"]
    newAccount["salt"] = salt
    # hash the plaintext password NOTE: This configuration is insecure for testing purposes
    hash = hashlib.sha256(hashlib.pbkdf2_hmac('sha256', account["password"].encode(), salt.encode(), 1)).hexdigest()
    newAccount["hash"] = hash
    # append the hashed account to hashed
    hashed["accounts"].append(newAccount)

# output hashed to the output json file
hashedJson = json.dumps(hashed, indent=2)
print(hashedJson)

outputFile = open(outputFilePath, "w")
outputFile.write(json.dumps(hashed, indent=2))