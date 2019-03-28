import re
import string
import nltk
from nltk.corpus import stopwords
from nltk import pos_tag, word_tokenize

c1 = 'Data/aquaman-tweets/aquaman/file_results_youtube/'
c2 = 'Data/aquaman-tweets/aquaman/file_results_twitter/'
c3 = 'Data/captain-tweets/'
c4 = 'Data/avengers-tweets/no_war/'

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
    # Remocao $ e %
    frase = re.sub('[R$%]','',frase)
    # Remocao de numeros
    frase = re.sub('[-10-9]','', frase)
    # Remocao de pontuacao
    frase = re.sub(r'[-./?!,":;()\']','',frase)
    # Remocao de stopwords
    texto = RemoveStopWords(frase)
    return texto
 
def runProcess(c, d, e):
    frequency = {}
    document_text = open(c + d + '.txt', 'r')
    text_string = document_text.read().lower()
    text_string = preProcess(text_string)
    match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
    print(match_pattern)
    f1 = open(c + e + '.txt', 'a+')

    for word in match_pattern:
        word = word.replace('tz','')
        count = frequency.get(word,0)
        frequency[word] = count + 1
        
        
    # frequency_list = frequency.keys()
    
    # for words in frequency_list:
    #     if frequency[words] > 50:
    #         txt = nltk.word_tokenize(words)
    #         f1.write(str(nltk.pos_tag(txt)) + ',' + str(frequency[words]) + '\n')
    # f1.close()

# runProcess(c1, 'result_aquaman_youtube_mneg', 'tf-mneg')
# runProcess(c1, 'result_aquaman_youtube_neg', 'tf-neg')
# runProcess(c1, 'result_aquaman_youtube_neu', 'tf-neu')
# runProcess(c1, 'result_aquaman_youtube_pos', 'tf-pos')
# runProcess(c1, 'result_aquaman_youtube_mpos', 'tf-mpos')

# runProcess(c2, 'result_aquaman_03_09/result_aquaman_03_09_mneg', 'result_aquaman_03_09/tf-mneg')
# runProcess(c2, 'result_aquaman_03_09/result_aquaman_03_09_neg', 'result_aquaman_03_09/tf-neg')
# runProcess(c2, 'result_aquaman_03_09/result_aquaman_03_09_neu', 'result_aquaman_03_09/tf-neu')
# runProcess(c2, 'result_aquaman_03_09/result_aquaman_03_09_pos', 'result_aquaman_03_09/tf-pos')
# runProcess(c2, 'result_aquaman_03_09/result_aquaman_03_09_mpos', 'result_aquaman_03_09/tf-mpos')

# runProcess(c2, 'result_aquaman_09_13/result_aquaman_09_13_mneg', 'result_aquaman_09_13/tf-mneg')
# runProcess(c2, 'result_aquaman_09_13/result_aquaman_09_13_neg', 'result_aquaman_09_13/tf-neg')
# runProcess(c2, 'result_aquaman_09_13/result_aquaman_09_13_neu', 'result_aquaman_09_13/tf-neu')
# runProcess(c2, 'result_aquaman_09_13/result_aquaman_09_13_pos', 'result_aquaman_09_13/tf-pos')
# runProcess(c2, 'result_aquaman_09_13/result_aquaman_09_13_mpos', 'result_aquaman_09_13/tf-mpos')

# runProcess(c2, 'result_aquaman_14_15/result_aquaman_14_15_mneg', 'result_aquaman_14_15/tf-mneg')
# runProcess(c2, 'result_aquaman_14_15/result_aquaman_14_15_neg', 'result_aquaman_14_15/tf-neg')
# runProcess(c2, 'result_aquaman_14_15/result_aquaman_14_15_neu', 'result_aquaman_14_15/tf-neu')
# runProcess(c2, 'result_aquaman_14_15/result_aquaman_14_15_pos', 'result_aquaman_14_15/tf-pos')
# runProcess(c2, 'result_aquaman_14_15/result_aquaman_14_15_mpos', 'result_aquaman_14_15/tf-mpos')

# runProcess(c2, 'result_aquaman_16_17/result_aquaman_16_17_mneg', 'result_aquaman_16_17/tf-mneg')
# runProcess(c2, 'result_aquaman_16_17/result_aquaman_16_17_neg', 'result_aquaman_16_17/tf-neg')
# runProcess(c2, 'result_aquaman_16_17/result_aquaman_16_17_neu', 'result_aquaman_16_17/tf-neu')
# runProcess(c2, 'result_aquaman_16_17/result_aquaman_16_17_pos', 'result_aquaman_16_17/tf-pos')
# runProcess(c2, 'result_aquaman_16_17/result_aquaman_16_17_mpos', 'result_aquaman_16_17/tf-mpos')

