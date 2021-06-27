nome = input('Digite o seu nome: ')

nomeC = 4
nomeN = 6

if len(nome) <= nomeC:
    print(f'{nome} é um nome muito curto')
elif len(nome) <= 6:
    print(f'{nome} é um nome normal')
else:
    print(f'{nome} é um nome muito grande')
