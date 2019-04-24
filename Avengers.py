import ijson
import json
import os
import csv
import pandas as pd 

avengers = "Data/avengers-tweets/no_war/"

def getYoutube(path, arquivo, name):
    f1 = open(path + arquivo + '_mpos.txt', 'w+', encoding='utf8')
    f2 = open(path + arquivo + '_pos.txt', 'w+', encoding='utf8')
    f3 = open(path + arquivo + '_neu.txt', 'w+', encoding='utf8')
    f4 = open(path + arquivo + '_neg.txt', 'w+', encoding='utf8')
    f5 = open(path + arquivo + '_mneg.txt', 'w+', encoding='utf8')
    with open (path + arquivo, 'r') as f:
        t = json.load(f)
        for texto in t:
            if '++' in texto['intensidade']:
                f1.write(texto['sentence'])
            if '+' in texto['intensidade']:
                f2.write(texto['sentence'])
            if '0' in texto['intensidade']:
                f3.write(texto['sentence'])
            if '-' in texto['intensidade']:
                f4.write(texto['sentence'])
            if '--' in texto['intensidade']:
                f5.write(texto['sentence'])
        f1.close()
        f2.close()
        f3.close()
        f4.close()
        f5.close()
            

# getYoutube(avengers, 'vingadores_2018_04_20_ing_sent', 'avengers')
# getYoutube(avengers, 'vingadores_2018_04_21_ing_sent', 'avengers')
# getYoutube(avengers, 'vingadores_2018_04_22_ing_sent', 'avengers')
# getYoutube(avengers, 'vingadores_2018_04_23_ing_sent', 'avengers')
# getYoutube(avengers, 'vingadores_2018_04_24_ing_sent', 'avengers')
# getYoutube(avengers, 'vingadores_2018_04_25_ing_sent', 'avengers')
# getYoutube(avengers, 'vingadores_2018_04_26_ing_sent', 'avengers')
# getYoutube(avengers, 'vingadores_2018_04_27_ing_sent', 'avengers')
# getYoutube(avengers, 'vingadores_2018_04_29_ing_sent', 'avengers')
# getYoutube(avengers, 'vingadores_2018_04_30_ing_sent', 'avengers')
# getYoutube(avengers, 'vingadores_2018_05_01_ing_sent', 'avengers')
# getYoutube(avengers, 'vingadores_2018_05_02_ing_sent', 'avengers')
# getYoutube(avengers, 'vingadores_2018_05_03_ing_sent', 'avengers')
# getYoutube(avengers, 'vingadores_2018_05_04_ing_sent', 'avengers')
