import nltk 

aquaman = "Data/aquaman-tweets/aquaman/"
captain = "Data/captain-tweets/"
avengers = "Data/avengers-tweets/no_war/"

def run(c, d):
    document_text = open(c + d + '.txt', 'r')
    for dt in document_text.readlines():
        t = dt.split()
        txt = t[0][1:len(t[0])-1]
        txt = nltk.word_tokenize(txt)
        # print(txt)
        print(nltk.pos_tag(txt))
        # print(dt)

run(captain, 'tf-mpos')
run(captain, 'tf-pos')
run(captain, 'tf-neu')
run(captain, 'tf-neg')
run(captain, 'tf-mneg')