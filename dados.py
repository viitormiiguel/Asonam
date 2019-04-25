import ijson
import json
# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# from datetime import datetime
# from langdetect import detect
import os
import csv
import ast
import re 
import nltk

aquaman = "Data/aquaman-tweets/aquaman/"
captain = "Data/captain-tweets/"
avengers = "Data/avengers-tweets/no_war/"

def resultados(path, arquivo, novo):
    dados = open(path + arquivo + '.csv', 'r')
    f1 = open(path + arquivo + '_mpos.txt', 'w+')
    f2 = open(path + arquivo + '_pos.txt', 'w+')
    f3 = open(path + arquivo + '_neu.txt', 'w+')
    f4 = open(path + arquivo + '_neg.txt', 'w+')
    f5 = open(path + arquivo + '_mneg.txt', 'w+')
    for t in dados.readlines():
        if t:
            x = '"' + t + '"'
            if x.find('"++"') > 0 :
                f1.write(t + "\n")                
            if x.find('"+"') > 0 :
                f2.write(t + "\n")
            if x.find('"0"') > 0 :
                f3.write(t + "\n")
            if x.find('"-"') > 0 :
                f4.write(t + "\n")
            if x.find('"--"') > 0 :
                f5.write(t + "\n")
    
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()

resultados(avengers, "result_avengers_youtube", 'null')

# resultados(aquaman, "result_aquaman_youtube", 'file_results_youtube/')
# resultados(captain, "result_captain_youtube", 'file_results_youtube/')

# resultados(aquaman, "result_aquaman_03_09", 'null')
# resultados(aquaman, "result_aquaman_09_13", 'null')
# resultados(aquaman, "result_aquaman_14_15", 'null')
# resultados(aquaman, "result_aquaman_16_17", 'null')

# resultados(captain, "result_captainmarvel_03-10_03-12", 'null')
# resultados(captain, "result_captainmarvel_03-13", 'null')
# resultados(captain, "result_captainmarvel_03-14_03-15", 'null')
# resultados(captain, "result_captainmarvel_03-18", 'null')

def runNumbers(c, d, e, f):
    document_text = open(c + d + '.txt', 'r')
    count = 0
    for dt in document_text.readlines():
        # print(dt)
        if dt:
            count += 1
    print('Numero de textos ' + e + ' ' + str(count) + ' ' + f) 


# runNumbers(captain, 'result_captain_youtube_mpos', 'muito positivo', 'youtube captain')
# runNumbers(captain, 'result_captain_youtube_pos', 'positivo', 'youtube captain')
# runNumbers(captain, 'result_captain_youtube_neu', 'neutro', 'youtube captain')
# runNumbers(captain, 'result_captain_youtube_neg', 'negativo', 'youtube captain')
# runNumbers(captain, 'result_captain_youtube_mneg', 'muito negativo', 'youtube captain')


# runNumbers(aquaman, 'file_results_youtube/result_aquaman_youtube_mneg', 'muito negativo', 'youtube aquaman')
# runNumbers(aquaman, 'file_results_youtube/result_aquaman_youtube_neg', 'negativo', 'youtube aquaman')
# runNumbers(aquaman, 'file_results_youtube/result_aquaman_youtube_neu', 'neutro', 'youtube aquaman')
# runNumbers(aquaman, 'file_results_youtube/result_aquaman_youtube_pos', 'positivo', 'youtube aquaman')
# runNumbers(aquaman, 'file_results_youtube/result_aquaman_youtube_mpos', 'muito positivo', 'youtube aquaman')

# runNumbers(aquaman, 'file_results_twitter/result_aquaman_03_09/result_aquaman_03_09_mneg', 'muito negativo', 'twitter 03-09 aquaman')
# runNumbers(aquaman, 'file_results_twitter/result_aquaman_03_09/result_aquaman_03_09_neg', 'negativo', 'twitter 03-09 aquaman')
# runNumbers(aquaman, 'file_results_twitter/result_aquaman_03_09/result_aquaman_03_09_neu', 'neutro', 'twitter 03-09 aquaman')
# runNumbers(aquaman, 'file_results_twitter/result_aquaman_03_09/result_aquaman_03_09_pos', 'positivo', 'twitter 03-09 aquaman')
# runNumbers(aquaman, 'file_results_twitter/result_aquaman_03_09/result_aquaman_03_09_mpos', 'muito positivo', 'twitter 03-09 aquaman')

