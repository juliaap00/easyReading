import stanza
#stanza.download('es') # download English model
nlp = stanza.Pipeline('es') # initialize English neural pipeline
doc = nlp("Se acostumbró a tener") # run annotation over a sentence


#ponerme, ponerte es 



print(doc)
for sentence in doc.sentences:
	for word in sentence.words:
		print(word.text, word.lemma, word.pos, word.feats, word.deprel)

print(replacedText)