import re
import string
import nltk
from nltk.corpus import stopwords
from nltk import pos_tag, word_tokenize

aquaman = "Data/aquaman-tweets/aquaman/"
captain = "Data/captain-tweets/"
avengers = "Data/avengers-tweets/no_war/"

people = ['Iron Man', 'Thor', 'Hulk', 'Captain America', 'Black Widow', 'War Machine', 'Doctor Strange',
'Spider Man', 'Black Panther', 'Gamora', 'Nebula', 'Loki', 'Vision', 'Scarlet Witch', 'Falcon', 'Winter Soldier', 'Heimdall',
'Okoye', 'Eitri', 'Wong', 'Mantis', 'Drax', 'Groot', 'Rocket', 'Pepper Potts', 'The Collector', 'Thanos', 'Star Lord']

vip = ['Iron Man', 'Thor', 'Hulk', 'Captain America', 'Black Widow', 'Doctor Strange', 'Spider-Man', 'Gamora', 'Thanos']

aq = ['Arthur', 'Mera', 'Vulko', 'King Orm', 'Atlanna', 'King Nereus', 'Manta', 'Tom Curry', 'Captain Murk', 'Jesse', 'Dr. Stephen Shin',
'King Atlan', 'Cargo Pilot']

cap = ['Carol Danvers', 'Vers', 'Captain Marvel', 'Nick Fury', 'Talos', 'Keller', 'Yon-Rogg', 'Supreme Intelligence', 'Dr. Wendy Lawson', 'Maria Rambeau',
'Agent Coulson', 'Bron-Char', 'Minn-Erva', 'Att-Lass', 'Korath', 'Ronan', 'Soh-Larr', 'Norex', 'Monica Rambeau']

def getImportanWords(c, d, p, q, vip, g):
        document_text = open(c + d + '.txt', 'r')
        arrayWords = []
        f1 = open(c + 'oc-yt-avengers-' +  g + '.txt', 'a+')
        for dt in document_text.readlines():
                t = dt.split()
                # print(t)
                try: 
                        x = 'null'
                        if t: 
                                txt = t[1][0:len(t[1])-4]
                                t1 = t[0][2:len(t[0])-1]
                                t1 = t1.replace("'","")

                                t2 = str(t[1][5:])
                                t2 = t2[t2.find(','):]
                                t2 = t2[1:]

                                if txt.find('JJ') == 1: 
                                        if int(t2) > 100:
                                                arrayWords.append(t1)
                except IndexError:
                        x = 'null'

        contagem = 0
        # print('\n')
        # print(q)
        for word in arrayWords:
                for texto in p:
                        if word in texto and vip in texto:
                                contagem += 1        
                # print('Palavra: ' + word + ' contagem ' + str(contagem) + ' personagem: ' + vip)
                # resp = 'Palavra: ' + word + ' contagem ' + str(contagem) + ' personagem: ' + vip + '\n'
                resp = word + ';' + str(contagem) + ';' + vip + '\n'
                f1.write(resp)
        f1.close

        return arrayWords


def runProcess(c, d, d1, e, f, g):
        doc = open(c + d + '.txt', 'r')
        arrayW = []
        # varre array de personagens
        for p in people:
                count = 0
                p = p.lower()
                for dt in doc.readlines():
                        # d = dt.split()
                        # print(dt)
                        dt = dt.lower()
                        if p in dt:
                                count += 1
                                final = dt 
                                # print('Contagem ' + str(count))
                                arrayW.append(final)
                getImportanWords(c, d1 + e, arrayW, f, p, g)
        return arrayW

# runProcess(avengers, 'vingadores_2018_04_20_ing_sent/vingadores_2018_04_20_ing_sent_mneg', 'vingadores_2018_04_20_ing_sent/', 'vingadores_2018_04_20_tf-mneg', 'Muito Negativo', 'mneg')
# runProcess(avengers, 'vingadores_2018_04_20_ing_sent/vingadores_2018_04_20_ing_sent_neg', 'vingadores_2018_04_20_ing_sent/', 'vingadores_2018_04_20_tf-neg', 'Negativo', 'neg')
# runProcess(avengers, 'vingadores_2018_04_20_ing_sent/vingadores_2018_04_20_ing_sent_neu', 'vingadores_2018_04_20_ing_sent/', 'vingadores_2018_04_20_tf-neu', 'Neutro', 'neu')
# runProcess(avengers, 'vingadores_2018_04_20_ing_sent/vingadores_2018_04_20_ing_sent_pos', 'vingadores_2018_04_20_ing_sent/', 'vingadores_2018_04_20_tf-pos', 'Positivo', 'pos')
# runProcess(avengers, 'vingadores_2018_04_20_ing_sent/vingadores_2018_04_20_ing_sent_mpos', 'vingadores_2018_04_20_ing_sent/', 'vingadores_2018_04_20_tf-mpos', 'Muito Positivo', 'mpos')

