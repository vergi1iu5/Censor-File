# censor.py
"""
	This program offers the user a way to censor a file by replacing
	desired words with astericks while ignoring punctuation and assuming
	no words are split between lines. The words can be specified either
	by their letter count (optional input numLetters), or by a file 
	containing the words to censor (optional input censorWords). The
	default option replaces words with 4 letters.
"""
import string
from censor_functions import censorByWord, censorByCount

def main(inFileStr, numLetters = 4, censorWords = "N/A"):
	
	if censorWords == "N/A":
		lineBuffer = censorByCount(inFileStr, numLetters)
	else:
		lineBuffer = censorByWord(inFileStr, censorWords)
	
	outFile = open("censoredFile.txt", "w")

	print("".join(lineBuffer), file = outFile)

	outFile.close()

if __name__ == '__main__':
	# Prompt to setup and call main() if program was not imported 
	# first.
	fileStr = input("Enter file name to censor: ")
	prompt = ''
	while prompt != 'c' or prompt != 'w':
		prompt = input("Censor by count [c], or by word [w]")
		prompt.strip()
	if prompt == 'c':
		n = int(input("Enter letter count to censor: "))
		main(fileStr, numLetters = n)
	else:
		badWordsFile = input("Enter file with words to  censor: ")
		main(fileStr, censorWords = badWords)

