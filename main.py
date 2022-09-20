import numpy as np
import pandas as pd
from textblob import TextBlob
import nltk

f = open('1957-Eisenhower.txt', 'r')
speech = f.read()

speechBlob = TextBlob(speech)
words = speechBlob.words
tags = speechBlob.tags
sentences = speechBlob.sentences
paragraphs = (len(sentences) / 5)

one = 0
two = 0

# Calculations Section
########################################################################
i = 0
while True:
    try:
        input = sentences[i][0]
        i = i + 1
        if (input.isupper()):
            one = one + 1
        elif (input.islower()):
            two = two + 1
    except:
        break
#########################################################################
i = 0
sum = 0
while True:
    try:
        sum = sum + len(words[i])
        i = i + 1
    except:
        break
averageWLength = sum / len(words)


#########################################################################
def checker(input):
    try:
        df = pd.DataFrame(speechBlob, columns=['let'])
        return df['let'].value_counts()[input]
    except:
        return 0


three = len(words)
four = averageWLength.__round__()
five = len(speechBlob.sentences)
six = (len(words) / len(sentences)).__round__()
seven = paragraphs.__round__()
eight = (len(words) / paragraphs).__round__()
nine = checker('!')
ten = checker('#')
eleven = checker('$')
twelve = checker('&')
thirteen = checker('%')
fourteen = checker('\'')
fifteen = checker('(')
sixteen = checker(')')
seventeen = checker('*')
eighteen = checker('+')
nineteen = checker(',')
twenty = checker('-')

ans = {'Questions': ["Number of sentences beginning with upper case: ", "Number of sentences beginning with lower case: ", "Number of Words: ", "Average Word Length: ", "Number of Sentences: ", "Average Number of Words per Sentence: ", "Number of Paragraphs: ", "Average Number of words per Paragraph: ", "Number of Exclamation Marks: ", "Number of Number Signs: ", "Number of Dollar Signs: ", "Number of Ampersands: ", "Number of Percent Signs: ", "Number of Apostrophes: ", "Number of Left parentheses: ", "Number of Right parentheses: ", "Number of Asterisks: ", "Number of Plus Signs: ", "Number of Commas: ", "Number of Dashes: "],
       'Answers': [one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty]}

df2 = pd.DataFrame.from_dict(ans)

print(df2)
