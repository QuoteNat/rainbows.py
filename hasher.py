# For databases
import json
# For hashing
import hashlib
# For random strings
import random
# For timing functions
import timeit

salt = "noSaltYet :)"

CHAR_LIMIT = 255

# Generates a random 10 character string
def randString():
    randString = ""
    for _ in range(10):
        # pick a random number between 0 and 255
        randomInteger = random.randint(0, CHAR_LIMIT)
        # add random integer as a character to randString
        randString += (chr(randomInteger))
    return randString

def createHashedDatabase(inputFilePath, outputFilePath, rounds):
    start = timeit.default_timer()
    # open the plaintext file as read only
    try:
        plaintextFile = open(inputFilePath)
    except FileNotFoundError:
        quit("Inputted file \"" + inputFilePath + "\" was not found. Exiting...")

    # read it into a dictionary
    plaintext = json.loads(plaintextFile.read())

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
        # generate the random salt
        salt = randString()
        newAccount = hashedTemplate.copy()
        newAccount["username"] = account["username"]
        newAccount["salt"] = salt
        # hash the plaintext password NOTE: This configuration is insecure for testing purposes
        hash = hashlib.sha256(hashlib.pbkdf2_hmac('sha256', account["password"].encode(), salt.encode(), rounds)).hexdigest()
        newAccount["hash"] = hash
        # append the hashed account to hashed
        hashed["accounts"].append(newAccount)

    outputFile = open(outputFilePath, "w")
    outputFile.write(json.dumps(hashed, indent=2))

    stop = timeit.default_timer()
    print("Hashing the plaintext database took " + "{0:.5g}".format(stop-start) + " seconds for " + str(len(plaintext["accounts"])) + " accounts.")