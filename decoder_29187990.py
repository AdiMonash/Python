# Student_ID: 29187990
# Name: Aditya Vinod Rane
# Start Date: 20/04/2018
# Last Modified Date: 03/05/2018

class Decoder(object): # defining the class to decode 


	def __init__(self): # initializing the dictionary
		self.dict = {'01' : 'A','1000' : 'B','1010' : 'C','100' : 'D','0' : 'E','0010' : 'F','110' : 'G','0000' : 'H',
		'00' : 'I','0111' : 'J','101' : 'K','0100' : 'L','11' : 'M','10' : 'N','111' : 'O','0110' : 'P',
		'1101' : 'Q','010' : 'R','000' : 'S','1' : 'T','001' : 'U','0001' : 'V','011' : 'W','1001' : 'X',
		'1011' : 'Y','1100' : 'Z','11111' : '0','01111' : '1','00111' : '2','00011' : '3','00001' : '4',
		'00000' : '5','10000' : '6','11000' : '7','11100' : '8','11110' : '9','010101':'.','110011':',','001100':'?'}


	def __str__(self): # defining function to return a string 
		temp = ""
		for key in self.dict.keys():
			temp += str(key) + ": " + str(self.dict[key]) + "\n"
		return temp

	def decode(self, morse_code_sequence): # function to take input from user
		decodedsentence = ''
		space_occured = 0
		line = morse_code_sequence.split('*')
		for numbers in line:
			if type(numbers) != None and numbers != '':
				decodedsentence += self.dict.get(numbers)
			elif numbers == '' and space_occured == 0:
				space_occured = 1
			elif numbers == '' and space_occured == 1:
				decodedsentence += ' '
				space_occured = 0
		#if line = morse_code_sequence.split('***'):
		#	print(" ")
		return decodedsentence




