import re 
import nltk 
import csv
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

aquaman = "Data/aquaman-tweets/aquaman/"
captain = "Data/captain-tweets/"
avengers = "Data/avengers-tweets/no_war/"


def runProcess(a, b, c):
    dados = open(a + b + '.txt', 'r')
    count = 0
    for t in dados.readlines():
        count += 1
    print(c + ' = ' + str(count))


# runProcess(avengers, 'vingadores_2018_04_20_ing_sent/vingadores_2018_04_20_ing_sent_mpos', 'Vingadores Muito Positivo')
# runProcess(avengers, 'vingadores_2018_04_20_ing_sent/vingadores_2018_04_20_ing_sent_pos', 'Vingadores Positivo')
# runProcess(avengers, 'vingadores_2018_04_20_ing_sent/vingadores_2018_04_20_ing_sent_neg', 'Vingadores Negativo')
# runProcess(avengers, 'vingadores_2018_04_20_ing_sent/vingadores_2018_04_20_ing_sent_mneg', 'Vingadores Muito Negativo')

# runProcess(avengers, 'vingadores_2018_04_21_ing_sent/vingadores_2018_04_21_ing_sent_mpos', 'Vingadores Muito Positivo')
# runProcess(avengers, 'vingadores_2018_04_21_ing_sent/vingadores_2018_04_21_ing_sent_pos', 'Vingadores Positivo')
# runProcess(avengers, 'vingadores_2018_04_21_ing_sent/vingadores_2018_04_21_ing_sent_neg', 'Vingadores Negativo')
# runProcess(avengers, 'vingadores_2018_04_21_ing_sent/vingadores_2018_04_21_ing_sent_mneg', 'Vingadores Muito Negativo')

# runProcess(avengers, 'vingadores_2018_04_22_ing_sent/vingadores_2018_04_22_ing_sent_mpos', 'Vingadores Muito Positivo')
# runProcess(avengers, 'vingadores_2018_04_22_ing_sent/vingadores_2018_04_22_ing_sent_pos', 'Vingadores Positivo')
# runProcess(avengers, 'vingadores_2018_04_22_ing_sent/vingadores_2018_04_22_ing_sent_neg', 'Vingadores Negativo')
# runProcess(avengers, 'vingadores_2018_04_22_ing_sent/vingadores_2018_04_22_ing_sent_mneg', 'Vingadores Muito Negativo')

# runProcess(avengers, 'vingadores_2018_04_23_ing_sent/vingadores_2018_04_23_ing_sent_mpos', 'Vingadores Muito Positivo')
# runProcess(avengers, 'vingadores_2018_04_23_ing_sent/vingadores_2018_04_23_ing_sent_pos', 'Vingadores Positivo')
# runProcess(avengers, 'vingadores_2018_04_23_ing_sent/vingadores_2018_04_23_ing_sent_neg', 'Vingadores Negativo')
# runProcess(avengers, 'vingadores_2018_04_23_ing_sent/vingadores_2018_04_23_ing_sent_mneg', 'Vingadores Muito Negativo')

# runProcess(avengers, 'vingadores_2018_04_24_ing_sent/vingadores_2018_04_24_ing_sent_mpos', 'Vingadores Muito Positivo')
# runProcess(avengers, 'vingadores_2018_04_24_ing_sent/vingadores_2018_04_24_ing_sent_pos', 'Vingadores Positivo')
# runProcess(avengers, 'vingadores_2018_04_24_ing_sent/vingadores_2018_04_24_ing_sent_neg', 'Vingadores Negativo')
# runProcess(avengers, 'vingadores_2018_04_24_ing_sent/vingadores_2018_04_24_ing_sent_mneg', 'Vingadores Muito Negativo')

