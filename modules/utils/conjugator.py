import mlconjug3
from modules.utils.data import morphologicalMap, subjTerminations2



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
	
	
def conjug(periphrasisMap, verb):
	morphologicMap = periphrasisMap['morf']
	if morphologicMap['VerbForm'] != 'Inf' and morphologicMap['VerbForm'] != 'Ger' and morphologicMap['VerbForm'] != 'Part':
		conjugationMap = generateConjug(periphrasisMap)
		default_conjugator = mlconjug3.Conjugator(language='es')
		conjugatedVerb = default_conjugator.conjugate(verb).conjug_info[conjugationMap['Mood']][conjugationMap['Tense']][conjugationMap['Person']]
		return conjugatedVerb
	
	else:
		default_conjugator = mlconjug3.Conjugator(language='es')
		conjugationMap = morphologicalMap[morphologicMap['VerbForm']]
		if morphologicMap['VerbForm'] == 'Part':
			conjugatedVerb = default_conjugator.conjugate(verb).conjug_info[conjugationMap[0]][conjugationMap[1]]
		else:
			conjugatedVerb = default_conjugator.conjugate(verb).conjug_info[conjugationMap[0]][conjugationMap[1]]['']

		return conjugatedVerb
	return verb



