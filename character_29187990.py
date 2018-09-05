
# Student_ID: 29187990
# Name: Aditya Vinod Rane
# Start Date: 16/05/2018
# Last Modified Date: 26/05/2018

import pandas as pd
import re

# defining class to analyse the number of occurrences of each character with the help of dataframe
class AnalyseCharacters:
    def __init__(self):
        self.Character = pd.DataFrame()

    def __str__(self):
        return ""

    
    # function to add Characters to dataframe
    def analyse_characters(self, tokenised_list):
        for token in tokenised_list:
            Character_Array = list(token.upper())
            for char in Character_Array:
                if char in self.Character.columns:
                    val = self.Character[char].tolist()
                    self.Character[char] = val[0] + 1
                else:
                    self.Character[char] = [1]


    
    # function to get punctuation frequency
    def get_punctuation_frequency(self):
        Punctuation = pd.DataFrame()
        chars = self.Character.columns.tolist()
        for char in chars:
            if not re.match("[A-Z0-9]", char):
                Punctuation[char] = self.Character[char]
        return Punctuation

    

    # function to get character frequency
    def get_alpha_frequency(self):
        Alphabets = pd.DataFrame()
        chars = self.Character.columns.tolist()
        for char in chars:
            if re.match("[A-Z0-9]", char):
                Alphabets[char] = self.Character[char]
        return Alphabets