runProcess(c3, 'result_captain_youtube_mneg', 'tf-mneg')
# runProcess(c3, 'result_captain_youtube_neg', 'tf-neg')
# runProcess(c3, 'result_captain_youtube_neu', 'tf-neu')
# runProcess(c3, 'result_captain_youtube_pos', 'tf-pos')
# runProcess(c3, 'result_captain_youtube_mpos', 'tf-mpos')

# runProcess(c4, 'vingadores_2018_04_20_ing_sent/vingadores_2018_04_20_ing_sent_mneg', 'vingadores_2018_04_20_tf-mneg')
# runProcess(c4, 'vingadores_2018_04_20_ing_sent/vingadores_2018_04_20_ing_sent_neg', 'vingadores_2018_04_20_tf-neg')
# runProcess(c4, 'vingadores_2018_04_20_ing_sent/vingadores_2018_04_20_ing_sent_neu', 'vingadores_2018_04_20_tf-neu')
# runProcess(c4, 'vingadores_2018_04_20_ing_sent/vingadores_2018_04_20_ing_sent_pos', 'vingadores_2018_04_20_tf-pos')
# runProcess(c4, 'vingadores_2018_04_20_ing_sent/vingadores_2018_04_20_ing_sent_mpos', 'vingadores_2018_04_20_tf-mpos')

# runProcess(c4, 'vingadores_2018_04_21_ing_sent/vingadores_2018_04_21_ing_sent_mneg', 'vingadores_2018_04_21_tf-mneg')
# runProcess(c4, 'vingadores_2018_04_21_ing_sent/vingadores_2018_04_21_ing_sent_neg', 'vingadores_2018_04_21_tf-neg')
# runProcess(c4, 'vingadores_2018_04_21_ing_sent/vingadores_2018_04_21_ing_sent_neu', 'vingadores_2018_04_21_tf-neu')
# runProcess(c4, 'vingadores_2018_04_21_ing_sent/vingadores_2018_04_21_ing_sent_pos', 'vingadores_2018_04_21_tf-pos')
# runProcess(c4, 'vingadores_2018_04_21_ing_sent/vingadores_2018_04_21_ing_sent_mpos', 'vingadores_2018_04_21_tf-mpos')

# runProcess(c4, 'vingadores_2018_04_22_ing_sent/vingadores_2018_04_22_ing_sent_mneg', 'vingadores_2018_04_22_tf-mneg')
# runProcess(c4, 'vingadores_2018_04_22_ing_sent/vingadores_2018_04_22_ing_sent_neg', 'vingadores_2018_04_22_tf-neg')
# runProcess(c4, 'vingadores_2018_04_22_ing_sent/vingadores_2018_04_22_ing_sent_neu', 'vingadores_2018_04_22_tf-neu')
# runProcess(c4, 'vingadores_2018_04_22_ing_sent/vingadores_2018_04_22_ing_sent_pos', 'vingadores_2018_04_22_tf-pos')
# runProcess(c4, 'vingadores_2018_04_22_ing_sent/vingadores_2018_04_22_ing_sent_mpos', 'vingadores_2018_04_22_tf-mpos')

# runProcess(c4, 'vingadores_2018_04_23_ing_sent/vingadores_2018_04_23_ing_sent_mneg', 'vingadores_2018_04_23_tf-mneg')
# runProcess(c4, 'vingadores_2018_04_23_ing_sent/vingadores_2018_04_23_ing_sent_neg', 'vingadores_2018_04_23_tf-neg')
# runProcess(c4, 'vingadores_2018_04_23_ing_sent/vingadores_2018_04_23_ing_sent_neu', 'vingadores_2018_04_23_tf-neu')
# runProcess(c4, 'vingadores_2018_04_23_ing_sent/vingadores_2018_04_23_ing_sent_pos', 'vingadores_2018_04_23_tf-pos')
# runProcess(c4, 'vingadores_2018_04_23_ing_sent/vingadores_2018_04_23_ing_sent_mpos', 'vingadores_2018_04_23_tf-mpos')