# runProcess(avengers, 'vingadores_2018_04_21_ing_sent/vingadores_2018_04_21_ing_sent_mneg', 'vingadores_2018_04_21_ing_sent/', 'vingadores_2018_04_21_tf-mneg', 'Muito Negativo', 'mneg')
# runProcess(avengers, 'vingadores_2018_04_21_ing_sent/vingadores_2018_04_21_ing_sent_neg', 'vingadores_2018_04_21_ing_sent/', 'vingadores_2018_04_21_tf-neg', 'Negativo', 'neg')
# runProcess(avengers, 'vingadores_2018_04_21_ing_sent/vingadores_2018_04_21_ing_sent_neu', 'vingadores_2018_04_21_ing_sent/', 'vingadores_2018_04_21_tf-neu', 'Neutro', 'neu')
# runProcess(avengers, 'vingadores_2018_04_21_ing_sent/vingadores_2018_04_21_ing_sent_pos', 'vingadores_2018_04_21_ing_sent/', 'vingadores_2018_04_21_tf-pos', 'Positivo', 'pos')
# runProcess(avengers, 'vingadores_2018_04_21_ing_sent/vingadores_2018_04_21_ing_sent_mpos', 'vingadores_2018_04_21_ing_sent/', 'vingadores_2018_04_21_tf-mpos', 'Muito Positivo', 'mpos')

# runProcess(avengers, 'vingadores_2018_04_22_ing_sent/vingadores_2018_04_22_ing_sent_mneg', 'vingadores_2018_04_22_ing_sent/', 'vingadores_2018_04_22_tf-mneg', 'Muito Negativo', 'mneg')
# runProcess(avengers, 'vingadores_2018_04_22_ing_sent/vingadores_2018_04_22_ing_sent_neg', 'vingadores_2018_04_22_ing_sent/', 'vingadores_2018_04_22_tf-neg', 'Negativo', 'neg')
# runProcess(avengers, 'vingadores_2018_04_22_ing_sent/vingadores_2018_04_22_ing_sent_neu', 'vingadores_2018_04_22_ing_sent/', 'vingadores_2018_04_22_tf-neu', 'Neutro', 'neu')
# runProcess(avengers, 'vingadores_2018_04_22_ing_sent/vingadores_2018_04_22_ing_sent_pos', 'vingadores_2018_04_22_ing_sent/', 'vingadores_2018_04_22_tf-pos', 'Positivo', 'pos')
# runProcess(avengers, 'vingadores_2018_04_22_ing_sent/vingadores_2018_04_22_ing_sent_mpos', 'vingadores_2018_04_22_ing_sent/', 'vingadores_2018_04_22_tf-mpos', 'Muito Positivo', 'mpos')

# runProcess(avengers, 'vingadores_2018_04_23_ing_sent/vingadores_2018_04_23_ing_sent_mneg', 'vingadores_2018_04_23_ing_sent/', 'vingadores_2018_04_23_tf-mneg', 'Muito Negativo', 'mneg')
# runProcess(avengers, 'vingadores_2018_04_23_ing_sent/vingadores_2018_04_23_ing_sent_neg', 'vingadores_2018_04_23_ing_sent/', 'vingadores_2018_04_23_tf-neg', 'Negativo', 'neg')
# runProcess(avengers, 'vingadores_2018_04_23_ing_sent/vingadores_2018_04_23_ing_sent_neu', 'vingadores_2018_04_23_ing_sent/', 'vingadores_2018_04_23_tf-neu', 'Neutro', 'neu')
# runProcess(avengers, 'vingadores_2018_04_23_ing_sent/vingadores_2018_04_23_ing_sent_pos', 'vingadores_2018_04_23_ing_sent/', 'vingadores_2018_04_23_tf-pos', 'Positivo', 'pos')
# runProcess(avengers, 'vingadores_2018_04_23_ing_sent/vingadores_2018_04_23_ing_sent_mpos', 'vingadores_2018_04_23_ing_sent/', 'vingadores_2018_04_23_tf-mpos', 'Muito Positivo', 'mpos')

