frutas = ['maça', 'banana', 'manga', 'uva']

frutas[1] = 'morango'
frutas.append('abacaxi') #insere no fim
print(frutas)

frutas[1:2] = ['abacate', 'laranja'] #substitui posição 1 pelos elementos
print(frutas)

frutas[1:3] = ['pera', 'melancia'] #substitui posição de 1 até 3 mas não inclui o 3
print(frutas)

frutas.insert(2, 'limão')
print(frutas)