# runProcess(avengers, 'vingadores_2018_04_25_ing_sent/vingadores_2018_04_25_ing_sent_mpos', 'Vingadores Muito Positivo')
# runProcess(avengers, 'vingadores_2018_04_25_ing_sent/vingadores_2018_04_25_ing_sent_pos', 'Vingadores Positivo')
# runProcess(avengers, 'vingadores_2018_04_25_ing_sent/vingadores_2018_04_25_ing_sent_neg', 'Vingadores Negativo')
# runProcess(avengers, 'vingadores_2018_04_25_ing_sent/vingadores_2018_04_25_ing_sent_mneg', 'Vingadores Muito Negativo')

# runProcess(avengers, 'vingadores_2018_04_26_ing_sent/vingadores_2018_04_26_ing_sent_mpos', 'Vingadores Muito Positivo')
# runProcess(avengers, 'vingadores_2018_04_26_ing_sent/vingadores_2018_04_26_ing_sent_pos', 'Vingadores Positivo')
# runProcess(avengers, 'vingadores_2018_04_26_ing_sent/vingadores_2018_04_26_ing_sent_neg', 'Vingadores Negativo')
# runProcess(avengers, 'vingadores_2018_04_26_ing_sent/vingadores_2018_04_26_ing_sent_mneg', 'Vingadores Muito Negativo')

# runProcess(avengers, 'vingadores_2018_04_27_ing_sent/vingadores_2018_04_27_ing_sent_mpos', 'Vingadores Muito Positivo')
# runProcess(avengers, 'vingadores_2018_04_27_ing_sent/vingadores_2018_04_27_ing_sent_pos', 'Vingadores Positivo')
# runProcess(avengers, 'vingadores_2018_04_27_ing_sent/vingadores_2018_04_27_ing_sent_neg', 'Vingadores Negativo')
# runProcess(avengers, 'vingadores_2018_04_27_ing_sent/vingadores_2018_04_27_ing_sent_mneg', 'Vingadores Muito Negativo')

# runProcess(avengers, 'vingadores_2018_04_29_ing_sent/vingadores_2018_04_29_ing_sent_mpos', 'Vingadores Muito Positivo')
# runProcess(avengers, 'vingadores_2018_04_29_ing_sent/vingadores_2018_04_29_ing_sent_pos', 'Vingadores Positivo')
# runProcess(avengers, 'vingadores_2018_04_29_ing_sent/vingadores_2018_04_29_ing_sent_neg', 'Vingadores Negativo')
# runProcess(avengers, 'vingadores_2018_04_29_ing_sent/vingadores_2018_04_29_ing_sent_mneg', 'Vingadores Muito Negativo')

# runProcess(avengers, 'vingadores_2018_04_30_ing_sent/vingadores_2018_04_30_ing_sent_mpos', 'Vingadores Muito Positivo')
# runProcess(avengers, 'vingadores_2018_04_30_ing_sent/vingadores_2018_04_30_ing_sent_pos', 'Vingadores Positivo')
# runProcess(avengers, 'vingadores_2018_04_30_ing_sent/vingadores_2018_04_30_ing_sent_neg', 'Vingadores Negativo')
# runProcess(avengers, 'vingadores_2018_04_30_ing_sent/vingadores_2018_04_30_ing_sent_mneg', 'Vingadores Muito Negativo')

# runProcess(avengers, 'vingadores_2018_05_01_ing_sent/vingadores_2018_05_01_ing_sent_mpos', 'Vingadores Muito Positivo')
# runProcess(avengers, 'vingadores_2018_05_01_ing_sent/vingadores_2018_05_01_ing_sent_pos', 'Vingadores Positivo')
# runProcess(avengers, 'vingadores_2018_05_01_ing_sent/vingadores_2018_05_01_ing_sent_neg', 'Vingadores Negativo')
# runProcess(avengers, 'vingadores_2018_05_01_ing_sent/vingadores_2018_05_01_ing_sent_mneg', 'Vingadores Muito Negativo')

