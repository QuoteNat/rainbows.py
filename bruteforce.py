# For databases
import json
# For hashing
import hashlib

# Reads and filters a dictionary database
def readDictionary(dictionaryFile):
    dictionary = []
    for line in dictionaryFile:
        line = line.strip()
        dictionary.append(line)
    
    return dictionary

def bruteforce(inputFilePath, dictionaryFilePath, outputFilePath, rounds):
    # open all the needed files
    databaseFile = 0
    dictionaryFile = 0
    outputFile = 0
    try:
        databaseFile = open(inputFilePath)
    except FileNotFoundError:
        quit("Database file \"" + inputFilePath + "\" was not found. Exiting...")
    
    try:
        dictionaryFile = open(dictionaryFilePath)
    except FileNotFoundError:
        quit("Dictionary file \"" + dictionaryFilePath + "\" was not found. Exiting...")
    
    outputFile = open(outputFilePath, "w")
    
    # load the database
    database = json.loads(databaseFile.read())
    # read in the dictionary
    dictionary = readDictionary(dictionaryFile)
    for word in dictionary:
        for account in database["accounts"]:
            hash = hashlib.sha256(hashlib.pbkdf2_hmac('sha256', word.encode(), account["salt"].encode(), rounds)).hexdigest()
            if hash == account["hash"]:
                print(account["username"] + "'s password is " + word)
                outputFile.write(account["username"] + " " + word + "\n")
