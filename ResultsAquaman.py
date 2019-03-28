import nltk
import csv
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

c = 'Data/aquaman-tweets/aquaman/'

def resultados(dia):
    # Resultados Aquaman
    dados = open(c + dia + '.csv', 'r', encoding='utf8')
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

resultados("taquaman_03_09")
resultados("taquaman_09_13")
resultados("taquaman_14_15")
resultados("taquaman_16_17")
