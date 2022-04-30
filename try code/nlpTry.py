import spacy
from spacy.matcher import Matcher
import re

def getMorphology(token):
	mapMorph = {}
	listMorph = str(token.morph).split('|')
	for item in listMorph:
		auxList = item.split('=')
		mapMorph[auxList[0]] = auxList[1]
	return mapMorph


def analyze(text):
	text = "(" + str(text) + ")"
	nlp = spacy.load('es_core_news_sm')
    
	pattern=[{'POS': 'VERB', 'OP': '+'}, {'POS': 'ADV', 'OP': '*'}, {'POS': 'DET', 'OP': '*'}, {'POS': 'ADP', 'OP': '*'}, {'POS': 'VERB', 'OP': '+'}]
	print(text)
	matcher = Matcher(nlp.vocab) 
	matcher.add("verb-phrases", [pattern])
	doc = nlp(text)
	matches = matcher(doc) 

	#for token in doc:
	#	print(f'{token.text:{8}} {token.pos_:{6}} {token.tag_:{6}} {token.dep_:{6}} {spacy.explain(token.pos_):{20}} {spacy.explain(token.tag_)}')
			#print(token.morph, token.i)

	    #if label['POS'] == 'VERB':
	    	#print(label, " -- ", spacy.explain(label))

	##Los de estan repetidos, tener cuidado con el indice !!

	spans = [doc[start:end] for _, start, end in matches] 
	print(spans)

	Map = {}
	for span in spans:
		Map[str(span)] = {}

	keys = list(Map.keys())


	for token in doc: 
		for key in keys:
			keyList = key.split()
			for item in keyList:
				if item == token.text:  
					index = keyList.index(item)
					if token.pos_ == 'ADP':
						if keyList[index - 1] == doc[index - 1].text:
							tokenMap = {
								'index': token.i,
								'type': token.pos_,
								'subtype': token.dep_,
								'tense':  getMorphology(token) if token.pos_ == "VERB" else 'None',
                                'lemma': token.lemma_
							}
							Map[key][token.text] = tokenMap
					else:
						tokenMap = {
							'index': token.i,
							'type': token.pos_,
							'subtype': token.dep_,
							'tense':  getMorphology(token) if token.pos_ == "VERB" else 'None',
                            'lemma': token.lemma_
							}
						Map[key][token.text] = tokenMap


	print(Map)

	textList = text.split()
	for word in textList:
		print(word)
		for key in Map.keys():
			if word in Map[key]: 
				if Map[key][word]['subtype'] == 'mark' or Map[key][word]['subtype'] == 'mark'  == '':
					textList[Map[key][word]['index']] = -1
				if Map[key][word]['subtype'] == 'ROOT' or Map[key][word]['subtype'] == 'acl':
					textList[Map[key][word]['index']] = -1

	newList = []
	for item in textList:
		if item != -1:
			newList.append(item)

	strList = ''
	for item in newList:
		strList += item + ' '


	return spans

