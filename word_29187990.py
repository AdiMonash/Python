# Student_ID: 29187990
# Name: Aditya Vinod Rane
# Start Date: 25/04/2018
# Last Modified Date: 03/05/2018

import re # importing regular expression as we will have to use it to find the matching character

class WordAnalyser: # defining class to analyse word
	

	def __init__(self): # function to take empty dictionary 
		self.dict = {}

	def __str__(self): # defining function to return a string
		temp = ""
		for key in self.dict.keys():
			temp += str(key) + ": " + str(self.dict[key]) + "\n"
		return temp

	def analyse_words(self, decoded_sequence): # function to increment the word count
		words = decoded_sequence.split() # split function to split the word and hence to increment the count properly
		for word in words:
			if re.match("^[A-Za-z]*$", word) or re.match("^[0-9]*$", word): # use of regular expression to find the matching character and hence to increment it
				if word in self.dict:
					self.dict[word] += 1
				else:
					self.dict[word] = 1
			elif re.match("^[A-Za-z]+?$", word) or re.match("^[A-Za-z]+,$", word) or re.match("^[A-Za-z]+.$", word): # filter words followed by puncation without any space between them
				word = word[:-1] # catches where it finds first word and it will increment it to word count
				if word in self.dict:
					self.dict[word] += 1
				else:
					self.dict[word] = 1
