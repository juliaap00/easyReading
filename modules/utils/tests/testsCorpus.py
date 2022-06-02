corpus = dict()

######################### PRUEBAS SENCILLAS ##########################

#Modal

corpus['Test 1 - Modal'] = { 'originalText' : 'Debo comprar una televisión.',	
'periphrasisList' : '[Debo comprar]', 
'simplifiedText' : 'Debo comprar una televisión.'
}

corpus['Test 2 - Modal'] = { 'originalText' : 'Quiero comprar una televisión.',	
'periphrasisList' : '[Quiero comprar]', 
'simplifiedText' : 'Quiero comprar una televisión.'
}
corpus['Test 3 - Modal'] = { 'originalText' : 'Hubo que comprar una televisión.',	
'periphrasisList' : '[Hubo que comprar]', 
'simplifiedText' : 'Hubo que comprar una televisión.'
}

corpus['Test 4 - Modal'] = { 'originalText' : 'Habrán de ser lo que hagamos.',	
'periphrasisList' : '[Habrán de ser]', 
'simplifiedText' : 'Habrán de ser lo que hagamos.'
}

corpus['Test 5 - Modal'] = { 'originalText' : 'Pareciera ser una fiesta.',	
'periphrasisList' : '[Pareciera ser]', 
'simplifiedText' : 'Pareciera ser una fiesta.'
}

corpus['Test 6 - Modal'] = { 'originalText' : 'Para que el pastel quede mejor, tienes que agregarle crema batida.',	
'periphrasisList' : '[tienes que agregarle]', 
'simplifiedText' : 'Para que el pastel quede mejor, tienes que agregarle crema batida.'
}

corpus['Test 7 - Modal'] = { 'originalText' : 'Él no ha de llegar tarde, sé que pronto llegará.',	
'periphrasisList' : '[ha de llegar]', 
'simplifiedText' : 'Él no ha de llegar tarde, sé que pronto llegará.'
}

corpus['Test 8 - Modal'] = { 'originalText' : 'Los ciclistas tienen que llevar siempre casco.',	
'periphrasisList' : '[tienen que llevar]', 
'simplifiedText' : 'Los ciclistas tienen que llevar siempre casco.'
}

corpus['Test 9 - Modal'] = { 'originalText' : 'Puede llover más tarde.',	
'periphrasisList' : '[Puede llover]', 
'simplifiedText' : 'Puede llover más tarde.'
}

corpus['Test 10 - Modal'] = { 'originalText' : 'Querría aproximarme a la barra.',	
'periphrasisList' : '[Querría aproximarme]', 
'simplifiedText' : 'Querría aproximarme a la barra.'
}


#Temporales sin matices
corpus['Test 1 - Temporal'] = { 'originalText' : 'Voy a conocer a tu padre.',	
'periphrasisList' : '[Voy a conocer]', 
'simplifiedText' : 'Conozco a tu padre.'
}

corpus['Test 2 - Temporal'] = { 'originalText' : 'Suelo comer con tu padre los domingos.',	
'periphrasisList' : '[Suelo comer]', 
'simplifiedText' : 'Como con tu padre los domingos.' #frecuentemente
}

corpus['Test 3 - Temporal'] = { 'originalText' : 'Sé cocinar fideos con pollo.',	
'periphrasisList' : '[Sé cocinar]', 
'simplifiedText' : 'Cocino fideos con pollo.'
}

corpus['Test 4 - Temporal'] = { 'originalText' : 'Se acostumbraron a cocinar fideos con pollo.',	
'periphrasisList' : '[Se acostumbraron a cocinar]', 
'simplifiedText' : 'Cocinaron fideos con pollo.' #frecuentemente
} #Reonocen acostumbró mal

corpus['Test 5 - Temporal'] = { 'originalText' : 'Acabaron de cocinar fideos con pollo.',	
'periphrasisList' : '[Acabaron de cocinar]', 
'simplifiedText' : 'Cocinaron fideos con pollo.' # de nuevo de que
}

corpus['Test 6 - Temporal'] = { 'originalText' : 'Volvieron a cocinar fideos con pollo.',	
'periphrasisList' : '[Volvieron a cocinar]', 
'simplifiedText' : 'Cocinaron fideos con pollo.' # de nuevo
}

