from modules.utils.simplifier.dictionary import isExsistantWord
from modules.utils.simplifier.grammaticalData import reflexivePronouns, reflexiveSuffix
from modules.utils.simplifier.wordProcessor import isVerb, getLemma, processToken, tokenToMap

from pprint	import pprint



def addPronoun(pronoun, text, subTokenMap, nlp, spell):

	textSpace = f"{text} "
	if 'pron' not in subTokenMap:
		textAux = textSpace.replace(f"{pronoun} ", '')
		if isExsistantWord(textAux, spell) and isVerb(textAux, nlp) and getLemma(text, nlp) == getLemma(textAux, nlp):

			tokenPron = processToken(pronoun, nlp)
			subTokenMap['pron'] = tokenToMap(tokenPron, nlp)
			subTokenMap['pron']['verb'] = text

def addVerbToPron(tokenMap):
	pron = tokenMap['pron']
	if tokenMap['ROOT']['position'] == pron['position'] + 1:
		tokenMap['ROOT']['pron'] = pron
		tokenMap.pop(pron)
	else:
		tokenMap['aux']['pron'] = pron

def checkReflexivePronouns(tokenMap, periphrasis, spell, nlp):
	if 'pron' in tokenMap.keys():
		addVerbToPron(tokenMap)
	for pronoun in reflexivePronouns:
		if pronoun in tokenMap['ROOT']['text']:
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


def isReflexive(periphrasisMap, verb):
	if 'pron' in periphrasisMap['ROOT'].keys(): 
		return f"{periphrasisMap['ROOT']['pron']['text']} {verb}"	
	return verb

def fixReflexiveVerbs(token, periphrasisMap, tokenInfo, spell):
	lemma = token.lemma_
	if not isExsistantWord(lemma, spell):
		if ' ' in lemma:
			lemma = lemma.split(' ')[0]
			tokenInfo['lemma'] = f'{lemma}'

		key = lemma[-3:]
		if key in reflexiveSuffix.keys() and lemma[-4] == 'r':
			pron = {
			'text' : reflexiveSuffix[key] ,
			'type' : 'PRON',
			'position' : token.i + 1
			}
			periphrasisMap['pron'] = pron

			tokenInfo['morf'] = {'VerbForm': 'Inf'}
			tokenInfo['lemma'] = lemma[0:-3]
