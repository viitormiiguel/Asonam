import nltk 

aquaman = "Data/aquaman-tweets/aquaman/"
captain = "Data/captain-tweets/"
avengers = "Data/avengers-tweets/no_war/"

def run(c, d):
        document_text = open(c + d + '.txt', 'r')
        arrayWords = []
        for dt in document_text.readlines():
                t = dt.split()
                txt = t[1][0:len(t[1])-4]
                t1 = t[0][2:len(t[0])-1]
                t1 = t1.replace("'","")
                if txt.find('JJ') == 1: 
                        arrayWords.append(t1)
                        
        print(d)
        print(arrayWords)

run(captain, 'tf-mpos')
run(captain, 'tf-pos')
run(captain, 'tf-neu')
run(captain, 'tf-neg')
run(captain, 'tf-mneg')