# runProcess(avengers, 'vingadores_2018_04_24_ing_sent/vingadores_2018_04_24_ing_sent_mneg', 'vingadores_2018_04_24_ing_sent/', 'vingadores_2018_04_24_tf-mneg', 'Muito Negativo', 'mneg')
# runProcess(avengers, 'vingadores_2018_04_24_ing_sent/vingadores_2018_04_24_ing_sent_neg', 'vingadores_2018_04_24_ing_sent/', 'vingadores_2018_04_24_tf-neg', 'Negativo', 'neg')
# runProcess(avengers, 'vingadores_2018_04_24_ing_sent/vingadores_2018_04_24_ing_sent_neu', 'vingadores_2018_04_24_ing_sent/', 'vingadores_2018_04_24_tf-neu', 'Neutro', 'neu')
# runProcess(avengers, 'vingadores_2018_04_24_ing_sent/vingadores_2018_04_24_ing_sent_pos', 'vingadores_2018_04_24_ing_sent/', 'vingadores_2018_04_24_tf-pos', 'Positivo', 'pos')
# runProcess(avengers, 'vingadores_2018_04_24_ing_sent/vingadores_2018_04_24_ing_sent_mpos', 'vingadores_2018_04_24_ing_sent/', 'vingadores_2018_04_24_tf-mpos', 'Muito Positivo', 'mpos')

# runProcess(avengers, 'vingadores_2018_04_25_ing_sent/vingadores_2018_04_25_ing_sent_mneg', 'vingadores_2018_04_25_ing_sent/', 'vingadores_2018_04_25_tf-mneg', 'Muito Negativo', 'mneg')
# runProcess(avengers, 'vingadores_2018_04_25_ing_sent/vingadores_2018_04_25_ing_sent_neg', 'vingadores_2018_04_25_ing_sent/', 'vingadores_2018_04_25_tf-neg', 'Negativo', 'neg')
# runProcess(avengers, 'vingadores_2018_04_25_ing_sent/vingadores_2018_04_25_ing_sent_neu', 'vingadores_2018_04_25_ing_sent/', 'vingadores_2018_04_25_tf-neu', 'Neutro', 'neu')
# runProcess(avengers, 'vingadores_2018_04_25_ing_sent/vingadores_2018_04_25_ing_sent_pos', 'vingadores_2018_04_25_ing_sent/', 'vingadores_2018_04_25_tf-pos', 'Positivo', 'pos')
# runProcess(avengers, 'vingadores_2018_04_25_ing_sent/vingadores_2018_04_25_ing_sent_mpos', 'vingadores_2018_04_25_ing_sent/', 'vingadores_2018_04_25_tf-mpos', 'Muito Positivo', 'mpos')

# runProcess(avengers, 'vingadores_2018_04_26_ing_sent/vingadores_2018_04_26_ing_sent_mneg', 'vingadores_2018_04_26_ing_sent/', 'vingadores_2018_04_26_tf-mneg', 'Muito Negativo', 'mneg')
# runProcess(avengers, 'vingadores_2018_04_26_ing_sent/vingadores_2018_04_26_ing_sent_neg', 'vingadores_2018_04_26_ing_sent/', 'vingadores_2018_04_26_tf-neg', 'Negativo', 'neg')
# runProcess(avengers, 'vingadores_2018_04_26_ing_sent/vingadores_2018_04_26_ing_sent_neu', 'vingadores_2018_04_26_ing_sent/', 'vingadores_2018_04_26_tf-neu', 'Neutro', 'neu')
# runProcess(avengers, 'vingadores_2018_04_26_ing_sent/vingadores_2018_04_26_ing_sent_pos', 'vingadores_2018_04_26_ing_sent/', 'vingadores_2018_04_26_tf-pos', 'Positivo', 'pos')
# runProcess(avengers, 'vingadores_2018_04_26_ing_sent/vingadores_2018_04_26_ing_sent_mpos', 'vingadores_2018_04_26_ing_sent/', 'vingadores_2018_04_26_tf-mpos', 'Muito Positivo', 'mpos')

