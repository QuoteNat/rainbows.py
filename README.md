A python rainbow table generator, meant as a way to demonstrate the importance of hashing passwords in databases. 

# INSTRUCTIONS
An example plaintext json file can be found in demoInput:
```json
{
    "accounts": [{
        "username": "alice",
        "password": "password"
    },
    {
        "username": "bob",
        "password": "banana"
    },
    {
        "username": "secure",
        "password": "weoruiqwuoriuqweoifudsf"
    }]
}
```

Command line arguments for the software can be found with the `-h` argument:
```
usage: rainbow.py [-h] [-i INPUT] [-d DICTIONARY] [-ha] [-r] [-n ROUNDS]

options:
  -h, --help            show this help message and exit
  -i INPUT, --Input INPUT
                        Input database file with plaintext passwords for
                        hashing.
  -d DICTIONARY, --Dictionary DICTIONARY
                        File path to the dictionary file used for brute
                        forcing.
  -ha, --Hash           Tells rainbow.py to create a json file with hashed
                        passwords.
  -r, --Rainbow         Tells rainbow.py to attempt to brute force
                        database.json using the provided dictionary.
  -n ROUNDS, --Rounds ROUNDS
                        Number of rounds to use for the hashing algorithm.
```

For brute forcing, you will need to provide your own newline delineated password list. 