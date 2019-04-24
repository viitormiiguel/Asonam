import ijson
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from datetime import datetime
from langdetect import detect
import os
import csv
import pandas as pd 


analyser = SentimentIntensityAnalyzer()

aquaman = "C:\\Users\\vitor\\Documents\\Python Projetcs\\AnalysisMoviews\\Data\\aquaman-tweets\\aquaman\\"
captain = "C:\\Users\\vitor\\Documents\\Python Projetcs\\AnalysisMoviews\\Data\\captain-tweets\\"
avengers = "Data/avengers-tweets/no_war/"

def print_sentiment_scores(sentence):
    snt = analyser.polarity_scores(sentence)
    if snt['compound'] < -0.5:
        classific = '--'
    elif snt['compound'] >= -0.5 and snt['compound'] < -0.1:
        classific = '-'
    elif snt['compound'] >= -0.1 and snt['compound'] <= 0.1:
        classific = '0'
    elif snt['compound'] > 0.1 and snt['compound'] <= 0.5:
        classific = '+'
    elif snt['compound'] > 0.5:
        classific = '++'
    
    return str(classific), str(sentence), str(snt['compound'])


def getYoutube(path, arquivo, name):
    with open (path + arquivo, 'r') as f:
        t = json.load(f)
    with open(path + 'result_' + name + '_youtube' + '.csv', mode='w', encoding="utf8") as fc:
        for texto in t:
            try:
                x = 'null'
                if texto[1]:
                    x = print_sentiment_scores(texto[1])
                    aux = '"%s","%s","%s","%s"\n' % (texto[0],x[0],x[1],x[2]) 
                    fc.write(aux)                    
            except IndexError:
                x = 'null'
            

# getYoutube(aquaman, 'json_youtube_aquamen_com.json', 'aquaman')
# getYoutube(captain, 'json_youtube_captain_com.json', 'captain')
getYoutube(avengers, 'json_youtube_avengers_com.json', 'avengers')
