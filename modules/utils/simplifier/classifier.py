import modules.utils.simplifier.grammaticalData as data


def getPattern(periphrasisMap):
	if isinstance(periphrasisMap['aux'], list):
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

	periphrasisMap['pattern'] = lemma
	if periphrasisMap['ROOT']['morf']['VerbForm'] == 'Part' or ( 'typePeriphrasis' in periphrasisMap.keys() and periphrasisMap['typePeriphrasis'] == 'Part' in periphrasisMap):
		return 'Part'
	if lemma in data.periphrasisType[typePeriph].keys():
		return data.periphrasisType[typePeriph][lemma]
	return 'Semiperifrasis'