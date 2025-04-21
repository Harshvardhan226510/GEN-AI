from textblob import TextBlob

text='I lov artificial intellgence so mch'

blob = TextBlob(text)

corrected_text = blob.correct()

print("Original text:", text)
print("Corrected text:", corrected_text)
