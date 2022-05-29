from modules.utils.periphrasisSimplifier  import periphrasisSimplifier
from modules.utils.tests.testsCorpus import corpus
import time
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
		tic = time.perf_counter()
		jsonAux = periphrasisSimplifier(value['originalText'], value['periphrasisList'].replace('[','').replace(']', ''))
		toc = time.perf_counter()

		actualValue = jsonAux['simplifiedText']
		explanation = jsonAux['explanation']
		if actualValue != value['simplifiedText']:
			print(f'---------------{key}: ERROR-----------------')

			print(f"Expected: {value['simplifiedText']}")
			print(f"Actual: {actualValue}")
			print(f"Explanation: {explanation}")
			print(f"Time: {toc - tic:0.4f} seconds")

			
		else:
			print(f'---------------{key}: PASS -----------------')
			print(f"Original: {value['originalText']}")
			print(f"Simplified: {actualValue}")
			print(f"Explanation: {explanation}")
			print(f"Time: {toc - tic:0.4f} seconds")
			
			#print(f"Original {value['originalText']}")
			#print(f"Simplified {value['simplifiedText']}")
		




if __name__ == "__main__":
    main()

