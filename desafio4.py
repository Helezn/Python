first_name = input('Por favor, digite o seu nome: ') #por defaul imput armazena string

age = int(input('Agora, digite sua idade: '))

print(type(first_name))

print (type(age))

#formas para apresentar o resultado:

print('Olá, {}! Você tem {} anos.' .format(first_name, age))

print('Olá,', first_name,'! Você tem', age, 'anos.')

print (f'Olá, {first_name}! Você tem {age} anos.')