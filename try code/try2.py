import spacy
from spacy.matcher import Matcher
import re
'''
periphrasis['Inf'] =  { 'ir' : 'Temporal Inmmediata',
						'acabar': 'Temporal Anterioridad Reciente',
						'terminar': 'Temporal Anterioridad Reciente',
						'soler' : 'Temporal Frecuentiva',
						'acostumbrar' : 'Temporal Frecuentiva',
						'volver' : 'Temporal Frecuentiva',
						'saber' : 'Temporal', #?
}

'''

periphrasisType = {}

inf = { 'ir' : 'Posterioridad Inmmediata',
		'soler': 'Temporal Frecuentiva', # a menudo
		'saber': 'Temporal', #bien
		'deber' : 'Modal Radical de Obligacion',
		'poder' : 'Modal Radical Capacidad',
		'parecer': 'Modal',
		'querer': 'Modal'

}
gen =  { 'estar' : 'Principal Cursiva',
		'ir' : 'Principal Cursiva',
		'venir': 'Principal Cursiva',
		'andar': 'Principal',
		'llevar': 'Otras Cursiva',
		'pasar' : 'Otras Cursiva',
		'pasarse': 'Otras Cursiva',
		'vivir': 'Frecuentiva', #eliminar verbo y conjugar
		'seguir': 'Frecuentiva',
		'continuar': 'Frecuentiva',
		'empezar': 'Escalares',
		'acabar': 'Escalares',
		'terminar': 'Escalares',
		'continuar': 'Escalares'
	}

periphrasisType['Inf'] = inf 
periphrasisType['Gen'] = gen 




def getType(lemma, typePeriph):
	return periphrasisType[typePeriph][lemma]


nlp = spacy.load('es_core_news_sm')
subbordinate=[[{'POS': 'VERB', 'DEP': 'ROOT','OP': '+'},  {'POS': 'VERB', 'DEP': 'xcomp', 'MORPH': 'VerbForm=Inf','OP': '+'}, {'POS': 'VERB','OP': '+'}], 
[{'POS': 'VERB', 'DEP': 'ROOT','OP': '+'},  {'POS': 'VERB', 'DEP': 'ccomp', 'MORPH': 'VerbForm=Inf','OP': '+'},{'POS': 'VERB','OP': '+'}]
]

patternGen=[[{'POS': 'VERB', 'DEP': 'xcomp', 'MORPH': 'VerbForm=Inf','OP': '+'}, {'POS': 'VERB', 'DEP': 'xcomp','MORPH': 'VerbForm=Gen','OP': '+'}],
[{'POS': 'VERB', 'DEP': 'ccomp', 'MORPH': 'VerbForm=Inf','OP': '+'}, {'POS': 'VERB', 'DEP': 'xcomp','MORPH': 'VerbForm=Gen','OP': '+'}],
[{'POS': 'VERB', 'DEP': 'ROOT','OP': '+'}, {'POS': 'DET', 'OP': '+'}, {'POS': 'VERB', 'DEP': 'xcomp', 'MORPH': 'VerbForm=Gen','OP': '+'}],
[{'POS': 'VERB', 'DEP': 'ROOT','OP': '+'},  {'POS': 'VERB', 'DEP': 'xcomp', 'MORPH': 'VerbForm=Ger','OP': '+'}]
]

patternInf=[[{'POS': 'VERB', 'DEP': 'xcomp', 'MORPH': 'VerbForm=Inf','OP': '+'}, {'POS': 'DET', 'OP': '+'}, {'POS': 'VERB', 'DEP': 'xcomp', 'MORPH': 'VerbForm=Inf','OP': '+'}],
[{'POS': 'VERB', 'DEP': 'ccomp', 'MORPH': 'VerbForm=Inf','OP': '+'}, {'POS': 'VERB', 'DEP': 'xcomp','OP': '+'}],
[{'POS': 'VERB', 'OP': '+'}, {'POS': 'DET', 'OP': '+'}, {'POS': 'VERB', 'MORPH': 'VerbForm=Inf','OP': '+'}],
[{'POS': 'VERB', 'OP': '+'}, {'POS': 'ADP', 'OP': '+'}, {'POS': 'VERB', 'MORPH': 'VerbForm=Inf','OP': '+'}],
[{'POS': 'AUX', 'OP': '+'}, {'POS': 'ADP', 'OP': '+'}, {'POS': 'VERB', 'MORPH': 'VerbForm=Inf','OP': '+'}],
[{'POS': 'VERB', 'DEP': 'ROOT','OP': '+'},  {'POS': 'VERB', 'DEP': 'xcomp', 'MORPH': 'VerbForm=Inf','OP': '+'}]
]
matcher = Matcher(nlp.vocab) 
matcher.add('subbordinate', subbordinate)
matcher.add('Inf', patternInf)
matcher.add('Gen', patternGen)

# doc = nlp("Vengo observando su conducta desde") para vengo, llendo, sueño, sigo el lemma que adjudica es vengo

doc = nlp("iré observando su conducta desde")
matches = matcher(doc) 
print([(w.text, w.pos_, w.morph, w.tag_, w.dep_, w.lemma_, w.i) for w in doc])

	#print(int('subbordinate'))
	#print(doc.vocab.strings[match])


spans = []
for idText,start, end in matches:
	if doc.vocab.strings['subbordinate'] != idText:
		spans.append(doc[start:end])

doc = nlp(spans[0]);
print([(w.text, w.pos_, w.morph, w.tag_, w.dep_, w.lemma_, w.i) for w in doc])

'''
mapPeriphrasis = {}
for token in doc:
	for  idText,start, end in matches:
		if doc.vocab.strings['subbordinate'] != idText:
			if token.i == start:
				mapPeriphrasis[doc[start:end]] = {
				'lemma' : token.lemma_,
				'morph': token.morph,
				'type': getType(token.lemma_, doc.vocab.strings[idText])
				}
				print(token.lemma_, getType(token.lemma_,doc.vocab.strings[idText]))

print(spans)
print(mapPeriphrasis)
'''