corpus['Test 7 - Temporal'] = { 'originalText' : 'Tú te has acostumbrado a madrugar.',	
'periphrasisList' : '[te has acostumbrado a madrugar]', 
'simplifiedText' : 'Tú has madrugado.' #frecuentemente
}

corpus['Test 8 - Temporal'] = { 'originalText' : 'No sé cuando acabaré de leer este libro.',	
'periphrasisList' : '[acabaré de leer]', 
'simplifiedText' : 'No sé cuando leeré este libro.' # de nuevo de que
}

corpus['Test 9 - Temporal'] = { 'originalText' : 'Volverán a visitarme mañana.',	
'periphrasisList' : '[volverán a visitarme]', 
'simplifiedText' : 'Me visitarán mañana.'
}
corpus['Test 10 - Temporal'] = { 'originalText' : 'Esa tarde iban a salir a patinar.',	
'periphrasisList' : '[iban a salir]', 
'simplifiedText' : 'Esa tarde salían a patinar.'
}



#Fasales

#Inminencia
corpus['Test 1 - Fasales Inminencia'] = { 'originalText' : 'Estoy por conocer a tu padre.', #Inminencia	
'periphrasisList' : '[Estoy por conocer]', 
'simplifiedText' : 'Conozco a tu padre.' #Conoceré a tu padre
}

corpus['Test 2 - Fasales Incoativa'] = { 'originalText' : 'Empiezas a conocer a tu padre.', #Inminencia	
'periphrasisList' : '[Empiezas a conocer]', 
'simplifiedText' : 'Conoces a tu padre.'
}

corpus['Test 3 - Anterioridad Reciente'] = { 'originalText' : 'Había acabado de llorar con tu padre.', #Inminencia	
'periphrasisList' : '[Había acabado de llorar]', 
'simplifiedText' : 'Había llorado con tu padre.'#Debería no simplificase?
}

corpus['Test 4 - Terminativas'] = { 'originalText' : 'Habrán terminado de comer con ellos.', #Inminencia	
'periphrasisList' : '[Habrán terminado de comer]', 
'simplifiedText' : 'Habrán comido con ellos.'#Habré llorado más bien
}

corpus['Test 5 - Incoativa'] = { 'originalText' : 'Se echó a llorar con tu padre.', #Inminencia	
'periphrasisList' : '[Se echó a llorar]', 
'simplifiedText' : 'Lloró con tu padre.'
}
corpus['Test 6 - Incoativa'] = { 'originalText' : 'Se meterá a jugar al baloncesto.', #Inminencia	
'periphrasisList' : '[Se meterá a jugar]', 
'simplifiedText' : 'Jugará al baloncesto.'
}

corpus['Test 7 - Incoativa'] = { 'originalText' : 'Se decidió a bailar toda la noche.', #Inminencia	
'periphrasisList' : '[Se decidió a bailar]', 
'simplifiedText' : 'Bailó toda la noche.'
}

corpus['Test 8 - Incoativa'] = { 'originalText' : 'Rompió a llorar con tu padre.', #Inminencia	
'periphrasisList' : '[Rompió a llorar]', 
'simplifiedText' : 'Lloró con tu padre.'
}

#Terminativas
corpus['Test 9 - Terminativas'] = { 'originalText' : 'Dejó de llorar con tu padre.', #Inminencia	
'periphrasisList' : '[Dejó de llorar]', 
'simplifiedText' : 'Lloró con tu padre.'#Debería no simplificase?
}

corpus['Test 10 - Terminativas'] = { 'originalText' : 'Acabamos de llorar con la película.', #Inminencia	
'periphrasisList' : '[Acabamos de llorar]', 
'simplifiedText' : 'Lloramos con la película.'#Debería no simplificase?
}

'''
#Escalares
'''
corpus['Test 1 - Escalares'] = { 'originalText' : 'Alcanzó a probar el postre.', #Inminencia	
'periphrasisList' : '[Alcanzó a probar]', 
'simplifiedText' : 'Probó el postre.'#Debería no simplificase?
}

