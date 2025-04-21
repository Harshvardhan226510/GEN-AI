import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

text= 'I am going to revolutionize the technology'
tokens = word_tokenize(text)

unigrams = list(ngrams(tokens, 1))
bigrams= list(ngrams(tokens, 2))
trigrams = list(ngrams(tokens, 3))

print(unigrams)
print(bigrams)
print(trigrams)
