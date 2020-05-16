##################################################################
"""
Function: censorByCount
	Censor text by number of letters in each word.
Inputs:
	- inFileStr: file to be censored
	- numLetters: number of letters each words has to contain to be
				  censored.
Outputs:
	- lineBuffer: Buffer containing all words censored.
"""
##################################################################
def censorByCount(inFileStr, numLetters):
	# Censor text by the number of letters in the word
	inFile = open(inFileStr, "r")
	lineBuffer = []

	for line in inFile.readlines():
		line = processManyWords(line, numLetters)
		lineBuffer.append(line)

	return lineBuffer
#################################################################
"""
Function: censorbyWord
	Censor file by replacing every word specified in censorWordsFile
	with *'s
Inputs:
	- inFileStr: file to be censored
	- censorWordsFile: Bad words to be sensored.
outputs:
	- lineBuffer: Buffer containing all the censored words in file
"""
#################################################################
def censorByWord(inFileStr, censorWordsFile):
	# Censors file by replacing every bad word specified by
	# censorWordsFile with "*"s
	inFile = open(inFileStr, "r")
	wordsFile = open(censorWordsFile, "r")
	badWords = wordsFile.readline().split(" ")
	lineBuffer = []

	for line in inFile.readlines():
		cleanLine = cleanManyWords(line, badWords)
		lineBuffer.append(cleanLine)

	return lineBuffer
#################################################################
"""
Function: censorManyWords
	Censor a sinlge line by replacing every word specified in badWords
	with *'s
Inputs:
	- line: single line to be censored
	- badWords: list containing bad words to be censored in line.
outputs:
	- line: Buffer containing all the censored words in line
"""
#################################################################
def cleanManyWords(line, badWords):
	# Cleans a single line of text by replacing every word if
	# found in badWords with '*'s
	words = line.split(" ")

	for i in range(len(words)):
		word = cleanOneWord(words[i], badWords)
		words[i] = word
	line = " ".join(words)
	return line
#################################################################
"""
Function: cleanOneWord
	Censor a word if found in badWords
Inputs:
	- word: single word to be censored
	- badWords: list containing bad words to be censored in line.
outputs:
	- word: censored word
"""
#################################################################
def cleanOneWord(word, badWords):
	# Clean word if in badWords
	newWord = word.strip('\n')
	newWord = newWord.translate(
		str.maketrans('', '', string.punctuation))
	if newWord in badWords:
		word = replaceWord(word)
	return word
#################################################################
"""
Function: processManyWords
	Splits lines into words and processes words if needed.
Inputs:
	- line: single line to be censored
	- numLetters: integer specifing length of words to censor.
outputs:
	- line: buffer containing all censored words
"""
#################################################################
def processManyWords(line, numLetters):
	# process an entire line. Split into words and processes
	# if needed
	words = line.split(" ")
		
	for i in range(len(words)):
		word = words[i]
		if len(word) > numLetters - 1:
			word = processOneWord(words[i], numLetters)
			words[i] = word
	line = " ".join(words)
	return line
#################################################################
"""
Function: processOneWords
	Processes a single line by removing punctuation and carriage
	returns. Censored if needed. Words is returned with original
	puntuation.
Inputs:
	- word: single word to be censored
	- numLetters: integer specifing length of words to censor.
outputs:
	- word: censored word
"""
#################################################################
def processOneWord(word, numLetters):
	# Process a single word. Remove punctuation and carriage return
	# and process if needed. Returns word censored with original
	# punctuation and carriage return if needed.
	newWord = word.strip('\n')
	newWord = newWord.translate(
		str.maketrans('', '', string.punctuation))
	
	if len(newWord) == numLetters:
		word = replaceWord(word)
	
	return word
#################################################################
"""
Function: replaceWord
	Replaces all letters in word with * and keeps puntuation and
	carriage returns.
Inputs:
	- word: single word to be censored
outputs:
	- word: censored word
"""
#################################################################
def replaceWord(word):
	lastWord = '\n' in word
	word = word.strip('\n')
	letters = list(word)
	for i in range(len(letters)):
		if not letters[i] in string.punctuation:
			letters[i] = '*'
	word = "".join(letters)

	if lastWord: word = word + '\n'

	return word