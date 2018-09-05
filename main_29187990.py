# Student_ID: 29187990
# Name: Aditya Vinod Rane
# Start Date: 28/04/2018
# Last Modified Date: 03/05/2018


# importing all the classes to main function
de = __import__('decoder_29187990')
ca = __import__('character_29187990')
wa = __import__('word_29187990')
sa = __import__('sentence_29187990')

def main():
	# creating the instance of all classes
	dec = de.Decoder()
	cha = ca.CharacterAnalyser()
	word = wa.WordAnalyser()
	sent = sa.SentenceAnalyser()


	false_input = False
	morse_list=[]
	while True: # Taking input from user
		false_input = False
		sentence = input("Enter MorseCode:")
    
    	# Quit statement
		if (sentence == 'quit'):
			print("Exit from the code.....")
			break
    
    	# Accepting Morse characters 
		elif(len(sentence) >= 1):
			for char in sentence:
				if (char not in ['0', '1', '*']):
					false_input = True
					print("Wrong input: ")
					break
			if not false_input:
				morse_list.append(sentence)
				false_input = False

	decoded = []
	for seq in morse_list: # to print the decoded code
		decoded.append(dec.decode(seq))
		print(dec.decode(seq))

	for item in decoded: # to analyse the character and increment it 
		cha.analyse_characters(item)
		print(str(cha))

	for item in decoded: # to analyse the words and increment it
		word.analyse_words(item)
		print(str(word))

	for item in decoded: # to analyse the sentence and increment it
		sent.analyse_sentence(item)
		print(str(sent))




if __name__ == "__main__":
	main()

