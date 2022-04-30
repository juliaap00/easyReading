from morphy.preprocessing import MultiLang
text = 'comía supe'
spanish = MultiLang(lang='es')
doc = spanish(text)
for token in doc.tokens:
    print('%s --> %s' % (token.text, token.lemma, token.morph))
