'''import spacy
from spacy.matcher import Matcher
from modules.utils.dictionary import isExsistantWord
import re
import modules.utils.data as data
from spellchecker import SpellChecker
import modules.utils.conjugator as mlconjug
from modules.utils.context.context import addContext

from pprint	 import pprint

def processToken(word, nlp):
	doc = nlp(word)
	for token in doc:
		return token


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


def addVerbToPron(tokenMap):
	pron = tokenMap['pron']
	if tokenMap['ROOT']['position'] == pron['position'] + 1:
		tokenMap['ROOT']['pron'] = pron
		tokenMap.pop(pron)
	else:
		tokenMap['aux']['pron'] = pron


def tokenToMap(token, nlp):
	tokenMap = { "text" : token.text,
				"dep" : token.dep_,
				"type" : token.pos_,
				"morf" : token.morph if token.pos_ == "VERB" or token.pos_ == "AUX" or token.pos_ == "PRON" else 'None',
				"position" :  token.i,
				"lemma" : token.lemma_
		}
	return tokenMap


def addPronoun(pronoun, text, subTokenMap, nlp, spell):

	textSpace = f"{text} "
	if 'pron' not in subTokenMap:
		textAux = textSpace.replace(f"{pronoun} ", '')
		if isExsistantWord(textAux, spell) and isVerb(textAux, nlp) and getLemma(text, nlp) == getLemma(textAux, nlp):

			tokenPron = processToken(pronoun, nlp)
			subTokenMap['pron'] = tokenToMap(tokenPron, nlp)
			subTokenMap['pron']['verb'] = text


def checkReflexivePronouns(tokenMap, periphrasis, spell, nlp):
	if 'pron' in tokenMap.keys():
		addVerbToPron(tokenMap)
	for pronoun in data.reflexivePronouns:
		if 'ROOT' in tokenMap.keys() and pronoun in tokenMap['ROOT']['text']:
			text = tokenMap['ROOT']['text']
			addPronoun(pronoun, text, tokenMap['ROOT'], nlp, spell)


		if pronoun in tokenMap['aux']:
			if isinstance(tokenMap['aux'], list):
				text = tokenMap['aux'][1]['text']
				subTokenMap = tokenMap['aux'][1]
			else: 
				text = tokenMap['aux']['text']
				subTokenMap = tokenMap['aux']
			addPronoun(pronoun, text, subTokenMap, nlp, spell)



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

def getPattern(periphrasisMap):
	if isinstance(periphrasisMap['aux'], list):
		##CHECKEAR
		auxMap = periphrasisMap['aux'][1]

	else:
		auxMap = periphrasisMap['aux']
		lemma = periphrasisMap['aux']['lemma']  

	lemma = auxMap['lemma']
	complements = periphrasisMap['complements']
	
	if 'pron' in auxMap.keys():
		lemma = f"{lemma}se"

	for complement in complements:
		lemma =  f"{lemma} {complement['text']}" 
	return lemma


def getPeriphrasisType(periphrasisMap):
	typePeriph = periphrasisMap['ROOT']['morf']['VerbForm']
	lemma = getPattern(periphrasisMap)

	# Aqui con el pattern puedo pillar el addContext
	periphrasisMap['pattern'] = lemma
	if periphrasisMap['ROOT']['morf']['VerbForm'] == 'Part' or ( 'typePeriphrasis' in periphrasisMap.keys() and periphrasisMap['typePeriphrasis'] == 'Part' in periphrasisMap):
		return 'Part'
	if lemma in data.periphrasisType[typePeriph].keys():
		return data.periphrasisType[typePeriph][lemma]
	return 'Semiperifrasis'


def getKeyVerb(token, periphrasisMap):
	if 'ROOT' in periphrasisMap.keys() and token['dep'] != 'ROOT':

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

	if 'ROOT' in periphrasisMap.keys() and token['dep'] == 'ROOT':
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


def isReflexive(periphrasisMap, verb):
	if 'pron' in periphrasisMap['ROOT'].keys():
		return f"{periphrasisMap['ROOT']['pron']['text']} {verb}"

	else:
		return verb


def fixReflexiveVerbs(token, periphrasisMap, tokenInfo, spell):
	lemma = token.lemma_
	if not isExsistantWord(lemma, spell):
		if ' ' in lemma:
			lemma = lemma.split(' ')[0]
			tokenInfo['lemma'] = f'{lemma}'

		key = lemma[-3:]
		if key in data.reflexiveSuffix.keys() and lemma[-4] == 'r':
			pron = {
			'text' : data.reflexiveSuffix[key] ,
			'type' : 'PRON',
			'position' : token.i + 1
			}
			periphrasisMap['pron'] = pron

			tokenInfo['morf'] = {'VerbForm': 'Inf'}
			tokenInfo['lemma'] = lemma[0:-3]


def getSubjuntiveType(periphrasisMap):
	if periphrasisMap['lemma'][-3] == 'era' or periphrasisMap['lemma'][-3] == 'ara':
		periphrasisMap['morf']['subType'] = '1'


##CAMBIAR LO LA EXPLICACION? O POR LO MENOS EN LA LLAMADA
def conjugMultipleAux(periphrasisMap, text, spell, tense):
	if periphrasisMap['aux'][0]['lemma'] == 'haber':
		periphrasisMap['ROOT']['morf']['VerbForm'] = 'Part'
		verbPart = mlconjug.conjug(periphrasisMap['ROOT'], periphrasisMap['ROOT']['lemma'])
		verb = f"{periphrasisMap['aux'][0]['text']} {verbPart}"		 
		return verb

	if tense == 'Fut':
		periphrasisMap['aux'][1]['morf'] = periphrasisMap['aux'][0]['morf']
		periphrasisMap['aux'][1]['morf']['Tense'] = 'Fut'
				
		verb = mlconjug.conjug(periphrasisMap['aux'][1], periphrasisMap['aux'][1]['lemma'])

		return f"{verb} {periphrasisMap['ROOT']['text']}"
	if tense == 'Part':
		periphrasisMap['aux'][1]['morf'] = periphrasisMap['aux'][0]['morf']
		periphrasisMap['aux'][1]['morf']['VerbForm'] = 'Part'
		verb = mlconjug.conjug(periphrasisMap['aux'][1], periphrasisMap['ROOT']['lemma'])
	else:

		periphrasisMap['aux'][1]['morf'] = periphrasisMap['aux'][0]['morf']
		#periphrasisMap['aux'][1]['morf']['Tense'] = periphrasisMap['aux'][0]['morf']['Tense']
				
		verb = mlconjug.conjug(periphrasisMap['aux'][1],  periphrasisMap['ROOT']['lemma'])

	return f"{verb}"

def isPartCopulative(aux):
	result = False
	if isinstance(aux, list):
		aux = aux[0]
	if aux['lemma'] == 'ser' or aux['lemma'] == 'estar':
		result = True
	return result


def changeConjugation(periphrasisMap, text, spell):
	returnVerbDict = {'verb' : ''}
	if (periphrasisMap['typePeriphrasis'] == 'Part' and isPartCopulative(periphrasisMap['aux'])) or (periphrasisMap['typePeriphrasis'] == 'Modal'):# and not 'tener' in periphrasisMap['aux']) :
		return returnVerbDict

	if periphrasisMap['typePeriphrasis'] == 'Part':

		if isinstance(periphrasisMap['aux'], list):

			if periphrasisMap['aux'][0]['lemma'] == 'tener' and periphrasisMap['aux'][0]['morf']['Tense'] == 'Pres':

				for complement in periphrasisMap['complements']:
					if 'que' in complement['text'] and 'Inf' in periphrasisMap['aux'][1]['morf']['VerbForm'] and 'Part' in periphrasisMap['ROOT']['morf']['VerbForm']:

							periphrasisMap['aux'][1]['morf'] = periphrasisMap['aux'][0]['morf']
							periphrasisMap['aux'][1]['morf']['Tense'] = 'Fut'
				
							verb = mlconjug.conjug(periphrasisMap['aux'][1], periphrasisMap['aux'][1]['lemma'])
							returnVerbDict['verb'] = f"{verb} {periphrasisMap['ROOT']['text']}"
							
	elif (periphrasisMap['typePeriphrasis'] != 'Part' and  periphrasisMap['typePeriphrasis'] != 'Modal') or (periphrasisMap['typePeriphrasis'] == 'Part' and periphrasisMap['ROOT']['lemma'] != 'ser' and periphrasisMap['ROOT']['lemma'] != 'estar') :

		verb = mlconjug.conjug(periphrasisMap['aux'], periphrasisMap['ROOT']['lemma']) if not isinstance(periphrasisMap['aux'], list) else conjugMultipleAux(periphrasisMap, text, spell, 'aux')
		returnVerbDict['verb'] = verb
	

	returnVerbDict['verb'] = isReflexive(periphrasisMap,returnVerbDict['verb'])	
	return returnVerbDict
	

def simplifyPeriphrasis(text, nlp, spell):
	doc = nlp(text)
	periphrasisMap = dict()

	complementList = list()
	for token in doc:
		tokenInfo = tokenToMap(token, nlp)
		key = 'aux'
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
	checkReflexivePronouns(periphrasisMap, text, spell, nlp)
	periphrasisMap['typePeriphrasis'] = getPeriphrasisType(periphrasisMap)
	returnVerbDict = changeConjugation(periphrasisMap, text, spell)
	return returnVerbDict
'''