corpus['Test 2 - Escalares'] = { 'originalText' : 'Durante el acto los diputados acertarán a decir unas palabras.', #Inminencia	
'periphrasisList' : '[acertarán a decir]', 
'simplifiedText' : 'Durante el acto los diputados dirán unas palabras.'#Debería no simplificase?
}
corpus['Test 3 - Escalares'] = { 'originalText' : 'Si fuese mi idea, empezaría por llamar a mi jefe.', #Inminencia	
'periphrasisList' : '[empezaría por llamar]', 
'simplifiedText' : 'Si fuese mi idea, llamaría a mi jefe.'#Debería no simplificase?
}

corpus['Test 4 - Escalares'] = { 'originalText' : 'Habrán acabado por comer comida rápida.', #Inminencia	
'periphrasisList' : '[Habrán acabado por comer]', 
'simplifiedText' : 'Habrán comido comida rápida.'#Habrán dicho probably
}

#Terminarás no lo reconoce como morf xd
corpus['Test 5 - Escalares'] = { 'originalText' : 'No sé si llegará a ser presidente.', #Inminencia	
'periphrasisList' : '[llegará a ser]', 
'simplifiedText' : 'No sé si será presidente.'#Debería no simplificase?
}

corpus['Test 6 - Modal'] = { 'originalText' : 'No escuché lo que venía a comentar.', #Inminencia	
'periphrasisList' : '[venía a comentar]', 
'simplifiedText' : 'No escuché lo que venía a comentar.'#Debería no simplificase?
}
corpus['Test 7 - Escalares'] = { 'originalText' : 'Corrímos todo lo que pudimos pero no llegamos a subir al bus.', #Inminencia	
'periphrasisList' : '[llegamos a subir]', 
'simplifiedText' : 'Corrímos todo lo que pudimos pero no subimos al bus.'#Debería no simplificase?
}

corpus['Test 8 - Escalares'] = { 'originalText' : 'Él acabaría por ser nuestro jefe.', #Inminencia	
'periphrasisList' : '[acabaría por ser]', 
'simplifiedText' : 'Él sería nuestro jefe.'#Debería no simplificase?
}
corpus['Test 9 - Escalares'] = { 'originalText' : 'Tú llegaste a estar en la televisión.', #Inminencia	
'periphrasisList' : '[llegaste a estar]', 
'simplifiedText' : 'Tú estuviste en la televisión.'#Debería no simplificase?
}
corpus['Test 10 - Escalares'] = { 'originalText' : 'Empezaré por acabar los deberes.', #Inminencia	
'periphrasisList' : '[Empezaré por acabar]', 
'simplifiedText' : 'Acabaré los deberes.'#Debería no simplificase?
}

#Gerundio
corpus['Test 1 - Gerundio'] = { 'originalText' : 'Estoy diciendo unas palabras.', #Inminencia	
'periphrasisList' : '[Estoy diciendo]', 
'simplifiedText' : 'Digo unas palabras.'#Debería no simplificase?
}
corpus['Test 2 - Gerundio'] = { 'originalText' : 'Vas cantando todo el día.', #Inminencia	
'periphrasisList' : '[Vas cantando]', 
'simplifiedText' : 'Cantas todo el día.'#Debería no simplificase?
}

corpus['Test 3 - Gerundio'] = { 'originalText' : 'Anduve leyendo un par de libros.', #Inminencia	
'periphrasisList' : '[Anduve leyendo]', 
'simplifiedText' : 'Leí un par de libros.'#Debería no simplificase?
}

corpus['Test 4 - Gerundio'] = { 'originalText' : 'Mis abuelos vivieron viajando por Europa.', #Inminencia	
'periphrasisList' : '[vivieron viajando]', 
'simplifiedText' : 'Mis abuelos viajaron por Europa.'#Debería no simplificase?
}
#SE DEJA COMO ERROR
corpus['Test 5 - Gerundio'] = { 'originalText' : 'Venís discutiendo todo el viaje.', #Inminencia	DEJAR EN ERROR PARA ENSEÑAR QUE FALLA CUANDO ES 2 PERSONA DEL PLURAL
'periphrasisList' : '[Venís discutiendo]', 
'simplifiedText' : 'Discutís todo el viaje.'
}

#Viviríais no lo reconoce
corpus['Test 6 - Gerundio'] = { 'originalText' : 'Vivirán diciendo unas palabras.', #Inminencia	
'periphrasisList' : '[Vivirán diciendo]', 
'simplifiedText' : 'Dirán unas palabras.'#Debería no simplificase?
}

