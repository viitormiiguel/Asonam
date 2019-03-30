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

                t2 = str(t[1][5:])
                t2 = t2[t2.find(','):]
                t2 = t2[1:]

                if txt.find('JJ') == 1: 
                        if int(t2) > 100:
                                arrayWords.append(t1)
                        
        # print(d)
        # print(arrayWords)

        return arrayWords

# run(captain, 'tf-mpos')
# run(captain, 'tf-pos')
# run(captain, 'tf-neu')
# run(captain, 'tf-neg')
run(captain, 'tf-mneg')
