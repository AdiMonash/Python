# Student_ID: 29187990
# Name: Aditya Vinod Rane
# Start Date: 28/04/2018
# Last Modified Date: 03/05/2018

class SentenceAnalyser: # defining the class to analyse the sentence
	

	def __init__(self): # initializing the clause, complete and question to 0
		self.dict = {'clause': 0, 'complete': 0, 'question': 0}

	def __str__(self): # defining function to return a string
		temp = ""
		for key in self.dict.keys():
			temp += str(key) + ": " + str(self.dict[key]) + "\n"
		return temp

	def analyse_sentence(self, decoded_sequence): # function to increment the clause, complete and question  
		char_list = list(decoded_sequence)
		for char in char_list:
			if char == ',':
				self.dict['clause'] += 1
			elif char == '.':
				self.dict['complete'] += 1
			elif char == '?':
				self.dict['question'] += 1