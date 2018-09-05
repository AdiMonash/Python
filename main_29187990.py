# Student_ID: 29187990
# Name: Aditya Vinod Rane
# Start Date: 22/05/2018
# Last Modified Date: 26/05/2018

# importing all the classes in main
import preprocessor_29187990
import character_29187990
import WordAnalyser_29187990
import visualiser_29187990
import glob
import pandas as pd
import os


# read the input file fo all the writters given 
def read_input():
    Content = []
    path = 'content/*.tok'
    files = glob.glob(path)
    for file in files:
        f = open(file, 'r')
        Content.append(f.read().upper())
        f.close()
    return Content

# defining the main function for execution of all the 4 tasks 
def main():
    PrePro = preprocessor_29187990.Preprocessor()
    Cha = character_29187990.AnalyseCharacters()
    WA = WordAnalyser_29187990.WordAnalyser()
    

    Content = read_input()
    Alphabets_df = pd.DataFrame()
    Punctuation_df = pd.DataFrame()
    Stop_Word_df = pd.DataFrame()
    Word_Length_df = pd.DataFrame()

    for i in range(len(Content)):
        PrePro.tokenise(Content[i])
        Tokens = PrePro.get_tokenised_list()
        Cha.analyse_characters(Tokens)
        WA.analyse_words(Tokens)
        Character_df = Cha.get_alpha_frequency().T
        Character_df.columns = [i]
        Pun_df = Cha.get_punctuation_frequency().T
        Pun_df.columns = [i]
        Stop_df = WA.get_stopword_frequency().T
        Stop_df.columns = [i]
        Word_df = WA.get_word_length_frequency().T
        Word_df.columns = [i]
        Alphabets_df = pd.concat([Alphabets_df, Character_df], axis=1)
        Alphabets_df.fillna(0, inplace=True)
        Punctuation_df = pd.concat([Punctuation_df, Pun_df], axis=1)
        Punctuation_df.fillna(0, inplace=True)
        Stop_Word_df = pd.concat([Stop_Word_df, Stop_df], axis=1)
        Stop_Word_df.fillna(0, inplace=True)
        Word_Length_df = pd.concat([Word_Length_df, Word_df], axis=1)
        Word_Length_df.fillna(0, inplace=True)

    av = visualiser_29187990.AnalysisVisualiser(Alphabets_df)
    av.visualise_character_frequency()
    av2 = visualiser_29187990.AnalysisVisualiser(Punctuation_df)
    av2.visualise_punctuation_frequency()
    av3 = visualiser_29187990.AnalysisVisualiser(Stop_Word_df)
    av3.visualise_stop_words_frequency()
    av4 = visualiser_29187990.AnalysisVisualiser(Word_Length_df)
    av4.visualise_word_length_frequency()


if __name__ == "__main__":
    main()
