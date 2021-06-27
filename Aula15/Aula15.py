num = input('Digite um número inteiro: ')

if num.isnumeric() and int(num) % 2 == 0:
    print('Número é par')
elif not num.isnumeric():
    print('O número não é válido')
else:
    print('O numero é impar')





