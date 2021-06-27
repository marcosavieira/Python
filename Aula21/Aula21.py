"""
for in em Python
iterando strings com for
função range(start=0, stop, step=1)
"""
texto = 'Python'
novaString = ''

# continue ---> pula para o proximo passo
# break ---> termina o laço

for letra in texto:
    if letra == 't':
        novaString += letra.upper()
    elif letra == 'h':
        novaString += letra.upper()
    else:
        novaString += letra

print(novaString)

