# For databases
import json
# For hashing
import hashlib

salt = "noSaltYet :)"

def createHashedDatabase(inputFilePath, outputFilePath):
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
        newAccount = hashedTemplate.copy()
        newAccount["username"] = account["username"]
        newAccount["salt"] = salt
        # hash the plaintext password NOTE: This configuration is insecure for testing purposes
        hash = hashlib.sha256(hashlib.pbkdf2_hmac('sha256', account["password"].encode(), salt.encode(), 1)).hexdigest()
        newAccount["hash"] = hash
        # append the hashed account to hashed
        hashed["accounts"].append(newAccount)

    outputFile = open(outputFilePath, "w")
    outputFile.write(json.dumps(hashed, indent=2))