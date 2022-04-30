import spacy
from spacy.matcher import Matcher
import re
#python -m spacy download es_core_news_lg
nlp = spacy.load('es_core_news_lg')
doc = nlp("os ponemos guapas")
print([(w.text, w.pos_, w.morph, w.tag_, w.dep_, w.lemma_, w.i) for w in doc])