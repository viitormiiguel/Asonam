import nltk
import csv
import datetime
import pandas as pd
# import matplotlib.pyplot as plt
import numpy as np

c = 'Data/captain-tweets/'

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

resultados("result_captainmarvel_03-10_03-12")
resultados("result_captainmarvel_03-13")
resultados("result_captainmarvel_03-14_03-15")
resultados("result_captainmarvel_03-18")
