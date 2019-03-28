import ijson
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from datetime import datetime
from langdetect import detect
import os
import csv

analyser = SentimentIntensityAnalyzer()

# Busca arquivos 
aquaman = "C:\\Users\\vitor\\Documents\\Python Projetcs\\AnalysisMoviews\\Data\\aquaman-tweets\\aquaman\\"

def print_sentiment_scores(sentence):
    snt = analyser.polarity_scores(sentence)
    #print(snt)
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

def getText(arquivo):
    with open(aquaman + arquivo, 'r', encoding='utf-8') as lines:
        reader = csv.reader(lines)
        next(reader)
        dataInfo = [r for r in reader]
    with open(aquaman + 'result_' + arquivo, mode='w', encoding="utf8") as fc:
        for t in dataInfo:
            try:
                x = 'null'
                if t[4]:
                    x = print_sentiment_scores(t[4])
                    aux = '"%s","%s","%s"\n' % (x[0],x[1],x[2]) 
                    fc.write(aux) 
            except IndexError:
                x = 'null'
   

getText('aquaman_03_09.csv')
getText('aquaman_09_13.csv')
getText('aquaman_14_15.csv')
getText('aquaman_16_17.csv')

