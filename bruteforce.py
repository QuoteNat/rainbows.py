# For databases
import json
# For hashing
import hashlib
# For run time timing
import timeit

# Reads and filters a dictionary database
def readDictionary(dictionaryFile):
    """Reads the dictionary file into an array.
    
    dictionaryFile: File path to the dictionary
    """
    dictionary = []
    for line in dictionaryFile:
        line = line.strip()
        dictionary.append(line)
    
    return dictionary

def bruteforce(inputFilePath, dictionaryFilePath, outputFilePath, rounds):
    """Attempts to brute force a hashed password database using a provided dictionary.

    Arguments:
    inputFilePath: path to the database
    dictionaryFilePath: path to the dictionary
    outputFilePath: file to write brute forced passwords to
    rounds: number of rounds to use when hashing
    """
    start = timeit.default_timer()
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
                # Stop attempting to brute force account by removing it from the list
                database["accounts"].remove(account)

    stop = timeit.default_timer()
    print("Brute forcing the hashed passwords took " + "{0:.5g}".format(stop-start) + " seconds for " + str(len(database["accounts"])) + " accounts.")