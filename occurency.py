import re
import string
import nltk
from nltk.corpus import stopwords
from nltk import pos_tag, word_tokenize

aquaman = "Data/aquaman-tweets/aquaman/"
captain = "Data/captain-tweets/"
avengers = "Data/avengers-tweets/no_war/"

people = ['Iron Man', 'Thor', 'Hulk', 'Captain America', 'Black Widow', 'War Machine', 'Doctor Strange',
'Spider-Man', 'Black Panther', 'Gamora', 'Nebula', 'Loki', 'Vision', 'Scarlet Witch', 'Falcon', 'Winter Soldier', 'Heimdall',
'Okoye', 'Eitri', 'Wong', 'Mantis', 'Drax', 'Groot', 'Rocket', 'Pepper Potts', 'The Collector', 'Thanos', 'Star-Lord']

vip = ['Iron Man', 'Thor', 'Hulk', 'Captain America', 'Black Widow', 'Doctor Strange', 'Spider-Man', 'Gamora', 'Thanos']

aq = ['Arthur', 'Mera', 'Vulko', 'King Orm', 'Atlanna', 'King Nereus', 'Manta', 'Tom Curry', 'Captain Murk', 'Jesse', 'Dr. Stephen Shin',
'King Atlan', 'Cargo Pilot']

cap = ['Carol Danvers', 'Vers', 'Captain Marvel', 'Nick Fury', 'Talos', 'Keller', 'Yon-Rogg', 'Supreme Intelligence', 'Dr. Wendy Lawson', 'Maria Rambeau',
'Agent Coulson', 'Bron-Char', 'Minn-Erva', 'Att-Lass', 'Korath', 'Ronan', 'Soh-Larr', 'Norex', 'Monica Rambeau']

def getImportanWords(c, d, p, q, vip):
        document_text = open(c + d + '.txt', 'r')
        arrayWords = []
        f1 = open(c + 'oc-pos-yt.txt', 'a+')
        for dt in document_text.readlines():
                t = dt.split()
                txt = t[1][0:len(t[1])-4]
                t1 = t[0][2:len(t[0])-1]
                t1 = t1.replace("'","")

                t2 = str(t[1][5:])
                t2 = t2[t2.find(','):]
                t2 = t2[1:]

                if txt.find('JJ') == 1: 
                        if int(t2) > 100:
                                arrayWords.append(t1)

        contagem = 0
        # print('\n')
        # print(q)
        for word in arrayWords:
                for texto in p:
                        if word in texto and vip in texto:
                                contagem += 1        
                # print('Palavra: ' + word + ' contagem ' + str(contagem) + ' personagem: ' + vip)
                resp = 'Palavra: ' + word + ' contagem ' + str(contagem) + ' personagem: ' + vip + '\n'
                f1.write(resp)
        f1.close

        return arrayWords


def runProcess(c, d, d1, e, f):
        doc = open(c + d + '.txt', 'r')
        arrayW = []
        # varre array de personagens
        for p in cap:
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
                # print(arrayW)
                getImportanWords(c, d1 + e, arrayW, f, p)
        return arrayW

# runProcess(avengers, 'vingadores_2018_04_30_ing_sent/vingadores_2018_04_30_ing_sent_mneg', 'vingadores_2018_04_30_ing_sent/', 'vingadores_2018_04_30_tf-mneg', 'Muito Negativo')
# runProcess(avengers, 'vingadores_2018_04_30_ing_sent/vingadores_2018_04_30_ing_sent_mpos', 'vingadores_2018_04_30_ing_sent/', 'vingadores_2018_04_30_tf-mpos', 'Muito Positivo')

# runProcess(aquaman, 'file_results_twitter/result_aquaman_09_13/result_aquaman_09_13_mpos', 'file_results_twitter/result_aquaman_09_13/', 'tf-mpos', 'Muito Positivo')
# runProcess(aquaman, 'file_results_twitter/result_aquaman_09_13/result_aquaman_09_13_mneg', 'file_results_twitter/result_aquaman_09_13/', 'tf-mneg', 'Muito Neg')

# runProcess(aquaman, 'file_results_youtube/result_aquaman_youtube_mneg', 'file_results_youtube/', 'tf-mneg', 'Muito Negativo')
# runProcess(aquaman, 'file_results_youtube/result_aquaman_youtube_mpos', 'file_results_youtube/', 'tf-mpos', 'Muito Positivo')

# runProcess(captain, 'result_captain_youtube_mneg', '', 'tf-mneg', 'Muito Negativo')
runProcess(captain, 'result_captain_youtube_mpos', '', 'tf-mpos', 'Muito Positivo')