# runProcess(avengers, 'vingadores_2018_05_02_ing_sent/vingadores_2018_05_02_ing_sent_mpos', 'Vingadores Muito Positivo')
# runProcess(avengers, 'vingadores_2018_05_02_ing_sent/vingadores_2018_05_02_ing_sent_pos', 'Vingadores Positivo')
# runProcess(avengers, 'vingadores_2018_05_02_ing_sent/vingadores_2018_05_02_ing_sent_neg', 'Vingadores Negativo')
# runProcess(avengers, 'vingadores_2018_05_02_ing_sent/vingadores_2018_05_02_ing_sent_mneg', 'Vingadores Muito Negativo')

# runProcess(avengers, 'vingadores_2018_05_03_ing_sent/vingadores_2018_05_03_ing_sent_mpos', 'Vingadores Muito Positivo')
# runProcess(avengers, 'vingadores_2018_05_03_ing_sent/vingadores_2018_05_03_ing_sent_pos', 'Vingadores Positivo')
# runProcess(avengers, 'vingadores_2018_05_03_ing_sent/vingadores_2018_05_03_ing_sent_neg', 'Vingadores Negativo')
# runProcess(avengers, 'vingadores_2018_05_03_ing_sent/vingadores_2018_05_03_ing_sent_mneg', 'Vingadores Muito Negativo')

# runProcess(avengers, 'vingadores_2018_05_04_ing_sent/vingadores_2018_05_04_ing_sent_mpos', 'Vingadores Muito Positivo')
# runProcess(avengers, 'vingadores_2018_05_04_ing_sent/vingadores_2018_05_04_ing_sent_pos', 'Vingadores Positivo')
# runProcess(avengers, 'vingadores_2018_05_04_ing_sent/vingadores_2018_05_04_ing_sent_neg', 'Vingadores Negativo')
# runProcess(avengers, 'vingadores_2018_05_04_ing_sent/vingadores_2018_05_04_ing_sent_mneg', 'Vingadores Muito Negativo')

# runProcess(aquaman, 'file_results_twitter/result_aquaman_03_09/result_aquaman_03_09_mneg', 'Aquaman Muito Negativo')
# runProcess(aquaman, 'file_results_twitter/result_aquaman_03_09/result_aquaman_03_09_neg', 'Aquaman Negativo')
# runProcess(aquaman, 'file_results_twitter/result_aquaman_03_09/result_aquaman_03_09_pos', 'Aquaman Positivo')
# runProcess(aquaman, 'file_results_twitter/result_aquaman_03_09/result_aquaman_03_09_mpos', 'Aquaman Muito Positivo')

# runProcess(aquaman, 'file_results_twitter/result_aquaman_09_13/result_aquaman_09_13_mneg', 'Aquaman Muito Negativo')
# runProcess(aquaman, 'file_results_twitter/result_aquaman_09_13/result_aquaman_09_13_neg', 'Aquaman Negativo')
# runProcess(aquaman, 'file_results_twitter/result_aquaman_09_13/result_aquaman_09_13_pos', 'Aquaman Positivo')
# runProcess(aquaman, 'file_results_twitter/result_aquaman_09_13/result_aquaman_09_13_mpos', 'Aquaman Muito Positivo')

# runProcess(aquaman, 'file_results_twitter/result_aquaman_14_15/result_aquaman_14_15_mneg', 'Aquaman Muito Negativo')
# runProcess(aquaman, 'file_results_twitter/result_aquaman_14_15/result_aquaman_14_15_neg', 'Aquaman Negativo')
# runProcess(aquaman, 'file_results_twitter/result_aquaman_14_15/result_aquaman_14_15_pos', 'Aquaman Positivo')
# runProcess(aquaman, 'file_results_twitter/result_aquaman_14_15/result_aquaman_14_15_mpos', 'Aquaman Muito Positivo')

# runProcess(aquaman, 'file_results_twitter/result_aquaman_16_17/result_aquaman_16_17_mneg', 'Aquaman Muito Negativo')
# runProcess(aquaman, 'file_results_twitter/result_aquaman_16_17/result_aquaman_16_17_neg', 'Aquaman Negativo')
# runProcess(aquaman, 'file_results_twitter/result_aquaman_16_17/result_aquaman_16_17_pos', 'Aquaman Positivo')
# runProcess(aquaman, 'file_results_twitter/result_aquaman_16_17/result_aquaman_16_17_mpos', 'Aquaman Muito Positivo')

