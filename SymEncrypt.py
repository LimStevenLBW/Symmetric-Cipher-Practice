#Steven Lim
#CECS 378 Symmetric Ciphers
#Encrypting Plaintexts

from collections import OrderedDict
import string
import random
from random import shuffle
	
#Method applies a decryption key to the cipher performing substitution, character by character
#param - A cipher string and a dictionary key to use
#return - The resultant text
def applyKey(cipher, keyDict):
	decrypted = ""
	for char in cipher:
		try:
			decrypted += keyDict[char];
		except KeyError, e:
			decrypted += " "
	return decrypted

#Formats the dictionary key into a key-alphabet string
#param - the dictionary to process
#return - the newly formatted key
def toString(key):
	formattedKey = ""
	key = OrderedDict(sorted(key.items(), key=lambda t: t[0]))
	
	for value in key.values():
		formattedKey += value
	return formattedKey
	


#-----------  Begin Main Process  ------------

plainText1 = "He who fights with monsters should look to it that he himself does not become a monster. And if you gaze long into an abyss, the abyss also gazes into you"
plainText2 = "There is a theory which states that if ever anybody discovers exactly what the Universe is for and why it is here, it will instantly disappear and be replaced by something even more bizarre and inexplicable.There is another theory which states that this has already happened"
plainText3 = "Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people's hats off--then, I account it high time to get to sea as soon as I can"

#Convert the all characters to lowercase
plainText1 = plainText1.lower()
plainText2 = plainText2.lower()
plainText3 = plainText3.lower()

#For each plaintext, we generate a new dictionary with randomly shuffled letter values from the alphabet
ascii = list(string.ascii_lowercase)
shuffle(ascii)

EncryptionKey1 = OrderedDict(zip(string.ascii_lowercase, ascii))
AlphaKey1 = toString(EncryptionKey1)

shuffle(ascii)

EncryptionKey2 = OrderedDict(zip(string.ascii_lowercase, ascii))
AlphaKey2 = toString(EncryptionKey2)

shuffle(ascii)

EncryptionKey3 = OrderedDict(zip(string.ascii_lowercase, ascii))
AlphaKey3 = toString(EncryptionKey3)

Cipher1 = applyKey(plainText1, EncryptionKey1)
Cipher2 = applyKey(plainText2, EncryptionKey2)
Cipher3 = applyKey(plainText3, EncryptionKey3)

BasicAlphabet = newKey = ''.join(EncryptionKey1.keys())

print "\nFirst Text: " + plainText1
print "Alphabet: " + BasicAlphabet
print "New Key:  " + AlphaKey1
print "Encoded: " + Cipher1
print "\n"

print "Second Text: " + plainText2
print "Alphabet: " + BasicAlphabet
print "New Key : " + AlphaKey2
print "Encoded: " + Cipher2
print "\n"


print "Third Text: " + plainText3
print "Alphabet: " + BasicAlphabet
print "New Key : " + AlphaKey3
print "Encoded: " + Cipher3
print "\n"





