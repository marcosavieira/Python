"""
For / Else em Python
"""

variavel = ['Marcos', 'Pamela', 'Brenno']

for valor in variavel:
    if valor.lower().startswith('M'):
        print(f'{valor} Começa com M ')
    else:
        print(f'{valor} Não Começa com M')
