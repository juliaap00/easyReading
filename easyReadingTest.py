from modules.utils.nlp  import easyReading
from modules.utils.tests.testsCorpus  import corpus

def main():
	json = { 'id': 9,
			'name': 'Pauta - Evitar Perifrasis',
			'description': '''Se debería evitar el uso de dos o más verbos seguidos, 
								exceptuando las perífrasis con los verbos modales deber,
								querer, saber y poder.''',
			'pass': False
			}

	reason = '''Algo parecido a "El texto presenta las siguientes
				perifrasis, que deberian evitarse: 
				'''

	for key, value in corpus.items():
		#if key == 'Test 1':
		json['originalText'] = value['originalText']	
		json['reason'] = f"{reason} {value['periphrasisList']}"
		actualValue = easyReading(json)
		#print(f"Actual len: {len(actualValue)}")
		#print(f"Expected len: {len(value['simplifiedText'])}")

		if actualValue != value['simplifiedText']:
			print(f'---------------{key}: ERROR-----------------')

			print(f"Expected {value['simplifiedText']}")
			print(f"Actual {actualValue}")
			
		else:
			#print('---------------PASS-----------------') 
			print(f'---------------{key}: PASS -----------------')
			print(f"Original {value['originalText']}")
			print(f"Simplified {actualValue}")
			'''
			print(f"Original {value['originalText']}")
			print(f"Simplified {value['simplifiedText']}")
		'''




if __name__ == "__main__":
    main()

