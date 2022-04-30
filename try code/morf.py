import spacy
from spacy.matcher import Matcher
import re

nlp = spacy.load('es_core_news_sm')
doc = nlp("Tu comías pipas")

print([(w.text, w.pos_, w.morph, w.tag_, w.dep_, w.lemma_, w.i) for w in doc])