corpus['Test 7 - Gerundio'] = { 'originalText' : 'Hubo seguido diciendo unas palabras.', #Inminencia	
'periphrasisList' : '[Hubo seguido diciendo]', 
'simplifiedText' : 'Hubo dicho unas palabras.'#Todavia suena fatal
}

corpus['Test 8 - Gerundio'] = { 'originalText' : 'No hay por qué preocuparse, se pasarán durmiendo todo el día.', #Inminencia	
'periphrasisList' : '[se pasarán durmiendo]', 
'simplifiedText' : 'No hay por qué preocuparse, dormirán todo el día.'#Todavia suena fatal
}

corpus['Test 9 - Gerundio'] = { 'originalText' : 'Ni que hubiese continuado hablando.', #Inminencia	
'periphrasisList' : '[hubiese continuado hablando]', 
'simplifiedText' : 'Ni que hubiese hablado.'#Todavia suena fatal
}

corpus['Test 10 - Gerundio'] = { 'originalText' : 'Estaremos descansando de aquí a un año.', #Inminencia	
'periphrasisList' : '[Estaremos descansando]', 
'simplifiedText' : 'Descansaremos de aquí a un año.'#Todavia suena fatal
}


#Participio
#VA

corpus['Test 1 - Participio'] = { 'originalText' : 'Estarán cansados de tanto de correr.', #Inminencia	
'periphrasisList' : '[Estarán cansados]', 
'simplifiedText' : 'Estarán cansados de tanto de correr.'
} 

corpus['Test 2 - Participio'] = { 'originalText' : 'Nos tiene dicho que no.', #Inminencia	
'periphrasisList' : '[tiene dicho]', 
'simplifiedText' : 'Nos dice que no.'
} 

corpus['Test 3 - Participio'] = { 'originalText' : 'A pesar de haber estado ocupado toda la semana he salido.', #Inminencia	
'periphrasisList' : '[haber estado ocupado]', 
'simplifiedText' : 'A pesar de haber estado ocupado toda la semana he salido.'
} 

corpus['Test 4 - Participio'] = { 'originalText' : 'La cena hubiese sido mejor si él hubiese estado menos cansado.', #Inminencia	
'periphrasisList' : '[hubiese estado cansado]', 
'simplifiedText' : 'La cena hubiese sido mejor si él hubiese estado menos cansado.'
} 
corpus['Test 5 - Participio'] = { 'originalText' : 'Llevo leídas cuarenta páginas de mi libro.', #Inminencia	-> He 
'periphrasisList' : '[Llevo leídas]', 
'simplifiedText' : 'Leo cuarenta páginas de mi libro.'#NOS?
} 
corpus['Test 6 - Participio'] = { 'originalText' : 'Llevas recorridas cinco tiendas y no has comprado nada.', #Inminencia	
'periphrasisList' : '[Llevas recorridas]', 
'simplifiedText' : 'Recorres cinco tiendas y no has comprado nada.' # HAS RECORRIDO
} 
corpus['Test 7 - Participio'] = { 'originalText' : 'Estarán tan cansados que no cenarán.', #Inminencia	
'periphrasisList' : '[Estarán cansados]', 
'simplifiedText' : 'Estarán tan cansados que no cenarán.'
} 
corpus['Test 8 - Participio'] = { 'originalText' : 'Nos tiene prohibido.', #Inminencia	
'periphrasisList' : '[tiene prohibido]', 
'simplifiedText' : 'Nos prohíbe.'
} 






################## Test Primera Aproximación ##############################

corpus['Test 1'] = { 'originalText' : 'Volvió a acostumbrarse a tener que hacer lo que le pedían.',	
'periphrasisList' : '[volvió a acostumbrarse, acostumbrarse a tener, tener que hacer]', 
'simplifiedText' : 'Tuvo de nuevo que hacer lo que le pedían.'
}

corpus['Test 2']  = { 'originalText' : 'Schiller olía una manzana para ponerse a escribir, según dicen.',	
'periphrasisList' : '[ponerse a escribir]', 
'simplifiedText' : 'Schiller olía una manzana para escribir, según dicen.'
}


