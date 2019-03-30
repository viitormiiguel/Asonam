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

def getImportanWords(c, d, p, q):
        document_text = open(c + d + '.txt', 'r')
        arrayWords = []
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
        print('\n')
        print(q)
        for word in arrayWords:
                for texto in p:
                        if word in texto:
                                contagem += 1        
                print('Palavra: ' + word + ' contagem ' + str(contagem))

        return arrayWords


def runProcess(c, d, d1, e, f):
        doc = open(c + d + '.txt', 'r')
        arrayW = []
        for p in vip:
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
        getImportanWords(avengers, d1 + e, arrayW, f)
        return arrayW

runProcess(avengers, 'vingadores_2018_04_22_ing_sent/vingadores_2018_04_22_ing_sent_mneg', 'vingadores_2018_04_22_ing_sent/', 'vingadores_2018_04_22_tf-mneg', 'Muito Negativo')
runProcess(avengers, 'vingadores_2018_04_30_ing_sent/vingadores_2018_04_30_ing_sent_mneg', 'vingadores_2018_04_30_ing_sent/', 'vingadores_2018_04_30_tf-mpos', 'Muito Positivo')
