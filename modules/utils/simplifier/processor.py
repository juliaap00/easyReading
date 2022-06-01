import spacy
from modules.utils.simplifier.dictionary import isExsistantWord
import re

import modules.utils.simplifier.grammaticalData as data
import modules.utils.simplifier.conjugator as mlconjug
from modules.utils.simplifier.pronounFixer import checkReflexivePronouns, fixReflexiveVerbs
from modules.utils.simplifier.wordProcessor import processToken, getMorphology, getLemma, tokenToMap
from modules.utils.simplifier.classifier import *
from modules.utils.simplifier.conjugator import *


def getKeyVerb(token, periphrasisMap):
	if 'ROOT' in periphrasisMap.keys() and token['dep'] != 'root':
		aux = periphrasisMap['ROOT']
		periphrasisMap.pop('ROOT')
		if 'aux' in periphrasisMap:
			if not isinstance(periphrasisMap['aux'],list):
				listAuxs = list()
				listAuxs.append(periphrasisMap['aux'])
				listAuxs.append(aux)
				periphrasisMap['aux'] = listAuxs
			else:
				periphrasisMap['aux'] = periphrasisMap['aux'].append(aux)
		else:
			periphrasisMap['aux'] = aux
		return 'ROOT'
	if 'ROOT' in periphrasisMap.keys() and token['dep'] == 'root':

		aux = periphrasisMap['ROOT']
		periphrasisMap.pop('ROOT')
		periphrasisMap['aux'] = aux
		return 'ROOT'

	if  token['dep'] == 'conj' or token['dep'] == 'xcomp':
		return 'ROOT'

	if token['morf']['VerbForm'] != 'Inf' and token['morf']['VerbForm']  != 'Ger' and token['morf']['VerbForm'] != 'Part':
		return 'aux'
	else:
		return 'ROOT'

def simplifyPeriphrasis(text, nlp, spell, default_conjugator):
	doc = nlp(text)
	periphrasisMap = dict()
	periphrasisMap['periphrasisText'] = text
	complementList = list()
	tic1 = time.perf_counter()

	for token in doc:
		tokenInfo = tokenToMap(token, nlp)

		key = 'aux'
		#tic = time.perf_counter()
		if  tokenInfo['type'] == 'VERB' or tokenInfo['type'] == 'AUX' :
			
			lemma = getLemma(tokenInfo['text'], nlp)
			if lemma != tokenInfo['lemma'] and lemma[-1] == 'r': 
				tokenInfo['lemma'] = lemma

			if tokenInfo['morf'] is None or 'VerbForm' not in tokenInfo['morf']:
				tokenInfo['morf'] = getMorphology(token, nlp, False)

			key = getKeyVerb(tokenInfo, periphrasisMap)
			fixReflexiveVerbs(token, periphrasisMap, tokenInfo, spell)
		elif tokenInfo['type'] == 'PROPN':
				tokenInfo['morf'] = getMorphology(token, nlp, False)

		elif tokenInfo['type'] == 'ADJ':
			doc = nlp(f"haber {tokenInfo['text']}")
			for tokenPart in doc:
				if tokenPart.text == tokenInfo['text']:
					tokenInfo['morf'] = getMorphology(tokenPart, nlp, False)
					tokenInfo['lemma'] = tokenPart.lemma_

			key = getKeyVerb(tokenInfo, periphrasisMap)

		elif tokenInfo['type'] == 'NOUN' or tokenInfo['type'] == 'INTJ':

			doc = nlp(f"yo {tokenInfo['text']}")
			for tokenPart in doc:
				if tokenPart.text == tokenInfo['text']:
					tokenInfo['morf'] = getMorphology(tokenPart, nlp, False)

			periphrasisMap['typePeriphrasis'] = 'Part'
			key = getKeyVerb(tokenInfo, periphrasisMap)
		



		else: 
			key = 'complement'
			
		if key == 'complement':
			complementList.append(tokenInfo)
		else:
			periphrasisMap[key] = tokenInfo;


		periphrasisMap['complements'] = complementList;

	
	tic = time.perf_counter()
	checkReflexivePronouns(periphrasisMap, text, spell, nlp)
	periphrasisMap['typePeriphrasis'] = getPeriphrasisType(periphrasisMap)


	returnVerbDict = changeConjugation(periphrasisMap, text, spell, default_conjugator)

	return returnVerbDict