corpus['Test 3']  = { 'originalText' : 'No acertó sino a sacudir la cabeza en un gesto que trataba de ser una negociación.',
'periphrasisList' : '[acertó a sacudir, trataba de ser]',
'simplifiedText' : 'No sacudió sino la cabeza en un gesto que era una negociación.'	
}


corpus['Test 4'] = { 'originalText' : 'Vivieron tocando en directo toda su vida en pequeños clubes.',
'periphrasisList' : '[vivieron tocando]',
'simplifiedText' : 'Tocaron en directo toda su vida en pequeños clubes.'	
}


corpus['Test 5'] = { 'originalText' : 'Vengo observando su conducta desde que llegó a ser miembro de la academia.',
'periphrasisList' : '[vengo observando, llegó a ser]',
'simplifiedText' : 'Observo su conducta desde que fue miembro de la academia.'
}

corpus['Test 6'] = { 'originalText' : 'Me lo dijo poniéndose a sonreír con dulzura.',
'periphrasisList' : '[poniéndose a sonreír]',
'simplifiedText' : 'Me lo dijo sonriendo con dulzura.'
}

corpus['Test 7'] = { 'originalText' : 'Se echó a llorar al ver los lugares donde solían ir a veranear juntos.',
'periphrasisList' : '[se echó a llorar, solían ir, ir a veranear]',
'simplifiedText' : 'Lloró al ver los lugares donde veraneaban con frecuencia juntos.' # PARTE 2
}

corpus['Test 8'] = { 'originalText' : 'Te tengo dicho que no molestes.',
'periphrasisList' : '[tengo dicho]', #???
'simplifiedText' : 'Te tengo dicho que no molestes.'
}

corpus['Test 9'] = { 'originalText' : 'Solía entonces venir a vernos los domingos, antes de que todo empezase a cambiar.',
'periphrasisList' : '[solía venir, venir a vernos ,empezase a cambiar]',
'simplifiedText' : 'Venía entonces con frecuencia a vernos los domingos, antes de que todo cambiase.'
}

corpus['Test 10'] = { 'originalText' : 'Está ahora teniendo que empezar a dar explicaciones sobre lo ocurrido.',
'periphrasisList' : '[está teniendo, teniendo que empezar, empezar a dar]',
'simplifiedText' : 'Tiene ahora que dar explicaciones sobre lo ocurrido.'
}

corpus['Test 11'] = { 'originalText' : 'La noche prometía ser tibia y perfumada.',
'periphrasisList' : '[prometía ser]',
'simplifiedText' : 'La noche era tibia y perfumada.'
}

corpus['Test 12'] = { 'originalText' : 'No supo convencer a los miembros del jurado en su defensa.',
'periphrasisList' : '[supo convencer]',
'simplifiedText' : 'No convenció a los miembros del jurado en su defensa.'
}

corpus['Test 13'] = { 'originalText' : 'Me puse a dormir nada más llegar a casa.',
'periphrasisList' : '[puse a dormir]',
'simplifiedText' : 'Me dormí nada más llegar a casa.'
}

corpus['Test 14'] = { 'originalText' : 'Tiene que haber sido el viento.',
'periphrasisList' : '[Tiene que haber sido]',
'simplifiedText' : 'Habrá sido el viento.'
}

corpus['Test 15'] = { 'originalText' : 'Estoy por recomendarte esta serie.',
'periphrasisList' : '[Estoy por recomendarte]',
'simplifiedText' : 'Te recomiendo esta serie.'
}

corpus['Test 16'] = { 'originalText' : 'Solía trabajar cantando las canciones.',
'periphrasisList' : '[Solía trabajar, trabajar cantando]',
'simplifiedText' : 'Cantaba con frecuencia las canciones.'
}

corpus['Test 17'] = { 'originalText' : 'Si no se pasase comiendo fuera habría aprobado el examen.',
'periphrasisList' : '[se pasase comiendo]',
'simplifiedText' : 'Si no comiese fuera habría aprobado el examen.'
}

corpus['Test 18'] = { 'originalText' : 'Terminaba de trabajar llorando cada día.',
'periphrasisList' : '[Terminaba de trabajar, trabajar llorando]',
'simplifiedText' : 'Lloraba cada día.'
}

