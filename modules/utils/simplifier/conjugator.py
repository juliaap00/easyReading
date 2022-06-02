import mlconjug3
from modules.utils.simplifier.grammaticalData import morphologicalMap, subjTerminations2
from modules.utils.contextAdder.context import addContext
from modules.utils.simplifier.pronounFixer import isReflexive


def conjugMultipleAux(periphrasisMap, text, spell, tense, default_conjugator):
	if periphrasisMap['aux'][0]['lemma'] == 'haber':
		periphrasisMap['ROOT']['morf']['VerbForm'] = 'Part'
		verbPart = conjug(periphrasisMap['ROOT'], periphrasisMap['ROOT']['lemma'], default_conjugator)
		verb = f"{periphrasisMap['aux'][0]['text']} {verbPart}"		 
		return verb

	if tense == 'Fut':
		periphrasisMap['aux'][1]['morf'] = periphrasisMap['aux'][0]['morf']
		periphrasisMap['aux'][1]['morf']['Tense'] = 'Fut'
				
		verb = conjug(periphrasisMap['aux'][1], periphrasisMap['aux'][1]['lemma'], default_conjugator)

		return f"{verb} {periphrasisMap['ROOT']['text']}"
	if tense == 'Part':
		periphrasisMap['aux'][1]['morf'] = periphrasisMap['aux'][0]['morf']
		periphrasisMap['aux'][1]['morf']['VerbForm'] = 'Part'
		verb = conjug(periphrasisMap['aux'][1], periphrasisMap['ROOT']['lemma'], default_conjugator)
	else:

		periphrasisMap['aux'][1]['morf'] = periphrasisMap['aux'][0]['morf']
				
		verb = conjug(periphrasisMap['aux'][1],  periphrasisMap['ROOT']['lemma'], default_conjugator)

	return f"{verb}"

def isPartCopulative(aux):
	result = False
	if isinstance(aux, list):
		aux = aux[0]
	if aux['lemma'] == 'ser' or aux['lemma'] == 'estar':
		result = True
	return result


def changeConjugation(periphrasisMap, text, spell, default_conjugator):
	returnVerbDict = {'verb' : '',
		'explanation' : ''}
	if (periphrasisMap['typePeriphrasis'] == 'Part' and isPartCopulative(periphrasisMap['aux'])) or (periphrasisMap['typePeriphrasis'] == 'Modal' and not 'tener' in periphrasisMap['aux']) :
		
		returnVerbDict['explanation'] = f"La perífraisis '{periphrasisMap['periphrasisText']}' no se simplifica puesto que es de tipo Participio y su verbo auxiliar es 'ser' o 'estar'." if periphrasisMap['typePeriphrasis'] == 'Part' else f"La perífraisis '{periphrasisMap['periphrasisText']}' no se simplifica puesto que es de tipo Modal."
		return returnVerbDict

	if periphrasisMap['typePeriphrasis'] == 'Part' and isinstance(periphrasisMap['aux'], list):
		if periphrasisMap['aux'][0]['lemma'] == 'tener' and periphrasisMap['aux'][0]['morf']['Tense'] == 'Pres':

			for complement in periphrasisMap['complements']:
				if 'que' in complement['text'] and 'Inf' in periphrasisMap['aux'][1]['morf']['VerbForm'] and 'Part' in periphrasisMap['ROOT']['morf']['VerbForm']:

						periphrasisMap['aux'][1]['morf'] = periphrasisMap['aux'][0]['morf']
						periphrasisMap['aux'][1]['morf']['Tense'] = 'Fut'
			
						verb = conjug(periphrasisMap['aux'][1], periphrasisMap['aux'][1]['lemma'], default_conjugator)
						returnVerbDict['verb'] = f"{verb} {periphrasisMap['ROOT']['text']}"
						returnVerbDict['explanation'] = f"La perífrasis '{periphrasisMap['periphrasisText']}' es de tipo Modal pero al estar formada por  'tener' (en presente) 'que' + '{periphrasisMap['aux'][1]['lemma']}' (infinitivo) + '{periphrasisMap['aux'][0]['lemma']}' (participio) se ha simplificado eliminando el verbo 'tener' y conjugando el verbo '{periphrasisMap['aux'][1]['lemma']}' a futuro."
						
	elif (periphrasisMap['typePeriphrasis'] != 'Part' and  periphrasisMap['typePeriphrasis'] != 'Modal') or (periphrasisMap['typePeriphrasis'] == 'Part' and periphrasisMap['ROOT']['lemma'] != 'ser' and periphrasisMap['ROOT']['lemma'] != 'estar') :

		verb = conjug(periphrasisMap['aux'], periphrasisMap['ROOT']['lemma'], default_conjugator) if not isinstance(periphrasisMap['aux'], list) else conjugMultipleAux(periphrasisMap, text, spell, 'aux', default_conjugator)
		returnVerbDict['verb'] = verb
		returnVerbDict['explanation'] = f"Se ha simplificado la perífrasis '{periphrasisMap['periphrasisText']}' conjugando el verbo raíz '{periphrasisMap['ROOT']['lemma']}' con el tiempo verbal del auxiliar '{periphrasisMap['pattern']}'."
		returnVerb = addContext(periphrasisMap, returnVerbDict['verb'])

		if isinstance(returnVerb, dict) and 'context' in returnVerb.keys() and 'explanation' in returnVerb.keys():
			returnVerbDict['explanation'] = f"{returnVerbDict['explanation'][:-1]} {returnVerb['explanation']}"
			returnVerbDict['context'] = returnVerb['context']

	returnVerbDict['verb'] = isReflexive(periphrasisMap,returnVerbDict['verb'])
	return returnVerbDict
	

def getSubjuntiveTermination(verb):
	for temination in subjTerminations2:
		if temination in verb:
			return '2'
	return '1'


def generateConjug(periphrasisMap):
	conjugationMap	= dict()
	morphologicMap = periphrasisMap['morf']

	conjugationMap['Mood'] = morphologicalMap[morphologicMap['Mood']]
	
	if morphologicMap['Mood'] == 'Cnd':
		morphologicMap['Tense'] = 'Cnd'

	conjugationMap['Tense'] = f"{conjugationMap['Mood']} {morphologicalMap[morphologicMap['Tense']]}"
	conjugationMap['Person'] = f"{morphologicMap['Person']}{morphologicalMap[morphologicMap['Number']]}"

	if morphologicMap['Mood'] == 'Sub' and morphologicMap['Tense'] == 'Imp':
		conjugationMap['Tense'] = f"{conjugationMap['Tense']} {getSubjuntiveTermination(periphrasisMap['text'])}"

	return	conjugationMap
	
	
def conjug(periphrasisMap, verb, default_conjugator):
	morphologicMap = periphrasisMap['morf']
	if morphologicMap['VerbForm'] != 'Inf' and morphologicMap['VerbForm'] != 'Ger' and morphologicMap['VerbForm'] != 'Part':
		conjugationMap = generateConjug(periphrasisMap)
		conjugatedVerb = default_conjugator.conjugate(verb).conjug_info[conjugationMap['Mood']][conjugationMap['Tense']][conjugationMap['Person']]
		return conjugatedVerb
	
	else:
		conjugationMap = morphologicalMap[morphologicMap['VerbForm']]
		if morphologicMap['VerbForm'] == 'Part':
			conjugatedVerb = default_conjugator.conjugate(verb).conjug_info[conjugationMap[0]][conjugationMap[1]]
		else:
			conjugatedVerb = default_conjugator.conjugate(verb).conjug_info[conjugationMap[0]][conjugationMap[1]]['']
		return conjugatedVerb
	return verb