# runNumbers(aquaman, 'file_results_twitter/result_aquaman_09_13/result_aquaman_09_13_mneg', 'muito negativo', 'twitter 09-13 aquaman')
# runNumbers(aquaman, 'file_results_twitter/result_aquaman_09_13/result_aquaman_09_13_neg', 'negativo', 'twitter 09-13 aquaman')
# runNumbers(aquaman, 'file_results_twitter/result_aquaman_09_13/result_aquaman_09_13_neu', 'neutro', 'twitter 09-13 aquaman')
# runNumbers(aquaman, 'file_results_twitter/result_aquaman_09_13/result_aquaman_09_13_pos', 'positivo', 'twitter 09-13 aquaman')
# runNumbers(aquaman, 'file_results_twitter/result_aquaman_09_13/result_aquaman_09_13_mpos', 'muito positivo', 'twitter 09-13 aquaman')

# runNumbers(aquaman, 'file_results_twitter/result_aquaman_14_15/result_aquaman_14_15_mneg', 'muito negativo', 'twitter 14-15 aquaman')
# runNumbers(aquaman, 'file_results_twitter/result_aquaman_14_15/result_aquaman_14_15_neg', 'negativo', 'twitter 14-15 aquaman')
# runNumbers(aquaman, 'file_results_twitter/result_aquaman_14_15/result_aquaman_14_15_neu', 'neutro', 'twitter 14-15 aquaman')
# runNumbers(aquaman, 'file_results_twitter/result_aquaman_14_15/result_aquaman_14_15_pos', 'positivo', 'twitter 14-15 aquaman')
# runNumbers(aquaman, 'file_results_twitter/result_aquaman_14_15/result_aquaman_14_15_mpos', 'muito positivo', 'twitter 14-15 aquaman')


# runNumbers(aquaman, 'file_results_twitter/result_aquaman_16_17/result_aquaman_16_17_mneg', 'muito negativo', 'twitter 16-17 aquaman')
# runNumbers(aquaman, 'file_results_twitter/result_aquaman_16_17/result_aquaman_16_17_neg', 'negativo', 'twitter 16-17 aquaman')
# runNumbers(aquaman, 'file_results_twitter/result_aquaman_16_17/result_aquaman_16_17_neu', 'neutro', 'twitter 16-17 aquaman')
# runNumbers(aquaman, 'file_results_twitter/result_aquaman_16_17/result_aquaman_16_17_pos', 'positivo', 'twitter 16-17 aquaman')
# runNumbers(aquaman, 'file_results_twitter/result_aquaman_16_17/result_aquaman_16_17_mpos', 'muito positivo', 'twitter 16-17 aquaman')

# runNumbers(avengers, 'vingadores_2018_04_20_ing_sent/vingadores_2018_04_20_ing_sent_mneg',  'muito negativo', 'vingadores_2018_04_20')
# runNumbers(avengers, 'vingadores_2018_04_20_ing_sent/vingadores_2018_04_20_ing_sent_neg', 'negativo', 'vingadores_2018_04_20')
# runNumbers(avengers, 'vingadores_2018_04_20_ing_sent/vingadores_2018_04_20_ing_sent_neu', 'neutro', 'vingadores_2018_04_20')
# runNumbers(avengers, 'vingadores_2018_04_20_ing_sent/vingadores_2018_04_20_ing_sent_pos', 'positivo', 'vingadores_2018_04_20')
# runNumbers(avengers, 'vingadores_2018_04_20_ing_sent/vingadores_2018_04_20_ing_sent_mpos',  'muito positivo', 'vingadores_2018_04_20')