# runProcess(avengers, 'vingadores_2018_04_27_ing_sent/vingadores_2018_04_27_ing_sent_mneg', 'vingadores_2018_04_27_ing_sent/', 'vingadores_2018_04_27_tf-mneg', 'Muito Negativo', 'mneg')
# runProcess(avengers, 'vingadores_2018_04_27_ing_sent/vingadores_2018_04_27_ing_sent_neg', 'vingadores_2018_04_27_ing_sent/', 'vingadores_2018_04_27_tf-neg', 'Negativo', 'neg')
# runProcess(avengers, 'vingadores_2018_04_27_ing_sent/vingadores_2018_04_27_ing_sent_neu', 'vingadores_2018_04_27_ing_sent/', 'vingadores_2018_04_27_tf-neu', 'Neutro', 'neu')
# runProcess(avengers, 'vingadores_2018_04_27_ing_sent/vingadores_2018_04_27_ing_sent_pos', 'vingadores_2018_04_27_ing_sent/', 'vingadores_2018_04_27_tf-pos', 'Positivo', 'pos')
# runProcess(avengers, 'vingadores_2018_04_27_ing_sent/vingadores_2018_04_27_ing_sent_mpos', 'vingadores_2018_04_27_ing_sent/', 'vingadores_2018_04_27_tf-mpos', 'Muito Positivo', 'mpos')

# runProcess(avengers, 'vingadores_2018_04_29_ing_sent/vingadores_2018_04_29_ing_sent_mneg', 'vingadores_2018_04_29_ing_sent/', 'vingadores_2018_04_29_tf-mneg', 'Muito Negativo', 'mneg')
# runProcess(avengers, 'vingadores_2018_04_29_ing_sent/vingadores_2018_04_29_ing_sent_neg', 'vingadores_2018_04_29_ing_sent/', 'vingadores_2018_04_29_tf-neg', 'Negativo', 'neg')
# runProcess(avengers, 'vingadores_2018_04_29_ing_sent/vingadores_2018_04_29_ing_sent_neu', 'vingadores_2018_04_29_ing_sent/', 'vingadores_2018_04_29_tf-neu', 'Neutro', 'neu')
# runProcess(avengers, 'vingadores_2018_04_29_ing_sent/vingadores_2018_04_29_ing_sent_pos', 'vingadores_2018_04_29_ing_sent/', 'vingadores_2018_04_29_tf-pos', 'Positivo', 'pos')
# runProcess(avengers, 'vingadores_2018_04_29_ing_sent/vingadores_2018_04_29_ing_sent_mpos', 'vingadores_2018_04_29_ing_sent/', 'vingadores_2018_04_29_tf-mpos', 'Muito Positivo', 'mpos')

# runProcess(avengers, 'vingadores_2018_04_30_ing_sent/vingadores_2018_04_30_ing_sent_mneg', 'vingadores_2018_04_30_ing_sent/', 'vingadores_2018_04_30_tf-mneg', 'Muito Negativo', 'mneg')
# runProcess(avengers, 'vingadores_2018_04_30_ing_sent/vingadores_2018_04_30_ing_sent_neg', 'vingadores_2018_04_30_ing_sent/', 'vingadores_2018_04_30_tf-neg', 'Negativo', 'neg')
# runProcess(avengers, 'vingadores_2018_04_30_ing_sent/vingadores_2018_04_30_ing_sent_neu', 'vingadores_2018_04_30_ing_sent/', 'vingadores_2018_04_30_tf-neu', 'Neutro', 'neu')
# runProcess(avengers, 'vingadores_2018_04_30_ing_sent/vingadores_2018_04_30_ing_sent_pos', 'vingadores_2018_04_30_ing_sent/', 'vingadores_2018_04_30_tf-pos', 'Positivo', 'pos')
# runProcess(avengers, 'vingadores_2018_04_30_ing_sent/vingadores_2018_04_30_ing_sent_mpos', 'vingadores_2018_04_30_ing_sent/', 'vingadores_2018_04_30_tf-mpos', 'Muito Positivo', 'mpos')

