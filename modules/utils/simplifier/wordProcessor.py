def isVerb(word, nlp):
	verb = False
	token = processToken(word,nlp)

	if token.pos_ == 'VERB' or token.pos_ == 'AUX':
		verb = True
	return verb
	
def getLemma(word, nlp):
	doc = nlp(word)
	for token in doc:
		lemma = token.lemma_ 
		lemmaList = lemma.split(" ")
	return lemmaList[0]


def processToken(word, nlp):
	doc = nlp(word)
	for token in doc:
		return token
		
def tokenToMap(token, nlp):
	tokenMap = { "text" : token.text,
				"dep" : token.dep_,
				"type" : token.pos_,
				"morf" : token.morph if token.pos_ == "VERB" or token.pos_ == "AUX" or token.pos_ == "PRON" else 'None',
				"position" :  token.i,
				"lemma" : token.lemma_
		}
	return tokenMap


def getMorphology(token, nlp, new):
	if new:
		token_aux = processToken(token.text, nlp)
	else:
		token_aux = token
	mapMorph = dict()
	listMorph = str(token_aux.morph).split('|')
	for item in listMorph:
		if item != 'None':
			auxList = item.split('=')
			mapMorph[auxList[0]] = auxList[1]
		else: return 'None'

	return mapMorph