# runNumbers(avengers, 'vingadores_2018_04_21_ing_sent/vingadores_2018_04_21_ing_sent_mneg',   'muito negativo','vingadores_2018_04_21')
# runNumbers(avengers, 'vingadores_2018_04_21_ing_sent/vingadores_2018_04_21_ing_sent_neg', 'negativo', 'vingadores_2018_04_21')
# runNumbers(avengers, 'vingadores_2018_04_21_ing_sent/vingadores_2018_04_21_ing_sent_neu', 'neutro', 'vingadores_2018_04_21')
# runNumbers(avengers, 'vingadores_2018_04_21_ing_sent/vingadores_2018_04_21_ing_sent_pos', 'positivo', 'vingadores_2018_04_21')
# runNumbers(avengers, 'vingadores_2018_04_21_ing_sent/vingadores_2018_04_21_ing_sent_mpos',   'muito positivo','vingadores_2018_04_21')

# runNumbers(avengers, 'vingadores_2018_04_22_ing_sent/vingadores_2018_04_22_ing_sent_mneg',  'muito negativo','vingadores_2018_04_22')
# runNumbers(avengers, 'vingadores_2018_04_22_ing_sent/vingadores_2018_04_22_ing_sent_neg','negativo', 'vingadores_2018_04_22')
# runNumbers(avengers, 'vingadores_2018_04_22_ing_sent/vingadores_2018_04_22_ing_sent_neu','neutro', 'vingadores_2018_04_22')
# runNumbers(avengers, 'vingadores_2018_04_22_ing_sent/vingadores_2018_04_22_ing_sent_pos','positivo', 'vingadores_2018_04_22')
# runNumbers(avengers, 'vingadores_2018_04_22_ing_sent/vingadores_2018_04_22_ing_sent_mpos',  'muito positivo','vingadores_2018_04_22')

# runNumbers(avengers, 'vingadores_2018_04_23_ing_sent/vingadores_2018_04_23_ing_sent_mneg',  'muito negativo','vingadores_2018_04_23')
# runNumbers(avengers, 'vingadores_2018_04_23_ing_sent/vingadores_2018_04_23_ing_sent_neg','negativo', 'vingadores_2018_04_23')
# runNumbers(avengers, 'vingadores_2018_04_23_ing_sent/vingadores_2018_04_23_ing_sent_neu','neutro', 'vingadores_2018_04_23')
# runNumbers(avengers, 'vingadores_2018_04_23_ing_sent/vingadores_2018_04_23_ing_sent_pos','positivo', 'vingadores_2018_04_23')
# runNumbers(avengers, 'vingadores_2018_04_23_ing_sent/vingadores_2018_04_23_ing_sent_mpos',  'muito positivo','vingadores_2018_04_23')

# runNumbers(avengers, 'vingadores_2018_04_24_ing_sent/vingadores_2018_04_24_ing_sent_mneg',  'muito negativo','vingadores_2018_04_24')
# runNumbers(avengers, 'vingadores_2018_04_24_ing_sent/vingadores_2018_04_24_ing_sent_neg','negativo', 'vingadores_2018_04_24')
# runNumbers(avengers, 'vingadores_2018_04_24_ing_sent/vingadores_2018_04_24_ing_sent_neu','neutro', 'vingadores_2018_04_24')
# runNumbers(avengers, 'vingadores_2018_04_24_ing_sent/vingadores_2018_04_24_ing_sent_pos','positivo', 'vingadores_2018_04_24')
# runNumbers(avengers, 'vingadores_2018_04_24_ing_sent/vingadores_2018_04_24_ing_sent_mpos',  'muito positivo','vingadores_2018_04_24')

