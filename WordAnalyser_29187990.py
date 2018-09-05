# Student_ID: 29187990
# Name: Aditya Vinod Rane
# Start Date: 19/05/2018
# Last Modified Date: 26/05/2018


import pandas as pd


# defining a class to analyse the number of occurrences for each word
class WordAnalyser:
    def __init__(self):
        self.Words = pd.DataFrame()
        self.Stop_Words = ['A', 'ABOUT', 'ABOVE', 'ACROSS', 'AFTER', 'AGAIN', 'AGAINST', 'ALL', 'ALMOST', 'ALONE', 'ALONG', 'ALREADY', 'ALSO', 'ALTHOUGH', 'ALWAYS', 'AMONG', 'AN', 'AND', 'ANOTHER', 'ANY', 'ANYBODY', 'ANYONE', 'ANYTHING', 'ANYWHERE', 'ARE', 'AREA', 'AREAS', 'AROUND', 'AS', 'ASK', 'ASKED', 'ASKING', 'ASKS', 'AT', 'AWAY', 'B', 'BACK', 'BACKED', 'BACKING', 'BACKS', 'BE', 'BECAME', 'BECAUSE', 'BECOME', 'BECOMES', 'BEEN', 'BEFORE', 'BEGAN', 'BEHIND', 'BEING', 'BEINGS', 'BEST', 'BETTER', 'BETWEEN', 'BIG', 'BOTH', 'BUT', 'BY', 'C', 'CAME', 'CAN', 'CANNOT', 'CASE', 'CASES', 'CERTAIN', 'CERTAINLY', 'CLEAR', 'CLEARLY', 'COME', 'COULD', 'D', 'DID', 'DIFFER', 'DIFFERENT', 'DIFFERENTLY', 'DO', 'DOES', 'DONE', 'DOWN', 'DOWN', 'DOWNED', 'DOWNING', 'DOWNS', 'DURING', 'E', 'EACH', 'EARLY', 'EITHER', 'END', 'ENDED', 'ENDING', 'ENDS', 'ENOUGH', 'EVEN', 'EVENLY', 'EVER', 'EVERY', 'EVERYBODY', 'EVERYONE', 'EVERYTHING', 'EVERYWHERE', 'F', 'FACE', 'FACES', 'FACT', 'FACTS', 'FAR', 'FELT', 'FEW', 'FIND', 'FINDS', 'FIRST', 'FOR', 'FOUR', 'FROM', 'FULL', 'FULLY', 'FURTHER', 'FURTHERED', 'FURTHERING', 'FURTHERS', 'G', 'GAVE', 'GENERAL', 'GENERALLY', 'GET', 'GETS', 'GIVE', 'GIVEN', 'GIVES', 'GO', 'GOING', 'GOOD', 'GOODS', 'GOT', 'GREAT', 'GREATER', 'GREATEST', 'GROUP', 'GROUPED', 'GROUPING', 'GROUPS', 'H', 'HAD', 'HAS', 'HAVE', 'HAVING', 'HE', 'HER', 'HERE', 'HERSELF', 'HIGH', 'HIGH', 'HIGH', 'HIGHER', 'HIGHEST', 'HIM', 'HIMSELF', 'HIS', 'HOW', 'HOWEVER', 'I', 'IF', 'IMPORTANT', 'IN', 'INTEREST', 'INTERESTED', 'INTERESTING', 'INTERESTS', 'INTO', 'IS', 'IT', 'ITS', 'ITSELF', 'J', 'JUST', 'K', 'KEEP', 'KEEPS', 'KIND', 'KNEW', 'KNOW', 'KNOWN', 'KNOWS', 'L', 'LARGE', 'LARGELY', 'LAST', 'LATER', 'LATEST', 'LEAST', 'LESS', 'LET', 'LETS', 'LIKE', 'LIKELY', 'LONG', 'LONGER', 'LONGEST', 'M', 'MADE', 'MAKE', 'MAKING', 'MAN', 'MANY', 'MAY', 'ME', 'MEMBER', 'MEMBERS', 'MEN', 'MIGHT', 'MORE', 'MOST',
                           'MOSTLY', 'MR', 'MRS', 'MUCH', 'MUST', 'MY', 'MYSELF', 'N', 'NECESSARY', 'NEED', 'NEEDED', 'NEEDING', 'NEEDS', 'NEVER', 'NEW', 'NEW', 'NEWER', 'NEWEST', 'NEXT', 'NO', 'NOBODY', 'NON', 'NOONE', 'NOT', 'NOTHING', 'NOW', 'NOWHERE', 'NUMBER', 'NUMBERS', 'O', 'OF', 'OFF', 'OFTEN', 'OLD', 'OLDER', 'OLDEST', 'ON', 'ONCE', 'ONE', 'ONLY', 'OPEN', 'OPENED', 'OPENING', 'OPENS', 'OR', 'ORDER', 'ORDERED', 'ORDERING', 'ORDERS', 'OTHER', 'OTHERS', 'OUR', 'OUT', 'OVER', 'P', 'PART', 'PARTED', 'PARTING', 'PARTS', 'PER', 'PERHAPS', 'PLACE', 'PLACES', 'POINT', 'POINTED', 'POINTING', 'POINTS', 'POSSIBLE', 'PRESENT', 'PRESENTED', 'PRESENTING', 'PRESENTS', 'PROBLEM', 'PROBLEMS', 'PUT', 'PUTS', 'Q', 'QUITE', 'R', 'RATHER', 'REALLY', 'RIGHT', 'RIGHT', 'ROOM', 'ROOMS', 'S', 'SAID', 'SAME', 'SAW', 'SAY', 'SAYS', 'SECOND', 'SECONDS', 'SEE', 'SEEM', 'SEEMED', 'SEEMING', 'SEEMS', 'SEES', 'SEVERAL', 'SHALL', 'SHE', 'SHOULD', 'SHOW', 'SHOWED', 'SHOWING', 'SHOWS', 'SIDE', 'SIDES', 'SINCE', 'SMALL', 'SMALLER', 'SMALLEST', 'SO', 'SOME', 'SOMEBODY', 'SOMEONE', 'SOMETHING', 'SOMEWHERE', 'STATE', 'STATES', 'STILL', 'STILL', 'SUCH', 'SURE', 'T', 'TAKE', 'TAKEN', 'THAN', 'THAT', 'THE', 'THEIR', 'THEM', 'THEN', 'THERE', 'THEREFORE', 'THESE', 'THEY', 'THING', 'THINGS', 'THINK', 'THINKS', 'THIS', 'THOSE', 'THOUGH', 'THOUGHT', 'THOUGHTS', 'THREE', 'THROUGH', 'THUS', 'TO', 'TODAY', 'TOGETHER', 'TOO', 'TOOK', 'TOWARD', 'TURN', 'TURNED', 'TURNING', 'TURNS', 'TWO', 'U', 'UNDER', 'UNTIL', 'UP', 'UPON', 'US', 'USE', 'USED', 'USES', 'V', 'VERY', 'W', 'WANT', 'WANTED', 'WANTING', 'WANTS', 'WAS', 'WAY', 'WAYS', 'WE', 'WELL', 'WELLS', 'WENT', 'WERE', 'WHAT', 'WHEN', 'WHERE', 'WHETHER', 'WHICH', 'WHILE', 'WHO', 'WHOLE', 'WHOSE', 'WHY', 'WILL', 'WITH', 'WITHIN', 'WITHOUT', 'WORK', 'WORKED', 'WORKING', 'WORKS', 'WOULD', 'X', 'Y', 'YEAR', 'YEARS', 'YET', 'YOU', 'YOUNG', 'YOUNGER', 'YOUNGEST', 'YOUR', 'YOURS', 'Z']

    def __str__(self):
        return ""

    #function to analyse words and find their frequency
    def analyse_words(self, tokenised_list):
        for word in tokenised_list:
            word = word.upper()
            if word in self.Words.columns:
                val = self.Words[word].tolist()
                self.Words[word] = val[0] + 1
            else:
                self.Words[word] = [1]


    #function to get stopword frequency
    def get_stopword_frequency(self):
        All_Words = self.Words.columns.tolist()
        Stop_Words_df = pd.DataFrame()
        for word in All_Words:
            if word in self.Stop_Words:
                Stop_Words_df[word] = self.Words[word].tolist()
        return Stop_Words_df


    #function to get word length frequency
    def get_word_length_frequency(self):
        All_The_Words = self.Words.columns.tolist()
        Word_Length_df = pd.DataFrame()
        for word in All_The_Words:
            Word_Length = len(word)
            if Word_Length in Word_Length_df.columns:
                val = Word_Length_df[Word_Length].tolist()
                Word_Length_df[Word_Length] = val[0] + 1
            else:
                Word_Length_df[Word_Length] = [1]
        return Word_Length_df



