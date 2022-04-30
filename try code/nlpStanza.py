import stanza
from spacy.matcher import Matcher
from modules.utils.verbsDictionary import isExsistantVerb
import re
import modules.utils.data as data
import modules.utils.mlconjugTry as mlconjug
from pprint	 import pprint


def getMorphology(token):
	mapMorph = dict()
	listMorph = str(token.feats).split('|')
	
	for item in listMorph:
		if item != 'None':
			auxList = item.split('=')
			mapMorph[auxList[0]] = auxList[1]
		else: return 'None'
	
	return mapMorph

def getPattern(periphrasisMap):
	lemma = periphrasisMap['aux']['lemma']
	complements = periphrasisMap['complements']
	
	for complement in complements:
		if complement['type'] == 'PRON' and complement['position'] == periphrasisMap['aux']['position']+1:
			lemma = f"{lemma}se"
		else:
			lemma =  f"{lemma} {complement['text']}" 

	return lemma

def getPeriphrasisType(periphrasisMap):
	typePeriph = periphrasisMap['ROOT']['morf']['VerbForm']
	lemma = getPattern(periphrasisMap)
	if lemma in data.periphrasisType[typePeriph].keys():
		return data.periphrasisType[typePeriph][lemma]
	return 'Semiperifrasis'


def getKeyVerb(token, periphrasisMap):
	if 'ROOT' in periphrasisMap.keys() and token['dep'] != 'root':
		aux = periphrasisMap['ROOT']
		periphrasisMap.pop('ROOT')
		periphrasisMap['aux'] = aux
		return 'ROOT'

	if 'ROOT' in periphrasisMap.keys() and token['dep'] == 'root': # POR QUE EL SEGUNDO ?
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
	if 'pron' in periphrasisMap.keys() and periphrasisMap['pron']['position'] == periphrasisMap['ROOT']['position'] + 1:
		return f"{periphrasisMap['pron']['text']} {verb}"
	else:
		print("a") 
		return verb

def fixReflexiveVerbs(token, periphrasisMap, tokenInfo, spell):
	lemma = token.lemma
	if not isExsistantVerb(lemma, spell):
		key = lemma[-3:]
		if key in data.reflexiveSuffix.keys() and lemma[-4] == 'r':
			pron = {
			'text' : data.reflexiveSuffix[key] ,
			'type' : 'PRON',
			'position' : token.id + 1
			}
			periphrasisMap['pron'] = pron

			tokenInfo['morf'] = {'VerbForm': 'Inf'}
			tokenInfo['lemma'] = lemma[0:-3]


def getSubjuntiveType(periphrasisMap):
	if periphrasisMap['lemma'][-3] == 'era':
		periphrasisMap['morf']['subType'] = '1'

def simplifyPeriphrasis(text,nlp, spell):
	doc = nlp(text)
	periphrasisMap = dict()

	complementList = list()

	for sentence in doc.sentences:
		for token in sentence.words:
			tokenInfo = { "text" : token.text,
					"dep" : token.deprel,
					"type" : token.pos,
					"morf" : getMorphology(token) if token.pos == "VERB" or "AUX" else 'None',
					#"tag" : token.tag,
					"position" :  token.id,
					"lemma" : token.lemma 
			}
			print(tokenInfo)

			if  token.pos == 'VERB' or token.pos == 'AUX' : #verbo copulativo
				key = getKeyVerb(tokenInfo, periphrasisMap)
				fixReflexiveVerbs(token, periphrasisMap, tokenInfo, spell)

			elif token.pos == 'ADJ':
				periphrasisMap['typePeriphrasis'] = 'Part'

			elif token.pos == 'PRON':
				key = 'pron'
			else: 
				key = 'complement'
				
			if key == 'complement':
				complementList.append(tokenInfo)
			else:
				periphrasisMap[key] = tokenInfo;

			periphrasisMap['complements'] = complementList;
		pprint(periphrasisMap)

		periphrasisMap['typePeriphrasis'] = getPeriphrasisType(periphrasisMap)

		if periphrasisMap['typePeriphrasis'] != 'Part' and  periphrasisMap['typePeriphrasis'] != 'Modal':
			print(periphrasisMap['aux']['morf'])
			
			#if periphrasisMap['aux']['morf']['Mood'] == 'Sub':
				#getSubjuntiveType(periphrasisMap['aux'])
			print(periphrasisMap['ROOT']['lemma'])
			verb = mlconjug.conjug(periphrasisMap['aux']['morf'], periphrasisMap['ROOT']['lemma'])
			print(verb)
			return isReflexive(periphrasisMap,verb)
		return text





