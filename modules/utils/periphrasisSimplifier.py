import spacy
from modules.utils.simplifier.processor  import simplifyPeriphrasis
from modules.utils.simplifier.wordProcessor import isVerb, getLemma
import modules.utils.simplifier.grammaticalData as data
from spellchecker import SpellChecker
import mlconjug3

import numpy


def create_json(sourceText, periphrasisList):
    json = { 'id': 9,
            'name': 'Pauta - Evitar Perifrasis',
            'description': '''Se debería evitar el uso de dos o más verbos seguidos, exceptuando las perífrasis con los verbos modales deber, querer, saber y poder.''',
            'pass': False,

            'reason':'''El texto presenta las siguientes perifrasis, que deberian evitarse:'''f"[{periphrasisList}].",
            'originalText': sourceText
    }
    return json

def replacePeriphrasis(replacedText, phrasal, simplify, context):
	if phrasal in replacedText:
		if context != '' :
			replacedText =  replacedText.replace(phrasal, f"{simplify} {context}" )
			return replacedText

		else:
			replacedText = replacedText.replace(phrasal, simplify)

		return replacedText

	wordlList = phrasal.split(" ")


	for word in wordlList[1:-1]:

		replacedText = replacedText.replace(f" {word} "," ")

		replacedText = replacedText.replace(f" {word}.",".")



	if context != '':
		replacedText = replacedText.replace(wordlList[0] , f"{simplify}")
		replacedText = replacedText.replace(wordlList[-1], f"{context}")

	else:
		replacedText = replacedText.replace(wordlList[0], simplify)
		replacedText = replacedText.replace(f" {wordlList[-1]}","")

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


def periphrasisSimplifier(sourceText, periphrasisList):
	json = create_json(sourceText,periphrasisList)
	try:
		if sourceText == '': 
			json['pass'] = True
			json['explanation'] = 'Ha ocurrido un error, por favor introduzca un texto a simplificar.'
			return json

		if periphrasisList == '': 
			json['simplifiedText'] = sourceText
			json['pass'] = True
			json['explanation'] = 'No se ha simplificado nada puesto que no hay perífrasis indicada para el texto introducido.'
			return json

		nlp = spacy.load('es_core_news_lg')

		replacedText = sourceText
		replacedText = f'{replacedText[0].lower()}{replacedText[1:]}'
		
		periphrasisList = f'{periphrasisList[0].lower()}{periphrasisList[1:]}'
		phrasalList = periphrasisList.split(',')
		phrasalList = numpy.char.strip(numpy.array(phrasalList)).tolist()

		spell = SpellChecker(language='es')
		default_conjugator = mlconjug3.Conjugator(language='es')

		simplify = ''
		multipleList = isMultiplePeriphrasis(replacedText,phrasalList, nlp)

		for phrasal in phrasalList:
			phrasal = mergeMultiplePreiphrasis(multipleList, replacedText, phrasal, nlp)
			

			simplify = simplifyPeriphrasis(phrasal,nlp, spell, default_conjugator)
			if simplify['verb'] != '':

				if (not 'context' in simplify.keys()):
					replacedText = replacePeriphrasis(replacedText, phrasal, simplify['verb'], '')
			
				else: 
					replacedText = replacePeriphrasis(replacedText, phrasal, simplify['verb'], simplify['context'] )
			
			json['explanation'] = simplify['explanation'] if not 'explanation' in json.keys() else f"{json['explanation']} {simplify['explanation']}"

		firstLetter = replacedText[0].upper()
		replacedText = f"{firstLetter}{replacedText[1:]}"
		
		json['simplifiedText'] = replacedText
		return json

	except Exception as e:
		json['simplifiedText'] = 'Ha ocurrido un error, por favor revise que toda la información es correcta e inténtelo de nuevo.'
		json['explanation'] = f'Ha ocurrido un error, por favor revise que toda la información es correcta e inténtelo de nuevo.'
		return json
