'''import spacy
from modules.utils.nlpPart1  import simplifyPeriphrasis, isVerb, getLemma
import modules.utils.data as data
from spellchecker import SpellChecker

def replacePeriphrasis(replacedText, phrasal, simplify, context):
	if phrasal in replacedText:	
		replacedText = replacedText.replace(phrasal, simplify)
		return replacedText

	wordlList = phrasal.split(" ")


	replacedText = replacedText.replace(wordlList[0], simplify)
	for word in wordlList[1:]:

		replacedText = replacedText.replace(f" {word} "," ")
		replacedText = replacedText.replace(f" {word}.",".")


		if context != '':
			replacedText = replacedText.replace(f".",f" {context}.")

	return replacedText


def isMultiplePeriphrasis(originaltest, periphrasisList, nlp):
	indicesList = list()
	wordlList = list()
	duplicatedMap = dict()
	for periphrasis in periphrasisList:
		wordlList = periphrasis.split(" ")
		for word in wordlList:
			if word != '':
				index = originaltest.find(word,0)
				if index not in indicesList or not isVerb(word, nlp) :
					indicesList.append(index)
				else: 
					duplicatedMap[periphrasis] = index
	return duplicatedMap

def mergeMultiplePreiphrasis(multipleList, replacedText, phrasal, nlp):
	simplify = ''
	if phrasal in multipleList.keys():
		aux = phrasal.split(" ")
		auxString = " ".join(aux[1:])

		rest = replacedText.find(auxString,0)
		restList = list()
		restList = replacedText[0:rest].split(" ")
		
		for word in restList:
			if word in data.reflexivePronouns:
				simplify = f'{word} '

			if getLemma(word, nlp) == getLemma(aux[0], nlp):
				simplify = f'{simplify}{word} {auxString}'
				break

	return phrasal if simplify == '' else simplify


def easyReading(json):
	#try:
	nlp = spacy.load('es_core_news_lg')

	indice = json['reason'].find('[',1)
	replacedText = json['originalText']
	replacedText = f'{replacedText[0].lower()}{replacedText[1:]}'
	
	lastIndex = json['reason'].find(']',1)
	lastPosition = lastIndex - len(json['reason'])
	
	phrasalString = json['reason'][indice+1:lastPosition] 

	phrasalString = f'{phrasalString[0].lower()}{phrasalString[1:]}'

	phrasalList = phrasalString.split(', ')
	if not phrasalList: 
		json['simplifiedText'] = json['originalText']
		return json

	spell = SpellChecker(language='es')
	simplify = ''
	multipleList = isMultiplePeriphrasis(replacedText,phrasalList, nlp)
	
	for phrasal in phrasalList:
		phrasal = mergeMultiplePreiphrasis(multipleList, replacedText, phrasal, nlp)
		simplify = simplifyPeriphrasis(phrasal,nlp, spell)
		if simplify['verb'] != '':

			if (not 'context' in simplify.keys()):
				replacedText = replacePeriphrasis(replacedText, phrasal, simplify['verb'], '')
		
			else: 
				replacedText = replacePeriphrasis(replacedText, phrasal, simplify['verb'], simplify['context'] )
		
	firstLetter = replacedText[0].upper()
	replacedText = f"{firstLetter}{replacedText[1:]}"
	
	json['simplifiedText'] = replacedText
	return json
'''