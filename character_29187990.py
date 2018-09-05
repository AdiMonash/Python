# Student_ID: 29187990
# Name: Aditya Vinod Rane
# Start Date: 21/04/2018
# Last Modified Date: 03/05/2018

import re # importing regular expression as we will have to use it to find the matching character

class CharacterAnalyser(object): # defining class to analyse the character
	

	def __init__(self): # function to define dictionary for alphabet and numbers and their count
		self.dict = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0,'G': 0,'H': 0,'I': 0,'J': 0, 'K': 0, 'L': 0,'M': 0,'N': 0,'O': 0,'P': 0,'Q': 0,'R': 0,
		'S': 0,'T': 0,'U': 0,'V': 0,'W': 0,'X': 0,'Y': 0,'Z': 0,'0': 0, '1': 0,'2': 0,'3': 0,'4': 0,'5': 0,'6': 0,'7': 0,'8': 0,'9': 0}

	def __str__(self): # defining function to return a string
		temp = ""
		for key in self.dict.keys():
			temp += str(key) + ": " + str(self.dict[key]) + "\n"
		return temp

	def analyse_characters(self, decoded_sequence): # function to increment the character if found in the above dictionary 
		character_list = list(decoded_sequence.upper())
		for char in character_list:
			if re.match("[A-Z0-9]", char): # use of regular expression to find the matching character and hence to increment it
				self.dict[char] += 1


