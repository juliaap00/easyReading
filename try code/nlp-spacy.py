import spacy
from spacy.matcher import Matcher
import re
import modules.utils.data as data
import modules.utils.mlconjugTry as mlconjug


def getMorphology(token):
	mapMorph = {}
	listMorph = str(token.morph).split('|')
	for item in listMorph:
		auxList = item.split('=')
		mapMorph[auxList[0]] = auxList[1]
	return mapMorph

#Ahora mismo no tiene sentido, en un futuro concatena los determinantes
def getPattern(tokenMap):
	print(tokenMap)
	lemma = tokenMap['aux']['lemma']
	complements = tokenMap['complements']
	for complement in complements:
		print(complement['text'])

		lemma = lemma + " " + complement['text']
	return lemma

''' def getLemma(verb):
	if verb['lemma'][-2:] == 'ar' or verb['lemma'][-2:] == 'er' or verb['lemma'][-2:] == 'ir':
		return verb['lemma'] 
	else: return 'A'
'''


def getType(tokenMap):
	typePeriph = tokenMap['ROOT']['morf']['VerbForm']
	lemma = getPattern(tokenMap)
	return data.periphrasisType[typePeriph][lemma]


def change(text):
	nlp = spacy.load('es_core_news_sm')
	# a, de, por --> mark
	# que --> cc

	# doc = nlp("Vengo observando su conducta desde") para vengo, llendo, sueño, sigo el lemma que adjudica es vengo

	doc = nlp(text)
	tokenMap = {}

	print([(w.text, w.pos_, w.morph, w.tag_, w.dep_, w.lemma_, w.i) for w in doc])


	complementList = []
	for token in doc:
		aux = { "text" : token.text,
				"dep" : token.dep_,
				"type" : token.pos_,
				"morf" : getMorphology(token) if token.pos_ == "VERB" else 'None',
				"tag" : token.tag_,
				"position" :  token.i,
				"lemma" : token.lemma_
		}
		key = 'aux'
		if  token.pos_ == 'VERB':
			key = 'ROOT' if aux['morf']['VerbForm'] == 'Inf' or aux['morf']['VerbForm'] == 'Gen' else 'aux'
		if token.pos_  == 'ADJ':
			key = 'ROOT'
			tokenMap['typePeriphrasis'] = 'Part'
			#aux['lemma'] = getLemma(aux['lemma'])
		if  token.dep_ == 'mark' or token.dep_ == 'cc':
			complementList.append(aux)
		else:
			tokenMap[key] = aux;

		tokenMap['complements'] = complementList;


	tokenMap['typePeriphrasis'] = getType(tokenMap)
	print(tokenMap)
	if tokenMap['typePeriphrasis'] != 'Part' and  tokenMap['typePeriphrasis'] != 'Modal':
			verb = mlconjug.conjug(tokenMap['aux']['morf'], tokenMap['ROOT']['text'])
			print(tokenMap['aux']['morf'])
			print(verb)
			return verb
	return text