# runProcess(avengers, 'vingadores_2018_05_01_ing_sent/vingadores_2018_05_01_ing_sent_mneg', 'vingadores_2018_05_01_ing_sent/', 'vingadores_2018_05_01_tf-mneg', 'Muito Negativo', 'mneg')
# runProcess(avengers, 'vingadores_2018_05_01_ing_sent/vingadores_2018_05_01_ing_sent_neg', 'vingadores_2018_05_01_ing_sent/', 'vingadores_2018_05_01_tf-neg', 'Negativo', 'neg')
# runProcess(avengers, 'vingadores_2018_05_01_ing_sent/vingadores_2018_05_01_ing_sent_neu', 'vingadores_2018_05_01_ing_sent/', 'vingadores_2018_05_01_tf-neu', 'Neutro', 'neu')
# runProcess(avengers, 'vingadores_2018_05_01_ing_sent/vingadores_2018_05_01_ing_sent_pos', 'vingadores_2018_05_01_ing_sent/', 'vingadores_2018_05_01_tf-pos', 'Positivo', 'pos')
# runProcess(avengers, 'vingadores_2018_05_01_ing_sent/vingadores_2018_05_01_ing_sent_mpos', 'vingadores_2018_05_01_ing_sent/', 'vingadores_2018_05_01_tf-mpos', 'Muito Positivo', 'mpos')

# runProcess(avengers, 'vingadores_2018_05_02_ing_sent/vingadores_2018_05_02_ing_sent_mneg', 'vingadores_2018_05_02_ing_sent/', 'vingadores_2018_05_02_tf-mneg', 'Muito Negativo', 'mneg')
# runProcess(avengers, 'vingadores_2018_05_02_ing_sent/vingadores_2018_05_02_ing_sent_neg', 'vingadores_2018_05_02_ing_sent/', 'vingadores_2018_05_02_tf-neg', 'Negativo', 'neg')
# runProcess(avengers, 'vingadores_2018_05_02_ing_sent/vingadores_2018_05_02_ing_sent_neu', 'vingadores_2018_05_02_ing_sent/', 'vingadores_2018_05_02_tf-neu', 'Neutro', 'neu')
# runProcess(avengers, 'vingadores_2018_05_02_ing_sent/vingadores_2018_05_02_ing_sent_pos', 'vingadores_2018_05_02_ing_sent/', 'vingadores_2018_05_02_tf-pos', 'Positivo', 'pos')
# runProcess(avengers, 'vingadores_2018_05_02_ing_sent/vingadores_2018_05_02_ing_sent_mpos', 'vingadores_2018_05_02_ing_sent/', 'vingadores_2018_05_02_tf-mpos', 'Muito Positivo', 'mpos')

# runProcess(avengers, 'vingadores_2018_05_03_ing_sent/vingadores_2018_05_03_ing_sent_mneg', 'vingadores_2018_05_03_ing_sent/', 'vingadores_2018_05_03_tf-mneg', 'Muito Negativo', 'mneg')
# runProcess(avengers, 'vingadores_2018_05_03_ing_sent/vingadores_2018_05_03_ing_sent_neg', 'vingadores_2018_05_03_ing_sent/', 'vingadores_2018_05_03_tf-neg', 'Negativo', 'neg')
# runProcess(avengers, 'vingadores_2018_05_03_ing_sent/vingadores_2018_05_03_ing_sent_neu', 'vingadores_2018_05_03_ing_sent/', 'vingadores_2018_05_03_tf-neu', 'Neutro', 'neu')
# runProcess(avengers, 'vingadores_2018_05_03_ing_sent/vingadores_2018_05_03_ing_sent_pos', 'vingadores_2018_05_03_ing_sent/', 'vingadores_2018_05_03_tf-pos', 'Positivo', 'pos')
# runProcess(avengers, 'vingadores_2018_05_03_ing_sent/vingadores_2018_05_03_ing_sent_mpos', 'vingadores_2018_05_03_ing_sent/', 'vingadores_2018_05_03_tf-mpos', 'Muito Positivo', 'mpos')

# runProcess(avengers, 'vingadores_2018_05_04_ing_sent/vingadores_2018_05_04_ing_sent_mneg', 'vingadores_2018_05_04_ing_sent/', 'vingadores_2018_05_04_tf-mneg', 'Muito Negativo', 'mneg')
# runProcess(avengers, 'vingadores_2018_05_04_ing_sent/vingadores_2018_05_04_ing_sent_neg', 'vingadores_2018_05_04_ing_sent/', 'vingadores_2018_05_04_tf-neg', 'Negativo', 'neg')
# runProcess(avengers, 'vingadores_2018_05_04_ing_sent/vingadores_2018_05_04_ing_sent_neu', 'vingadores_2018_05_04_ing_sent/', 'vingadores_2018_05_04_tf-neu', 'Neutro', 'neu')
# runProcess(avengers, 'vingadores_2018_05_04_ing_sent/vingadores_2018_05_04_ing_sent_pos', 'vingadores_2018_05_04_ing_sent/', 'vingadores_2018_05_04_tf-pos', 'Positivo', 'pos')
# runProcess(avengers, 'vingadores_2018_05_04_ing_sent/vingadores_2018_05_04_ing_sent_mpos', 'vingadores_2018_05_04_ing_sent/', 'vingadores_2018_05_04_tf-mpos', 'Muito Positivo', 'mpos')

