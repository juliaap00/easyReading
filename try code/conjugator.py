import mlconjug3

default_conjugator = mlconjug3.Conjugator(language='es')

test1 = default_conjugator.conjugate("comer").conjug_info['Infinitivo']['Infinitivo Infinitivo']['']
print(test1)

