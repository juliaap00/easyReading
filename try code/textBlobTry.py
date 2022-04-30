from textblob import TextBlob, Word


text = '''
El perro
'''

blob = TextBlob(text)
print(blob.tags)

w = Word("comido")
w.lemmatize("v")