# runProcess(aquaman, 'file_results_twitter/result_aquaman_09_13/result_aquaman_09_13_mpos', 'file_results_twitter/result_aquaman_09_13/', 'tf-mpos', 'Muito Positivo', 'mpos')
# runProcess(aquaman, 'file_results_twitter/result_aquaman_09_13/result_aquaman_09_13_pos', 'file_results_twitter/result_aquaman_09_13/', 'tf-pos', 'Positivo', 'pos')
# runProcess(aquaman, 'file_results_twitter/result_aquaman_09_13/result_aquaman_09_13_neu', 'file_results_twitter/result_aquaman_09_13/', 'tf-neu', 'Neutro', 'neu')
# runProcess(aquaman, 'file_results_twitter/result_aquaman_09_13/result_aquaman_09_13_neg', 'file_results_twitter/result_aquaman_09_13/', 'tf-neg', 'Negativo', 'neg')
# runProcess(aquaman, 'file_results_twitter/result_aquaman_09_13/result_aquaman_09_13_mneg', 'file_results_twitter/result_aquaman_09_13/', 'tf-mneg', 'Muito Negativo', 'mneg')

# runProcess(aquaman, 'file_results_twitter/result_aquaman_03_09/result_aquaman_03_09_mpos', 'file_results_twitter/result_aquaman_03_09/', 'tf-mpos', 'Muito Positivo', 'mpos')
# runProcess(aquaman, 'file_results_twitter/result_aquaman_03_09/result_aquaman_03_09_pos', 'file_results_twitter/result_aquaman_03_09/', 'tf-pos', 'Positivo', 'pos')
# runProcess(aquaman, 'file_results_twitter/result_aquaman_03_09/result_aquaman_03_09_neu', 'file_results_twitter/result_aquaman_03_09/', 'tf-neu', 'Neutro', 'neu')
# runProcess(aquaman, 'file_results_twitter/result_aquaman_03_09/result_aquaman_03_09_neg', 'file_results_twitter/result_aquaman_03_09/', 'tf-neg', 'Negativo', 'neg')
# runProcess(aquaman, 'file_results_twitter/result_aquaman_03_09/result_aquaman_03_09_mneg', 'file_results_twitter/result_aquaman_03_09/', 'tf-mneg', 'Muito Negativo', 'mneg')

# runProcess(aquaman, 'file_results_twitter/result_aquaman_14_15/result_aquaman_14_15_mpos', 'file_results_twitter/result_aquaman_14_15/', 'tf-mpos', 'Muito Positivo', 'mpos')
# runProcess(aquaman, 'file_results_twitter/result_aquaman_14_15/result_aquaman_14_15_pos', 'file_results_twitter/result_aquaman_14_15/', 'tf-pos', 'Positivo', 'pos')
# runProcess(aquaman, 'file_results_twitter/result_aquaman_14_15/result_aquaman_14_15_neu', 'file_results_twitter/result_aquaman_14_15/', 'tf-neu', 'Neutro', 'neu')
# runProcess(aquaman, 'file_results_twitter/result_aquaman_14_15/result_aquaman_14_15_neg', 'file_results_twitter/result_aquaman_14_15/', 'tf-neg', 'Negativo', 'neg')
# runProcess(aquaman, 'file_results_twitter/result_aquaman_14_15/result_aquaman_14_15_mneg', 'file_results_twitter/result_aquaman_14_15/', 'tf-mneg', 'Muito Negativo', 'mneg')

