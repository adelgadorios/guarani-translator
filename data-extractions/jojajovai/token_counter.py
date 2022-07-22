from nltk.tokenize import word_tokenize
from nltk.tokenize import TweetTokenizer
ce =  open("combined.es",'r')
cg =  open("combined.gn",'r')
data = ce.read()
data2 = cg.read()
x = word_tokenize(data)
x2 = word_tokenize(data2)
#x = data.split(' ')
print(len(x))
print(len(x2))
print("total is: ", len(x)+len(x2))
