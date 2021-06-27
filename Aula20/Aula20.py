frase = 'o rato roeu a roupa do rei de roma'
tamanho = len(frase)
contador = 0
nova_frase = ''

while contador < tamanho:
    letra = frase[contador]
    if letra == 'r':
        nova_frase += 'R'
    else:
        nova_frase += letra
    contador += 1

print(nova_frase)