# runNumbers(avengers, 'vingadores_2018_04_25_ing_sent/vingadores_2018_04_25_ing_sent_mneg',  'muito negativo','vingadores_2018_04_25')
# runNumbers(avengers, 'vingadores_2018_04_25_ing_sent/vingadores_2018_04_25_ing_sent_neg','negativo', 'vingadores_2018_04_25')
# runNumbers(avengers, 'vingadores_2018_04_25_ing_sent/vingadores_2018_04_25_ing_sent_neu','neutro', 'vingadores_2018_04_25')
# runNumbers(avengers, 'vingadores_2018_04_25_ing_sent/vingadores_2018_04_25_ing_sent_pos','positivo', 'vingadores_2018_04_25')
# runNumbers(avengers, 'vingadores_2018_04_25_ing_sent/vingadores_2018_04_25_ing_sent_mpos',  'muito positivo','vingadores_2018_04_25')

# runNumbers(avengers, 'vingadores_2018_04_26_ing_sent/vingadores_2018_04_26_ing_sent_mneg',  'muito negativo','vingadores_2018_04_26')
# runNumbers(avengers, 'vingadores_2018_04_26_ing_sent/vingadores_2018_04_26_ing_sent_neg','negativo', 'vingadores_2018_04_26')
# runNumbers(avengers, 'vingadores_2018_04_26_ing_sent/vingadores_2018_04_26_ing_sent_neu','neutro', 'vingadores_2018_04_26')
# runNumbers(avengers, 'vingadores_2018_04_26_ing_sent/vingadores_2018_04_26_ing_sent_pos','positivo', 'vingadores_2018_04_26')
# runNumbers(avengers, 'vingadores_2018_04_26_ing_sent/vingadores_2018_04_26_ing_sent_mpos',  'muito positivo','vingadores_2018_04_26')

# runNumbers(avengers, 'vingadores_2018_04_27_ing_sent/vingadores_2018_04_27_ing_sent_mneg',  'muito negativo','vingadores_2018_04_27')
# runNumbers(avengers, 'vingadores_2018_04_27_ing_sent/vingadores_2018_04_27_ing_sent_neg','negativo', 'vingadores_2018_04_27')
# runNumbers(avengers, 'vingadores_2018_04_27_ing_sent/vingadores_2018_04_27_ing_sent_neu','neutro', 'vingadores_2018_04_27')
# runNumbers(avengers, 'vingadores_2018_04_27_ing_sent/vingadores_2018_04_27_ing_sent_pos','positivo', 'vingadores_2018_04_27')
# runNumbers(avengers, 'vingadores_2018_04_27_ing_sent/vingadores_2018_04_27_ing_sent_mpos',  'muito positivo','vingadores_2018_04_27')

# runNumbers(avengers, 'vingadores_2018_04_29_ing_sent/vingadores_2018_04_29_ing_sent_mneg',  'muito negativo','vingadores_2018_04_29')
# runNumbers(avengers, 'vingadores_2018_04_29_ing_sent/vingadores_2018_04_29_ing_sent_neg','negativo', 'vingadores_2018_04_29')
# runNumbers(avengers, 'vingadores_2018_04_29_ing_sent/vingadores_2018_04_29_ing_sent_neu','neutro', 'vingadores_2018_04_29')
# runNumbers(avengers, 'vingadores_2018_04_29_ing_sent/vingadores_2018_04_29_ing_sent_pos','positivo', 'vingadores_2018_04_29')
# runNumbers(avengers, 'vingadores_2018_04_29_ing_sent/vingadores_2018_04_29_ing_sent_mpos',  'muito positivo','vingadores_2018_04_29')

# runNumbers(avengers, 'vingadores_2018_04_30_ing_sent/vingadores_2018_04_30_ing_sent_mneg',  'muito negativo','vingadores_2018_04_30')
# runNumbers(avengers, 'vingadores_2018_04_30_ing_sent/vingadores_2018_04_30_ing_sent_neg','negativo', 'vingadores_2018_04_30')
# runNumbers(avengers, 'vingadores_2018_04_30_ing_sent/vingadores_2018_04_30_ing_sent_neu','neutro', 'vingadores_2018_04_30')
# runNumbers(avengers, 'vingadores_2018_04_30_ing_sent/vingadores_2018_04_30_ing_sent_pos','positivo', 'vingadores_2018_04_30')
# runNumbers(avengers, 'vingadores_2018_04_30_ing_sent/vingadores_2018_04_30_ing_sent_mpos',  'muito positivo','vingadores_2018_04_30')

