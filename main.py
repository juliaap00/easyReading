from modules.utils.nlp  import easyReading







def main():
	json = { 'id': 9,
			'name': 'Pauta - Evitar Perifrasis',
			'description': '''Se debería evitar el uso de dos o más verbos seguidos, 
								exceptuando las perífrasis con los verbos modales deber,
								querer, saber y poder.''',
			'pass': False,

			'reason':''' Algo parecido a "El texto presenta las siguientes
						perifrasis, que deberian evitarse: 
						[Se echó a llorar, ponerse a bailar].''',
			'originalText': 'Se echó a llorar en vez de ponerse a bailar.'
	}


	if json['pass'] == False:
		print(easyReading(json));


if __name__ == "__main__":
    main()

