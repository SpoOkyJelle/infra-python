import os 
import hashlib
import sys



# We voegen een salt toe om het brute forcen van het wachtwoord lastiger te maken.
salt = os.urandom(32)
# Het wachtwoord dat versleuteld wordt 
print('Enter password:')
password = input()

# Maak een key voor het versleutelen van het wachtwoord
key = hashlib.pbkdf2_hmac(
    'sha256',
    password.encode('utf-8'), # Zet het wachtwoord over naar bytes
    salt, # Voeg de salt toe
    100000, # Het aantal iteraties van utf-8 die over het wachtwoord gaan
    dklen=128 # vraag een 128 byte key
)

# print de key
print(key)


