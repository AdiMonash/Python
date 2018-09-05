# Student_ID: 29187990
# Name: Aditya Vinod Rane
# Start Date: 14/05/2018
# Last Modified Date: 26/05/2018

# defining a class to perform basic preprocessing of each input text
class Preprocessor:
    

    def __init__(self):
        self.Tokens = []

    
    # overwrite str function to display the token list
    def __str__(self): 
        temp = ""
        temp += "Token Numbers: %d" % len(self.Tokens)
        return temp

    
    # function to tokenise the input sentence.
    def tokenise(self, input_sequence):
        Tokens = input_sequence.split()
        for token in Tokens:
            self.Tokens.append(token)

    # function to return tokenised list
    def get_tokenised_list(self):
        return self.Tokens


