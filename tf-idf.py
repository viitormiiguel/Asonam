import sys 
import codecs
import nltk
from nltk.corpus import stopwords
from nltk import pos_tag, word_tokenize
import csv
import datetime
from collections import Counter
import re
import math
from textblob import TextBlob as tb

c = 'Data/aquaman-tweets/aquaman/'
d = 'Data/captain-tweets/'

default_stopwords = set(nltk.corpus.stopwords.words('english'))

def RemoveStopWords(instancia):
    instancia  = instancia.lower()
    stopwords = set(nltk.corpus.stopwords.words('english'))
    palavras = [i for i in instancia.split() if not i in stopwords]
    return (" ".join(palavras))

def preProcess(txt):
    # Conversao para minusculos
    frase = txt.lower()
    # Remover urls
    frase = re.sub(r"http\S+", "", frase)
    # Remoção $ e %
    frase = re.sub('[R$%]','',frase)
    # Remoção de numeros
    frase = re.sub('[-10-9]','', frase)
    # Remoçao de pontuação
    frase = re.sub(r'[-./?!,":;()\']','',frase)
    # Remoção de stopwords
    frase = re.sub('[➖]','',frase)
    texto = RemoveStopWords(frase)
    return texto

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf (word, bloblist)

def algo(b, f):
    f1 = open(c + 'file_results_youtube/' + f + '.txt', 'a+', encoding="utf8")
    for i, blob in enumerate(b):
        print("Top words in document {}".format(i + 1))
        scores = {word: tfidf(word, blob, b) for word in blob.words}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        for word, score in sorted_words[:50]:
            print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
            f1.write(word + '\n')

    f1.close()

def divideDataset(fonte):
    bl1 = []
    bl2 = []
    doc1 = ""
    doc2 = ""
    with open(fonte + 'dataset.csv', encoding="utf8") as dados:
        reader = csv.reader(dados)
        next(reader)
        d1 = [t for t in reader] 
        for d in d1:
            if d:
                try:                    
                    if 'Positivo' in d[1]:
                        d1 = preProcess(d[0])
                        doc1 += "\n" + d1
                        t1 = tb(doc1)
                        bl1 = [t1]
                    if 'Negativo' in d[1]:
                        d2 = preProcess(d[0])
                        doc2 += "\n" + d2
                        t2 = tb(doc2)
                        bl2 = [t2]
                except IndexError:
                    _ = 'null'
        algo(bl2, 'n')
        algo(bl1, 'p')

# divideDataset(c)

aquaman = "Data/aquaman-tweets/aquaman/"
captain = "Data/captain-tweets/"

def getFiles(p, f, t):
    doc = ""
    b = []
    with open(p + f, encoding='utf8') as file:
        for line in file:
            try:
                line = line.split(',')
                if line[2]:
                    l = preProcess(line[2])
                    doc += "\n" + l
                    t1 = tb(doc)
                    b = [t1]
            except IndexError:
                _ = 'null'
        algo(b, t)
        # algo(bl2, 'n')
        # algo(bl1, 'p')


# getFiles(aquaman, 'file_results_youtube/result_aquaman_youtube_mneg.txt', 'tfidf-mneg')
getFiles(aquaman, 'file_results_youtube/result_aquaman_youtube_neg.txt', 'tfidf-neg')
getFiles(aquaman, 'file_results_youtube/result_aquaman_youtube_neu.txt', 'tfidf-neu')
getFiles(aquaman, 'file_results_youtube/result_aquaman_youtube_pos.txt', 'tfidf-pos')
getFiles(aquaman, 'file_results_youtube/result_aquaman_youtube_mpos.txt', 'tfidf-mpos')

getFiles(captain, 'file_results_youtube/result_captain_youtube_mneg.txt', 'tfidf-mneg')
getFiles(captain, 'file_results_youtube/result_captain_youtube_neg.txt', 'tfidf-neg')
getFiles(captain, 'file_results_youtube/result_captain_youtube_neu.txt', 'tfidf-neu')
getFiles(captain, 'file_results_youtube/result_captain_youtube_pos.txt', 'tfidf-pos')
getFiles(captain, 'file_results_youtube/result_aquaman_youtube_mpos.txt', 'tfidf-mpos')

# divideDataset(c + '/file_results_youtube/result_aquaman_youtube_pos.txt')
