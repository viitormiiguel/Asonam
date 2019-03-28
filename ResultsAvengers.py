import nltk
import csv
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

c = 'Data/avengers-tweets/no_war/'

def resultados(dia):
    # Resultados vingadores
    dados = open(c + dia + '_ing_sent.csv', 'r', encoding='utf8')
    pos = 0 
    neg = 0
    for t in dados.readlines():
        if 'Positivo' in t:
            pos += 1
        if 'Negativo' in t:
            neg += 1
    print('| --- ' + dia + ' --- |')
    print('Investing Pos ', pos)
    print('Investing Neg ', neg)

resultados("vingadores_2018_04_20")
resultados("vingadores_2018_04_21")
resultados("vingadores_2018_04_22")
resultados("vingadores_2018_04_23")
resultados("vingadores_2018_04_24")
# resultados("vingadores_2018_04_25")
resultados("vingadores_2018_04_26")
resultados("vingadores_2018_04_27")

# # Depois da estreia
resultados("vingadores_2018_04_30")
resultados("vingadores_2018_05_01")
resultados("vingadores_2018_05_02")
resultados("vingadores_2018_05_03")
resultados("vingadores_2018_05_04")