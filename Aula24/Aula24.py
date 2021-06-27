"""
Split Join Enumerate em Python
* split - dividir uma string # str
* join - juntar uma string # str
* enumerate - enumerar elementos da lista # iteráveis
"""

string = 'O Brasil é penta! '
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(f'O indice é: {indice}\n O valor é: {valor}\n A lista com indice é: {lista[indice]}')

lista2 = ['Marcos', 'Pamela', 'Brenno']

for indice2, nome in enumerate(lista2):
    print(f'O indice é: {indice2}\n O nome é: {nome}')