corpus['Test 19'] = { 'originalText' : 'Mis padres solían ir antes a pasear con mis hermanos cuando íbamos a explorar.',
'periphrasisList' : '[solían ir, ir a pasear, íbamos a explorar]',
'simplifiedText' : 'Mis padres paseaban con frecuencia antes con mis hermanos cuando explorábamos.'
}


corpus['Test 20'] = { 'originalText' : 'Mis padres solían ir antes de que naciese yo a pasear con mis hermanos cuando íbamos solos sin supervisión a explorar.',
'periphrasisList' : '[solían ir, ir a pasear, íbamos a explorar]',
'simplifiedText' : 'Mis padres paseaban con frecuencia antes de que naciese yo con mis hermanos cuando explorábamos solos sin supervisión.'
}

corpus['Test 21'] = { 'originalText' : 'Tiene que haber comido antes de las dos.',
'periphrasisList' : '[Tiene que haber comido]',
'simplifiedText' : 'Habrá comido antes de las dos.'
}
'''
##################### Test Segunda Aproximación ####################################
'''
corpus['Test 22'] = { 'originalText' : 'Suele comprar los domingos.',
'periphrasisList' : '[Suele comprar]',
'simplifiedText' : 'Compra con frecuencia los domingos.'
}

corpus['Test 23'] = { 'originalText' : 'Alberto sigue cocinando los findes.',
'periphrasisList' : '[sigue cocinando]',
'simplifiedText' : 'Alberto cocina todavía los findes.'
}

corpus['Test 24'] = { 'originalText' : 'El niño vuelve a salir al parque.',
'periphrasisList' : '[vuelve a salir]',
'simplifiedText' : 'El sale de nuevo al parque.'
}

corpus['Test 24'] = { 'originalText' : 'Suele ir a comprar los domingos.',
'periphrasisList' : '[Suele ir, ir a comprar]',
'simplifiedText' : 'Compra con frecuencia los domingos.'
}

corpus['Test 25'] = { 'originalText' : 'Continuaron comiendo después de hablar.',
'periphrasisList' : '[Continuaron comiendo]',
'simplifiedText' : 'Comieron aún después de hablar.'
}

corpus['Test 26'] = { 'originalText' : 'Solían irse de vacaciones a París.',
'periphrasisList' : '[Solían irse]',
'simplifiedText' : 'Se iban con frecuencia de vacaciones a París.'
}

corpus['Test 27'] = { 'originalText' : 'Volví a cantar con mi familia.',
'periphrasisList' : '[Volví a cantar]',
'simplifiedText' : 'Canté de nuevo con mi familia.'
}

corpus['Test 28'] = { 'originalText' : 'Habéis vuelto a viajar gratis.',
'periphrasisList' : '[Habéis vuelto a viajar]',
'simplifiedText' : 'Habéis viajado de nuevo gratis.'
}

corpus['Test 28'] = { 'originalText' : 'Ellos siguen viajando con su familia por Navidad.',
'periphrasisList' : '[siguen viajando]',
'simplifiedText' : 'Ellos viajan todavía con su familia por Navidad.'
}

#Test Complejos 



corpus['Test 29'] = { 'originalText' : 'Estará ahora teniendo que volver a empezar a dar explicaciones sobre lo ocurrido.',
'periphrasisList' : '[Estará teniendo, teniendo que volver, volver a empezar, empezar a dar]',
'simplifiedText' : 'Tendrá ahora que dar de nuevo explicaciones sobre lo ocurrido.'
}

corpus['Test 29'] = { 'originalText' : 'Estará ahora teniendo que volver a empezar a dar explicaciones sobre lo ocurrido.',
'periphrasisList' : '[Estará teniendo, teniendo que volver, volver a empezar, empezar a dar]',
'simplifiedText' : 'Tendrá ahora que dar de nuevo explicaciones sobre lo ocurrido.'
}

corpus['Test 30'] = { 'originalText' : 'Tenemos que haber llamado al médico que solíamos visitar antes de empezar a mudarnos.',
'periphrasisList' : '[Tenemos que haber llamado, solíamos visitar, empezar a mudarnos]',
'simplifiedText' : 'Habremos llamado al médico que visitamos con frecuencia antes de mudarnos.'
}




