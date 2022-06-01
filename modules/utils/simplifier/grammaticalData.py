
reflexiveSuffix = {
'lar' : 'le',
'tar' : 'te',
'mar' : 'me'	
}

reflexivePronouns = ['me', 'te', 'se', 'nos', 'os']

subjTerminations2 = ['ese', 'eses', 'ésemos', 'eseis', 'esen', 'ase', 'ases', 'ásemos', 'aseis', 'asen']

morphologicalMap = {
	'Ind' : 'Indicativo',
	'Sub' : 'Subjuntivo',
	'Cnd' : 'Condicional',
	'Sing': 's',
	'Plur': 'p',
	'Pres': 'presente',
	'Ger': 'presente',
	'Imp': 'pretérito imperfecto',
	'Past': 'pretérito perfecto simple',
	'Fut': 'futuro',
	#'Cond': 'Condicional',
	'Inf': ['Infinitivo','Infinitivo Infinitivo'],
	'Ger': ['Gerundio','Gerundio Gerondio'],
	'Part': ['Participo','Participo Participo']
} 

periphrasisType = dict()

infinitiveMap = { 'ir a': 'Posterioridad Inmmediata',
		'soler': 'Temporal Frecuentiva', # a menudo
		'saber': 'Temporal', #bien
		'acabar de': 'Temporal Anterioridad reciente', #Puede ser Anterioridad reciente o terminativa
		'terminar de': 'Tempoactual',
		'acostumbrar' : 'Frecuentiva',
		'acostumbrar a' : 'Frecuentiva',
		'volver a' : 'Frecuentiva',
		'estar por': 'Inminencia',
		'estar para': 'Inminencia',
		'estar a punto de': 'Inminencia', #a ver que hacemos, supongo pillar todo lo que se complemento mm
		'empezar a' : 'Incoactiva',
		'echar a' : 'Incoactiva', #echarse
		'echarse a' : 'Incoactiva', #echarse
		
		'comenzar a' : 'Incoactiva',
		'ponerse a' : 'Incoactiva',
		'poner a' : 'Incoactiva', #ponerse 
		'entrar a' : 'Incoactiva',
		'dejar de' : 'Terminativa',
		'cesar de' : 'Terminativa',
		#'acabar de' : 'Terminativa', #Colisiona con acabar de tempoactual --> MATICES ?
		'terminar de' : 'Terminativa',
		'pasar a': 'Transitiva', #me lo he inventado 
		'empezar por': 'Escalares',
		'acabar por': 'Escalares',
		'terminar por': 'Escalares',
		'llegar a': 'Escalares',
		'deber' : 'Modal', # Radical de Obligacion',
		'tener que': 'Modal', #de Obligacion',
		'haber de': 'Modal', #de Obligacion',
		'haber que': 'Modal', #de Obligacion',
		'poder' : 'Modal', #Radical Capacidad', #colisiones tb 
		'deber de': 'Modal', #Probabilidad',
		#'haber de': 'Modal', #Probabilidad', #colisiona
		#'tener que': 'Modal', #'Certeza' #colisiona
		'venir a': 'Modal', #'Aproximacion',
		'parecer': 'Modal',
		'querer': 'Modal'

}

gerundMap =  { 'estar' : 'Principal Cursiva',
		'ir' : 'Principal Cursiva',
		'venir': 'Principal Cursiva',
		'andar': 'Principal',
		'llevar': 'Cursiva',
		'pasar' : 'Cursiva',
		'pasarse': 'Cursiva',
		'vivir': 'Frecuentiva', 
		'seguir': 'Frecuentiva',
		'continuar': 'Frecuentiva',
		'empezar': 'Escalares',
		'acabar': 'Escalares',
		'terminar': 'Escalares',
	}

periphrasisType['Inf'] = infinitiveMap 
periphrasisType['Ger'] = gerundMap 