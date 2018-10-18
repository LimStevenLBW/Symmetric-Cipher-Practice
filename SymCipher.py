#Steven Lim
#CECS 378 Symmetric Ciphers

from collections import OrderedDict
from math import log10
import itertools
import string
import random
from random import shuffle
#Method creates an ordered dictionary and pairs the keys with values based on the cipher input
#param - A cipher string
#return - An ordered dictionary containing the alphabet as keys and letter frequencies as values
def letterFreq(cipher):
	freq = OrderedDict.fromkeys(string.ascii_lowercase, 0)
	for letter in cipher:
		keys = freq.keys();
		if letter in keys:
			freq[letter] += 1

	#Sort the dictionary in descending order			
	freq = OrderedDict(sorted(freq.items(), key=lambda t: t[1], reverse = True))
	return freq
	
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
			continue
	return decrypted

#Assembles a dictionary containing quadgrams counts from an enormous set of English words
#The counts are then converted to usable numbers for scoring
def readFile(quadgrams_file):
	quadgramScoreDict = {}
	#Iterates through each line while inserting keys & value pairs into a dictionary
	for line in quadgrams_file:
		key, value = line.split(" ")
		quadgramScoreDict[key] = int(value)
		
	#Totals all the values in the dictionary, itervalues is used to save memory by avoiding the temp list from values()	
	totalValueCount = sum(quadgramScoreDict.itervalues())
	
	#Conversion of counts to scorable values, formula used is (value/total)
	for key in quadgramScoreDict.keys():
		quadgramScoreDict[key] = log10(float(quadgramScoreDict[key])/totalValueCount)
	
	return quadgramScoreDict
	
	
#Method will score a given text using a quadgram analysis, the better the score, the more likely it is to be English
#param - a text to be scored
#return - the calculated score of the text	
def scoreText(text, quadgramScoreDict):
	score = 0
	#Removing whitespace
	text = text.replace(" ", "")

	#Extracts quadgrams from the text and assigns the score
	for i in xrange(len(text)):
		quadgram = ""
		if((i+3) >= len(text)):
			break
		else:
			quadgram += text[i]
			quadgram += text[i+1]
			quadgram += text[i+2]
			quadgram += text[i+3]
			quadgram = quadgram.upper()
			try:
				score += quadgramScoreDict[quadgram]
			except KeyError, e:
				#If not found
				continue
	return score

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
freqEng = ["e", "t", "a", "o", "i", "n", "s", "r", "h", "l", "d", "c", "u", "m", "f", "p", "g", "w", "y", "b", "v", "k", "x", "j", "q", "z"]
#List of Ciphers
cipher_1 = "fqjcb rwjwj vnjax bnkhj whxcq nawjv nfxdu mbvnu ujbbf nnc"
cipher_2 = "oczmz vmzor jocdi bnojv dhvod igdaz admno ojbzo rcvot jprvi oviyv aozmo cvooj ziejt dojig toczr dnzno jahvi fdiyv xcdzq zoczn zxjiy"
cipher_3 = "p spawa qleji taiul rtwll rflrl laoat wsqqj atgac kthls iraoa twlpl qjatw jufrh lhuts qataq itats aittkstqfj cae"
cipher_4 = "hqz ewqin azqej shayz niqbe aheum hnmnj jaqii yuexq ayqkn jbeuq iihed yzhni ifnun sayiz yudhesqshu qesqa iluym qkque aqaqm oejjs hqzyu jdzqa diesh niznj jayzy uiqhq vayzq shsnj jejjz nshnahnmyt isnae sqfun dqzew qiead zevqi zhnjq shqze udqai jrmtq uishq ifnun siiqa suoij qqfni syyle iszhnbhmei squih nimnx hsead shqmr udquq uaqeu iisqe jshnj oihyy snaxs hqihe lsilu ymhni tyz"

quadgrams_file = open("english_quadgrams.txt", "r")
quadgramScoreDict = readFile(quadgrams_file)

#This is a dictionary containing the top ten best scoring keys
bestKeys = {}
score = 0;
msg = ""

#Create dictionary containing frequency analysis results, let's make the first key
freq = letterFreq(cipher_1)
keyDict = OrderedDict(zip(freq.keys(), freqEng))

#This is the initial state of the decryption, the message has the key applied to decrypt
msg = applyKey(cipher_1, keyDict)
score = scoreText(msg, quadgramScoreDict)

#The key used is becomes an alphabet-key in a dictionary and stored with its score
bestKeys[toString(keyDict)] = score

#We will not accept any keys lower than the threshold
minScore = score

#From here on, we will 'step', swapping characters in the key to find the best solution
#Beginning steps
jumpCounter = 0
endCounter = 0

#Implementation of swapping using random choices
while(endCounter < 30000):
	#Swaps 2 random values within the dictionary
	key1, key2 = random.sample(list(keyDict), 2)
	keyDict[key1], keyDict[key2] = keyDict[key2], keyDict[key1]
	
	#Evaluate the key and obtain the score
	msg = applyKey(cipher_1, keyDict)
	print msg
	score = scoreText(msg, quadgramScoreDict)
	print score
	
	#Examine the score, record if a suitable key was found
	if (score > minScore):
		jumpCounter = 0
		alphaKey = toString(keyDict)
		
		#Add the new score
		bestKeys[alphaKey] = score
	
		#Remove the weakest key
		if(len(bestKeys) > 10):
		
			minKey = min(bestKeys, key=bestKeys.get)
			del bestKeys[minKey]
		
		#Calculate the new minimum value
		minKey = min(bestKeys, key=bestKeys.get)
		minScore = bestKeys[minKey]
		
		endCounter = 0
	elif (jumpCounter >= 1000):
		jumpCounter = 0
		#Completely randomize the dictionary for a new starting point
		ascii = list(string.ascii_lowercase)
		#Using random.shuffle
		shuffle(ascii)
		
		keyDict = OrderedDict(zip(string.ascii_lowercase, ascii))
	else:
		endCounter += 1
		jumpCounter += 1
	
	
#Program results are displayed
print "\nThe original text was: " + cipher_1
print "\n The best scores achieved are the decrypted texts...\n"
for key,value in bestKeys.iteritems():
	print "Key used: " + key
	keyDict = OrderedDict.fromkeys(string.ascii_lowercase, 0)
	
	i = 0
	for k in keyDict:
		keyDict[k] = key[i]
		i += 1
	print applyKey(cipher_1, keyDict) 
	print value
	print "\n"

	

"""
#From here on, we will 'step', swapping characters in the key to find the best solution
for p in itertools.permutations(alphaKey):
	newKey = ''.join(p)
	print newKey
	keyDict = OrderedDict.fromkeys(string.ascii_lowercase, 0)
	
	i = 0
	for k in keyDict:
		keyDict[k] = newKey[i]
		i += 1
	
	print " sadas"
	print failCounter
	print keyDict
		
	msg = applyKey(cipher_1, keyDict)
	print msg
	score = scoreText(msg, quadgramScoreDict)
		
	print score
	if(score > bestScore):
		failCounter = 0
		bestScore = score
		bestKey = ''.join(p)
		bestDecryption = msg
			
		print "Decrypted Text = " + bestDecryption
		print bestScore
		print bestKey
			
	else:
		failCounter += 1
		if (failCounter > 100000):
			break


print "\n The best score achieved is the decrypted text\n = " + bestDecryption
print bestScore
print bestKey
"""





