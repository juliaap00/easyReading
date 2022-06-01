from spellchecker import SpellChecker

def isExsistantWord(lemma, spell):
	misspelled = [lemma]
	misspelled = spell.unknown(misspelled)
	
	return True if not misspelled  else False