# runNumbers(avengers, 'vingadores_2018_05_01_ing_sent/vingadores_2018_05_01_ing_sent_mneg',  'muito negativo','vingadores_2018_05_01')
# runNumbers(avengers, 'vingadores_2018_05_01_ing_sent/vingadores_2018_05_01_ing_sent_neg','negativo', 'vingadores_2018_05_01')
# runNumbers(avengers, 'vingadores_2018_05_01_ing_sent/vingadores_2018_05_01_ing_sent_neu','neutro', 'vingadores_2018_05_01')
# runNumbers(avengers, 'vingadores_2018_05_01_ing_sent/vingadores_2018_05_01_ing_sent_pos','positivo', 'vingadores_2018_05_01')
# runNumbers(avengers, 'vingadores_2018_05_01_ing_sent/vingadores_2018_05_01_ing_sent_mpos',  'muito positivo','vingadores_2018_05_01')

# runNumbers(avengers, 'vingadores_2018_05_02_ing_sent/vingadores_2018_05_02_ing_sent_mneg',  'muito negativo','vingadores_2018_05_02')
# runNumbers(avengers, 'vingadores_2018_05_02_ing_sent/vingadores_2018_05_02_ing_sent_neg','negativo', 'vingadores_2018_05_02')
# runNumbers(avengers, 'vingadores_2018_05_02_ing_sent/vingadores_2018_05_02_ing_sent_neu','neutro', 'vingadores_2018_05_02')
# runNumbers(avengers, 'vingadores_2018_05_02_ing_sent/vingadores_2018_05_02_ing_sent_pos','positivo', 'vingadores_2018_05_02')
# runNumbers(avengers, 'vingadores_2018_05_02_ing_sent/vingadores_2018_05_02_ing_sent_mpos',  'muito positivo','vingadores_2018_05_02')

# runNumbers(avengers, 'vingadores_2018_05_03_ing_sent/vingadores_2018_05_03_ing_sent_mneg',  'muito negativo','vingadores_2018_05_03')
# runNumbers(avengers, 'vingadores_2018_05_03_ing_sent/vingadores_2018_05_03_ing_sent_neg','negativo', 'vingadores_2018_05_03')
# runNumbers(avengers, 'vingadores_2018_05_03_ing_sent/vingadores_2018_05_03_ing_sent_neu','neutro', 'vingadores_2018_05_03')
# runNumbers(avengers, 'vingadores_2018_05_03_ing_sent/vingadores_2018_05_03_ing_sent_pos','positivo', 'vingadores_2018_05_03')
# runNumbers(avengers, 'vingadores_2018_05_03_ing_sent/vingadores_2018_05_03_ing_sent_mpos',  'muito positivo','vingadores_2018_05_03')

# runNumbers(avengers, 'vingadores_2018_05_04_ing_sent/vingadores_2018_05_04_ing_sent_mneg',  'muito negativo','vingadores_2018_05_04')
# runNumbers(avengers, 'vingadores_2018_05_04_ing_sent/vingadores_2018_05_04_ing_sent_neg','negativo', 'vingadores_2018_05_04')
# runNumbers(avengers, 'vingadores_2018_05_04_ing_sent/vingadores_2018_05_04_ing_sent_neu','neutro', 'vingadores_2018_05_04')
# runNumbers(avengers, 'vingadores_2018_05_04_ing_sent/vingadores_2018_05_04_ing_sent_pos','positivo', 'vingadores_2018_05_04')
# runNumbers(avengers, 'vingadores_2018_05_04_ing_sent/vingadores_2018_05_04_ing_sent_mpos',  'muito positivo','vingadores_2018_05_04')

