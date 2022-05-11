import nltk
from nltk.corpus import comtrans

nltk.download('comtrans')
print(comtrans.aligned_sents('alignment-de-en.txt')[0])