# runProcess(aquaman, 'file_results_twitter/result_aquaman_16_17/result_aquaman_16_17_mpos', 'file_results_twitter/result_aquaman_16_17/', 'tf-mpos', 'Muito Positivo', 'mpos')
# runProcess(aquaman, 'file_results_twitter/result_aquaman_16_17/result_aquaman_16_17_pos', 'file_results_twitter/result_aquaman_16_17/', 'tf-pos', 'Positivo', 'pos')
# runProcess(aquaman, 'file_results_twitter/result_aquaman_16_17/result_aquaman_16_17_neu', 'file_results_twitter/result_aquaman_16_17/', 'tf-neu', 'Neutro', 'neu')
# runProcess(aquaman, 'file_results_twitter/result_aquaman_16_17/result_aquaman_16_17_neg', 'file_results_twitter/result_aquaman_16_17/', 'tf-neg', 'Negativo', 'neg')
# runProcess(aquaman, 'file_results_twitter/result_aquaman_16_17/result_aquaman_16_17_mneg', 'file_results_twitter/result_aquaman_16_17/', 'tf-mneg', 'Muito Negativo', 'mneg')

# runProcess(aquaman, 'file_results_youtube/result_aquaman_youtube_mneg', 'file_results_youtube/', 'tf-mneg', 'Muito Negativo')
# runProcess(aquaman, 'file_results_youtube/result_aquaman_youtube_mpos', 'file_results_youtube/', 'tf-mpos', 'Muito Positivo')

# runProcess(captain, 'result_captain_youtube_mneg', '', 'tf-mneg', 'Muito Negativo')
# runProcess(captain, 'result_captain_youtube_neg', '', 'tf-neg', 'Negativo')
# runProcess(captain, 'result_captain_youtube_pos', '', 'tf-pos', 'Positivo')
# runProcess(captain, 'result_captain_youtube_mpos', '', 'tf-mpos', 'Muito Positivo')

runProcess(avengers, 'result_avengers_youtube_mneg', '', 'result_avengers_youtube_tf-mneg', 'Muito Negativo', 'mneg')
runProcess(avengers, 'result_avengers_youtube_mpos', '', 'result_avengers_youtube_tf-mpos', 'Muito Positivo', 'mpos')
runProcess(avengers, 'result_avengers_youtube_pos', '', 'result_avengers_youtube_tf-pos', 'Positivo', 'pos')
runProcess(avengers, 'result_avengers_youtube_neg', '', 'result_avengers_youtube_tf-neg', 'Negativo', 'neg')
runProcess(avengers, 'result_avengers_youtube_neu', '', 'result_avengers_youtube_tf-neu', 'Neutro', 'neu')

# runProcess(captain, 'result_captainmarvel_03-10_03-12/result_captainmarvel_03-10_03-12_mneg', '', 'result_captainmarvel_03-10_03-12/result_captainmarvel_03-10_03-12_tf-mneg', 'Muito Negativo', 'mneg')
# runProcess(captain, 'result_captainmarvel_03-10_03-12/result_captainmarvel_03-10_03-12_neg', '', 'result_captainmarvel_03-10_03-12/result_captainmarvel_03-10_03-12_tf-neg', 'Negativo', 'neg')
# runProcess(captain, 'result_captainmarvel_03-10_03-12/result_captainmarvel_03-10_03-12_neu', '', 'result_captainmarvel_03-10_03-12/result_captainmarvel_03-10_03-12_tf-neu', 'Neutro', 'neu')
# runProcess(captain, 'result_captainmarvel_03-10_03-12/result_captainmarvel_03-10_03-12_pos', '', 'result_captainmarvel_03-10_03-12/result_captainmarvel_03-10_03-12_tf-pos', 'Positivo', 'pos')
# runProcess(captain, 'result_captainmarvel_03-10_03-12/result_captainmarvel_03-10_03-12_mpos', '', 'result_captainmarvel_03-10_03-12/result_captainmarvel_03-10_03-12_tf-mpos', 'Muito Positivo', 'mpos')

# runProcess(captain, 'result_captainmarvel_03-13/result_captainmarvel_03-13_mneg', '', 'result_captainmarvel_03-13/result_captainmarvel_03-13_tf-mneg', 'Muito Negativo', 'mneg')
# runProcess(captain, 'result_captainmarvel_03-13/result_captainmarvel_03-13_neg', '', 'result_captainmarvel_03-13/result_captainmarvel_03-13_tf-neg', 'Negativo', 'neg')
# runProcess(captain, 'result_captainmarvel_03-13/result_captainmarvel_03-13_neu', '', 'result_captainmarvel_03-13/result_captainmarvel_03-13_tf-neu', 'Neutro', 'neu')
# runProcess(captain, 'result_captainmarvel_03-13/result_captainmarvel_03-13_pos', '', 'result_captainmarvel_03-13/result_captainmarvel_03-13_tf-pos', 'Positivo', 'pos')
# runProcess(captain, 'result_captainmarvel_03-13/result_captainmarvel_03-13_mpos', '', 'result_captainmarvel_03-13/result_captainmarvel_03-13_tf-mpos', 'Muito Positivo', 'mpos')