# runNumbers(captain, 'result_captainmarvel_03-10_03-12/result_captainmarvel_03-10_03-12_mneg', 'muito negativo', 'result_captainmarvel_03-10_03-12')
# runNumbers(captain, 'result_captainmarvel_03-10_03-12/result_captainmarvel_03-10_03-12_neg', 'negativo', 'result_captainmarvel_03-10_03-12')
# runNumbers(captain, 'result_captainmarvel_03-10_03-12/result_captainmarvel_03-10_03-12_neu', 'neutro', 'result_captainmarvel_03-10_03-12')
# runNumbers(captain, 'result_captainmarvel_03-10_03-12/result_captainmarvel_03-10_03-12_pos', 'positivo', 'result_captainmarvel_03-10_03-12')
# runNumbers(captain, 'result_captainmarvel_03-10_03-12/result_captainmarvel_03-10_03-12_mpos', 'muito positivo', 'result_captainmarvel_03-10_03-12')

# runNumbers(captain, 'result_captainmarvel_03-13/result_captainmarvel_03-13_mneg', 'muito negativo', 'result_captainmarvel_03-13')
# runNumbers(captain, 'result_captainmarvel_03-13/result_captainmarvel_03-13_neg', 'negativo', 'result_captainmarvel_03-13')
# runNumbers(captain, 'result_captainmarvel_03-13/result_captainmarvel_03-13_neu', 'neutro', 'result_captainmarvel_03-13')
# runNumbers(captain, 'result_captainmarvel_03-13/result_captainmarvel_03-13_pos', 'positivo', 'result_captainmarvel_03-13')
# runNumbers(captain, 'result_captainmarvel_03-13/result_captainmarvel_03-13_mpos', 'muito positivo', 'result_captainmarvel_03-13')

# runNumbers(captain, 'result_captainmarvel_03-14_03-15/result_captainmarvel_03-14_03-15_mneg', 'muito negativo', 'result_captainmarvel_03-14_03-15')
# runNumbers(captain, 'result_captainmarvel_03-14_03-15/result_captainmarvel_03-14_03-15_neg', 'negativo', 'result_captainmarvel_03-14_03-15')
# runNumbers(captain, 'result_captainmarvel_03-14_03-15/result_captainmarvel_03-14_03-15_neu', 'neutro', 'result_captainmarvel_03-14_03-15')
# runNumbers(captain, 'result_captainmarvel_03-14_03-15/result_captainmarvel_03-14_03-15_pos', 'positivo', 'result_captainmarvel_03-14_03-15')
# runNumbers(captain, 'result_captainmarvel_03-14_03-15/result_captainmarvel_03-14_03-15_mpos', 'muito positivo', 'result_captainmarvel_03-14_03-15')

# runNumbers(captain, 'result_captainmarvel_03-18/result_captainmarvel_03-18_mneg', 'muito negativo', 'result_captainmarvel_03-18')
# runNumbers(captain, 'result_captainmarvel_03-18/result_captainmarvel_03-18_neg', 'negativo', 'result_captainmarvel_03-18')
# runNumbers(captain, 'result_captainmarvel_03-18/result_captainmarvel_03-18_neu', 'neutro', 'result_captainmarvel_03-18')
# runNumbers(captain, 'result_captainmarvel_03-18/result_captainmarvel_03-18_pos', 'positivo', 'result_captainmarvel_03-18')
# runNumbers(captain, 'result_captainmarvel_03-18/result_captainmarvel_03-18_mpos', 'muito positivo', 'result_captainmarvel_03-18')

runNumbers(avengers, 'result_avengers_youtube_mneg', 'muito negativo', 'Youtube')
runNumbers(avengers, 'result_avengers_youtube_neg', 'negativo', 'Youtube')
runNumbers(avengers, 'result_avengers_youtube_neu', 'neutro', 'Youtube')
runNumbers(avengers, 'result_avengers_youtube_pos', 'positivo', 'Youtube')
runNumbers(avengers, 'result_avengers_youtube_mpos', 'muito positivo', 'Youtube')
