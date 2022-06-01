from pprint	 import pprint
from modules.utils.contextAdder.dataContext import contextMap 


def addContext(periphrasisMap, verb):
	pattern = periphrasisMap['pattern'].split(" ")
	if pattern[0] in contextMap.keys():
		verbDict = {
		'verb' : verb,
		'context' : contextMap[pattern[0]]
		}
		verbDict['explanation'] = f"y se ha añadido el contexto '{verbDict['context']}' a la simplificación para evitar la pérdida de matices al simplificar."
		return verbDict
	return verb