# runProcess(captain, 'result_captainmarvel_03-14_03-15/result_captainmarvel_03-14_03-15_mneg', '', 'result_captainmarvel_03-14_03-15/result_captainmarvel_03-14_03-15_tf-mneg', 'Muito Negativo', 'mneg')
# runProcess(captain, 'result_captainmarvel_03-14_03-15/result_captainmarvel_03-14_03-15_neg', '', 'result_captainmarvel_03-14_03-15/result_captainmarvel_03-14_03-15_tf-neg', 'Negativo', 'neg')
# runProcess(captain, 'result_captainmarvel_03-14_03-15/result_captainmarvel_03-14_03-15_neu', '', 'result_captainmarvel_03-14_03-15/result_captainmarvel_03-14_03-15_tf-neu', 'Neutro', 'neu')
# runProcess(captain, 'result_captainmarvel_03-14_03-15/result_captainmarvel_03-14_03-15_pos', '', 'result_captainmarvel_03-14_03-15/result_captainmarvel_03-14_03-15_tf-pos', 'Positivo', 'pos')
# runProcess(captain, 'result_captainmarvel_03-14_03-15/result_captainmarvel_03-14_03-15_mpos', '', 'result_captainmarvel_03-14_03-15/result_captainmarvel_03-14_03-15_tf-mpos', 'Muito Positivo', 'mpos')

# runProcess(captain, 'result_captainmarvel_03-18/result_captainmarvel_03-18_mneg', '', 'result_captainmarvel_03-18/result_captainmarvel_03-18_tf-mneg', 'Muito Negativo', 'mneg')
# runProcess(captain, 'result_captainmarvel_03-18/result_captainmarvel_03-18_neg', '', 'result_captainmarvel_03-18/result_captainmarvel_03-18_tf-neg', 'Negativo', 'neg')
# runProcess(captain, 'result_captainmarvel_03-18/result_captainmarvel_03-18_neu', '', 'result_captainmarvel_03-18/result_captainmarvel_03-18_tf-neu', 'Neutro', 'neu')
# runProcess(captain, 'result_captainmarvel_03-18/result_captainmarvel_03-18_pos', '', 'result_captainmarvel_03-18/result_captainmarvel_03-18_tf-pos', 'Positivo', 'pos')
# runProcess(captain, 'result_captainmarvel_03-18/result_captainmarvel_03-18_mpos', '', 'result_captainmarvel_03-18/result_captainmarvel_03-18_tf-mpos', 'Muito Positivo', 'mpos')

# runProcess(captain, 'result_captain_youtube_mpos', '', 'tf-mpos', 'Muito Positivo', 'mpos')
# runProcess(captain, 'result_captain_youtube_pos', '', 'tf-pos', 'Positivo', 'pos')
# runProcess(captain, 'result_captain_youtube_neu', '', 'tf-neu', 'Neutro', 'neu')
# runProcess(captain, 'result_captain_youtube_neg', '', 'tf-neg', 'Negativo', 'neg')
# runProcess(captain, 'result_captain_youtube_mneg', '', 'tf-mneg', 'Muito Negativo', 'mneg')

# runProcess(aquaman, 'file_results_youtube/result_aquaman_youtube_mpos', '', 'file_results_youtube/tf-mpos', 'Muito Positivo', 'mpos')
# runProcess(aquaman, 'file_results_youtube/result_aquaman_youtube_pos', '', 'file_results_youtube/tf-pos', 'Positivo', 'pos')
# runProcess(aquaman, 'file_results_youtube/result_aquaman_youtube_neu', '', 'file_results_youtube/tf-neu', 'Neutro', 'neu')
# runProcess(aquaman, 'file_results_youtube/result_aquaman_youtube_neg', '', 'file_results_youtube/tf-neg', 'Negativo', 'neg')
# runProcess(aquaman, 'file_results_youtube/result_aquaman_youtube_mneg', '', 'file_results_youtube/tf-mneg', 'Muito Negativo', 'mneg')