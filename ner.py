
import nltk 
from nltk import word_tokenize, pos_tag, ne_chunk

sentence = "Rogue from X-Men did steal captain Marvel's powers right?"
print(ne_chunk(pos_tag(word_tokenize(sentence))))