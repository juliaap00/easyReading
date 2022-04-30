# Load word_dict and composite_dict
import torch
model = torch.load('~/stanza_resources/en/lemma/ewt.pt', map_location='cpu')
word_dict, composite_dict = model['dicts']

# Customize your own dictionary
composite_dict[('myword', 'NOUN')] = 'mylemma'
word_dict['ponerme'] = 'poner'

# Save your model
torch.save(model, '~/stanza_resources/en/lemma/ewt_customized.pt')

# Load your customized model with Stanza
import stanza
nlp = stanza.Pipeline('en', package='ewt', processors='tokenize,pos,lemma', lemma_model_path='~/stanza_resources/en/lemma/ewt_customized.pt'
print(nlp('myword')) # Should get lemma 'mylemma'