# runProcess(aquaman, 'file_results_youtube/result_aquaman_youtube_mneg', 'Aquaman Muito Negativo')
# runProcess(aquaman, 'file_results_youtube/result_aquaman_youtube_neg', 'Aquaman Negativo')
# runProcess(aquaman, 'file_results_youtube/result_aquaman_youtube_pos', 'Aquaman Positivo')
# runProcess(aquaman, 'file_results_youtube/result_aquaman_youtube_mpos', 'Aquaman Muito Positivo')

# runProcess(captain, 'result_captainmarvel_03-10_03-12/result_captainmarvel_03-10_03-12_mneg', 'Captain Marvel Muito Negativo')
# runProcess(captain, 'result_captainmarvel_03-10_03-12/result_captainmarvel_03-10_03-12_neg', 'Captain Marvel Negativo')
# runProcess(captain, 'result_captainmarvel_03-10_03-12/result_captainmarvel_03-10_03-12_pos', 'Captain Marvel Positivo')
# runProcess(captain, 'result_captainmarvel_03-10_03-12/result_captainmarvel_03-10_03-12_mpos', 'Captain Marvel Muito Positivo')

# runProcess(captain, 'result_captainmarvel_03-13/result_captainmarvel_03-13_mneg', 'Captain Marvel Muito Negativo')
# runProcess(captain, 'result_captainmarvel_03-13/result_captainmarvel_03-13_neg', 'Captain Marvel Negativo')
# runProcess(captain, 'result_captainmarvel_03-13/result_captainmarvel_03-13_pos', 'Captain Marvel Positivo')
# runProcess(captain, 'result_captainmarvel_03-13/result_captainmarvel_03-13_mpos', 'Captain Marvel Muito Positivo')

# runProcess(captain, 'result_captainmarvel_03-14_03-15/result_captainmarvel_03-14_03-15_mneg', 'Captain Marvel Muito Negativo')
# runProcess(captain, 'result_captainmarvel_03-14_03-15/result_captainmarvel_03-14_03-15_neg', 'Captain Marvel Negativo')
# runProcess(captain, 'result_captainmarvel_03-14_03-15/result_captainmarvel_03-14_03-15_pos', 'Captain Marvel Positivo')
# runProcess(captain, 'result_captainmarvel_03-14_03-15/result_captainmarvel_03-14_03-15_mpos', 'Captain Marvel Muito Positivo')

# runProcess(captain, 'result_captainmarvel_03-18/result_captainmarvel_03-18_mneg', 'Captain Marvel Muito Negativo')
# runProcess(captain, 'result_captainmarvel_03-18/result_captainmarvel_03-18_neg', 'Captain Marvel Negativo')
# runProcess(captain, 'result_captainmarvel_03-18/result_captainmarvel_03-18_pos', 'Captain Marvel Positivo')
# runProcess(captain, 'result_captainmarvel_03-18/result_captainmarvel_03-18_mpos', 'Captain Marvel Muito Positivo')

# runProcess(captain, 'result_captain_youtube_mneg', 'Captain Marvel Muito Negativo')
# runProcess(captain, 'result_captain_youtube_neg', 'Captain Marvel Negativo')
# runProcess(captain, 'result_captain_youtube_pos', 'Captain Marvel Positivo')
# runProcess(captain, 'result_captain_youtube_mpos', 'Captain Marvel Muito Positivo')

runProcess(avengers, 'result_avengers_youtube_mneg', 'Avengers Muito Negativo')
runProcess(avengers, 'result_avengers_youtube_neg', 'Avengers Negativo')
runProcess(avengers, 'result_avengers_youtube_pos', 'Avengers Positivo')
runProcess(avengers, 'result_avengers_youtube_mpos', 'Avengers Muito Positivo')