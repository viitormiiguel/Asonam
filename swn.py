import nltk
import re
import csv 
# import ijson
import json
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn
from nltk import sent_tokenize, word_tokenize, pos_tag

lemmatizer = WordNetLemmatizer()

def swn_pos(tag):
    if tag.startswith('J'):
        return wn.ADJ
    elif tag.startswith('N'):
        return wn.NOUN
    elif tag.startswith('R'):
        return wn.ADV
    elif tag.startswith('V'):
        return wn.VERB
    return None

def RemoveStopWords(instancia):
    instancia  = instancia.lower()
    stopwords = set(nltk.corpus.stopwords.words('english'))
    palavras = [i for i in instancia.split() if not i in stopwords]
    return (" ".join(palavras))

def clean_text(text):
    text = text.lower()
    text = re.sub('[-10-9]','', text)
    text = re.sub(r'[-./?!,":;()\']','',text)
    text = RemoveStopWords(text)
    return text

def swn_polaridade(text):
    text = str(text).encode().decode()
    sentiment = 0.0
    tokens_c = 0.0
    text = clean_text(text)
    raw_texts = sent_tokenize(text)
    for raw_text in raw_texts:
        tag_text = pos_tag(word_tokenize(raw_text))
        # print(tag_text)
        for word, tag in tag_text:
            wn_tag = swn_pos(tag)
            if wn_tag not in (wn.NOUN, wn.ADJ, wn.ADV):
                continue 
            lemma = lemmatizer.lemmatize(word, pos=wn_tag)
            if not lemma:
                continue
            synsets = wn.synsets(lemma, pos=wn_tag)
            if not synsets:
                continue
            synset = synsets[0]
            swn_synset = swn.senti_synset(synset.name())
            sentiment += swn_synset.pos_score() - swn_synset.neg_score()
            tokens_c += 1
        # print(sentiment)
        if not tokens_c:
            return 0
        if sentiment > 0:
            return 'Positivo, Score: ', sentiment
        if sentiment < 0:
            return 'Negativo, Score: ', sentiment
        if sentiment == 0:
            return 'Neutro, Score: ', sentiment

# print(swn_polaridade("I was hoping to have a good real One V. One with the avengers and black order in infinity  but I guess I have to"))

c = 'Data/avengers-tweets/no_war/'
d = 'Data/aquaman-tweets/aquaman/'

def dataAvengers(c, arq):
    with open(c + arq + '.json', 'r') as f:
        ds = json.load(f)
    with open(c + arq + '.csv', mode='w', encoding="utf8") as fc:
        fc = csv.writer(fc, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for d in ds:
            try:
                x = swn_polaridade(d['sentence'])
                y = d['sentence']
                x = str(x)
                fc.writerow([y, x])
            except IndexError:
                x = 'null'

def dataAquaman(d, arq):
    with open(d + arq +'.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        dataInfo = [r for r in reader]
    with open(d + 't' + arq + '.csv', mode='w', encoding="utf8") as fc:
        fc = csv.writer(fc, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for t in dataInfo:
            # print(t[4])
            try:
                x = swn_polaridade(t[4])
                y = t[4]
                x = str(x)
                fc.writerow([y, x])
            except IndexError:
                x = 'null'

print("Analisando tweets AQUAMAN")
dataAquaman(d, "aquaman_03_09")
dataAquaman(d, "aquaman_09_13")
dataAquaman(d, "aquaman_14_15")
dataAquaman(d, "aquaman_16_17")
print("Analise concluida!")

# Antes da estreia
# print("Analisando antes estreia...")
# dataAvengers(c, "vingadores_2018_04_20_ing_sent")
# dataAvengers(c, "vingadores_2018_04_21_ing_sent")
# dataAvengers(c, "vingadores_2018_04_22_ing_sent")
# dataAvengers(c, "vingadores_2018_04_23_ing_sent")
# dataAvengers(c, "vingadores_2018_04_24_ing_sent")
# dataAvengers(c, "vingadores_2018_04_25_ing_sent")
# dataAvengers(c, "vingadores_2018_04_26_ing_sent")
# dataAvengers(c, "vingadores_2018_04_27_ing_sent")

# # Depois da estreia
# print("Analisando depois estreia...")
# dataAvengers(c, "vingadores_2018_04_30_ing_sent")
# dataAvengers(c, "vingadores_2018_05_01_ing_sent")
# dataAvengers(c, "vingadores_2018_05_02_ing_sent")
# dataAvengers(c, "vingadores_2018_05_03_ing_sent")
# dataAvengers(c, "vingadores_2018_05_04_ing_sent")

# print("Analise finalizada!")