# runProcess(c4, 'vingadores_2018_04_24_ing_sent/vingadores_2018_04_24_ing_sent_mneg', 'vingadores_2018_04_24_tf-mneg')
# runProcess(c4, 'vingadores_2018_04_24_ing_sent/vingadores_2018_04_24_ing_sent_neg', 'vingadores_2018_04_24_tf-neg')
# runProcess(c4, 'vingadores_2018_04_24_ing_sent/vingadores_2018_04_24_ing_sent_neu', 'vingadores_2018_04_24_tf-neu')
# runProcess(c4, 'vingadores_2018_04_24_ing_sent/vingadores_2018_04_24_ing_sent_pos', 'vingadores_2018_04_24_tf-pos')
# runProcess(c4, 'vingadores_2018_04_24_ing_sent/vingadores_2018_04_24_ing_sent_mpos', 'vingadores_2018_04_24_tf-mpos')

# runProcess(c4, 'vingadores_2018_04_25_ing_sent/vingadores_2018_04_25_ing_sent_mneg', 'vingadores_2018_04_25_tf-mneg')
# runProcess(c4, 'vingadores_2018_04_25_ing_sent/vingadores_2018_04_25_ing_sent_neg', 'vingadores_2018_04_25_tf-neg')
# runProcess(c4, 'vingadores_2018_04_25_ing_sent/vingadores_2018_04_25_ing_sent_neu', 'vingadores_2018_04_25_tf-neu')
# runProcess(c4, 'vingadores_2018_04_25_ing_sent/vingadores_2018_04_25_ing_sent_pos', 'vingadores_2018_04_25_tf-pos')
# runProcess(c4, 'vingadores_2018_04_25_ing_sent/vingadores_2018_04_25_ing_sent_mpos', 'vingadores_2018_04_25_tf-mpos')

# runProcess(c4, 'vingadores_2018_04_26_ing_sent/vingadores_2018_04_26_ing_sent_mneg', 'vingadores_2018_04_26_tf-mneg')
# runProcess(c4, 'vingadores_2018_04_26_ing_sent/vingadores_2018_04_26_ing_sent_neg', 'vingadores_2018_04_26_tf-neg')
# runProcess(c4, 'vingadores_2018_04_26_ing_sent/vingadores_2018_04_26_ing_sent_neu', 'vingadores_2018_04_26_tf-neu')
# runProcess(c4, 'vingadores_2018_04_26_ing_sent/vingadores_2018_04_26_ing_sent_pos', 'vingadores_2018_04_26_tf-pos')
# runProcess(c4, 'vingadores_2018_04_26_ing_sent/vingadores_2018_04_26_ing_sent_mpos', 'vingadores_2018_04_26_tf-mpos')

# runProcess(c4, 'vingadores_2018_04_27_ing_sent/vingadores_2018_04_27_ing_sent_mneg', 'vingadores_2018_04_27_tf-mneg')
# runProcess(c4, 'vingadores_2018_04_27_ing_sent/vingadores_2018_04_27_ing_sent_neg', 'vingadores_2018_04_27_tf-neg')
# runProcess(c4, 'vingadores_2018_04_27_ing_sent/vingadores_2018_04_27_ing_sent_neu', 'vingadores_2018_04_27_tf-neu')
# runProcess(c4, 'vingadores_2018_04_27_ing_sent/vingadores_2018_04_27_ing_sent_pos', 'vingadores_2018_04_27_tf-pos')
# runProcess(c4, 'vingadores_2018_04_27_ing_sent/vingadores_2018_04_27_ing_sent_mpos', 'vingadores_2018_04_27_tf-mpos')

# runProcess(c4, 'vingadores_2018_04_29_ing_sent/vingadores_2018_04_29_ing_sent_mneg', 'vingadores_2018_04_29_tf-mneg')
# runProcess(c4, 'vingadores_2018_04_29_ing_sent/vingadores_2018_04_29_ing_sent_neg', 'vingadores_2018_04_29_tf-neg')
# runProcess(c4, 'vingadores_2018_04_29_ing_sent/vingadores_2018_04_29_ing_sent_neu', 'vingadores_2018_04_29_tf-neu')
# runProcess(c4, 'vingadores_2018_04_29_ing_sent/vingadores_2018_04_29_ing_sent_pos', 'vingadores_2018_04_29_tf-pos')
# runProcess(c4, 'vingadores_2018_04_29_ing_sent/vingadores_2018_04_29_ing_sent_mpos', 'vingadores_2018_04_29_tf-mpos')

