import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize

text= 'I love Artificial intelligence so much'
tokens= word_tokenize(text)
print('Tokens:', tokens)
