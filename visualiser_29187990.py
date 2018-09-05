# Student_ID: 29187990
# Name: Aditya Vinod Rane
# Start Date: 21/05/2018
# Last Modified Date: 26/05/2018


import pandas as pd
import matplotlib.pyplot as plt

# defining class for visualising the analysis (in bar-graph) which we have done 
class AnalysisVisualiser:
    def __init__(self, all_text_stats):
        self.all_text_stats = all_text_stats


    # function to visualise character
    def visualise_character_frequency(self):
        for i in range(len(self.all_text_stats.columns.tolist())):
            self.all_text_stats.iloc[:, i].plot(kind='bar', legend=False)
            plt.show()

    
    # function to visualise punctuation
    def visualise_punctuation_frequency(self):
        for i in range(len(self.all_text_stats.columns.tolist())):
            self.all_text_stats.iloc[:, i].plot(kind='bar', legend=False)
            plt.show()

    
    # function to visualise stop words
    def visualise_stop_words_frequency(self):
        for i in range(len(self.all_text_stats.columns.tolist())):
            self.all_text_stats.iloc[:, i].plot(kind='bar', legend=False)
            plt.show()

    
    # function to visualise word length
    def visualise_word_length_frequency(self):
        for i in range(len(self.all_text_stats.columns.tolist())):
            self.all_text_stats.iloc[:, i].plot(kind='bar', legend=False)
            plt.show()