# runProcess(c4, 'vingadores_2018_04_30_ing_sent/vingadores_2018_04_30_ing_sent_mneg', 'vingadores_2018_04_30_tf-mneg')
# runProcess(c4, 'vingadores_2018_04_30_ing_sent/vingadores_2018_04_30_ing_sent_neg', 'vingadores_2018_04_30_tf-neg')
# runProcess(c4, 'vingadores_2018_04_30_ing_sent/vingadores_2018_04_30_ing_sent_neu', 'vingadores_2018_04_30_tf-neu')
# runProcess(c4, 'vingadores_2018_04_30_ing_sent/vingadores_2018_04_30_ing_sent_pos', 'vingadores_2018_04_30_tf-pos')
# runProcess(c4, 'vingadores_2018_04_30_ing_sent/vingadores_2018_04_30_ing_sent_mpos', 'vingadores_2018_04_30_tf-mpos')

# runProcess(c4, 'vingadores_2018_05_01_ing_sent/vingadores_2018_05_01_ing_sent_mneg', 'vingadores_2018_05_01_tf-mneg')
# runProcess(c4, 'vingadores_2018_05_01_ing_sent/vingadores_2018_05_01_ing_sent_neg', 'vingadores_2018_05_01_tf-neg')
# runProcess(c4, 'vingadores_2018_05_01_ing_sent/vingadores_2018_05_01_ing_sent_neu', 'vingadores_2018_05_01_tf-neu')
# runProcess(c4, 'vingadores_2018_05_01_ing_sent/vingadores_2018_05_01_ing_sent_pos', 'vingadores_2018_05_01_tf-pos')
# runProcess(c4, 'vingadores_2018_05_01_ing_sent/vingadores_2018_05_01_ing_sent_mpos', 'vingadores_2018_05_01_tf-mpos')

# runProcess(c4, 'vingadores_2018_05_02_ing_sent/vingadores_2018_05_02_ing_sent_mneg', 'vingadores_2018_05_02_tf-mneg')
# runProcess(c4, 'vingadores_2018_05_02_ing_sent/vingadores_2018_05_02_ing_sent_neg', 'vingadores_2018_05_02_tf-neg')
# runProcess(c4, 'vingadores_2018_05_02_ing_sent/vingadores_2018_05_02_ing_sent_neu', 'vingadores_2018_05_02_tf-neu')
# runProcess(c4, 'vingadores_2018_05_02_ing_sent/vingadores_2018_05_02_ing_sent_pos', 'vingadores_2018_05_02_tf-pos')
# runProcess(c4, 'vingadores_2018_05_02_ing_sent/vingadores_2018_05_02_ing_sent_mpos', 'vingadores_2018_05_02_tf-mpos')

# runProcess(c4, 'vingadores_2018_05_03_ing_sent/vingadores_2018_05_03_ing_sent_mneg', 'vingadores_2018_05_03_tf-mneg')
# runProcess(c4, 'vingadores_2018_05_03_ing_sent/vingadores_2018_05_03_ing_sent_neg', 'vingadores_2018_05_03_tf-neg')
# runProcess(c4, 'vingadores_2018_05_03_ing_sent/vingadores_2018_05_03_ing_sent_neu', 'vingadores_2018_05_03_tf-neu')
# runProcess(c4, 'vingadores_2018_05_03_ing_sent/vingadores_2018_05_03_ing_sent_pos', 'vingadores_2018_05_03_tf-pos')
# runProcess(c4, 'vingadores_2018_05_03_ing_sent/vingadores_2018_05_03_ing_sent_mpos', 'vingadores_2018_05_03_tf-mpos')

# runProcess(c4, 'vingadores_2018_05_04_ing_sent/vingadores_2018_05_04_ing_sent_mneg', 'vingadores_2018_05_04_tf-mneg')
# runProcess(c4, 'vingadores_2018_05_04_ing_sent/vingadores_2018_05_04_ing_sent_neg', 'vingadores_2018_05_04_tf-neg')
# runProcess(c4, 'vingadores_2018_05_04_ing_sent/vingadores_2018_05_04_ing_sent_neu', 'vingadores_2018_05_04_tf-neu')
# runProcess(c4, 'vingadores_2018_05_04_ing_sent/vingadores_2018_05_04_ing_sent_pos', 'vingadores_2018_05_04_tf-pos')
# runProcess(c4, 'vingadores_2018_05_04_ing_sent/vingadores_2018_05_04_ing_sent_mpos', 'vingadores_2018_05_04_tf-mpos')