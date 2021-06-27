hora = input('Digite que horas são: ')

bomDia = 11
boaTarde = 17
boaNoite = 23

if hora.isnumeric() and int(hora) <= bomDia:
    print('Bom dia')
elif hora.isnumeric() and int(hora) <= boaTarde:
    print('Boa tarde')
elif hora.isnumeric() and int(hora) <= boaNoite:
    print('Boa Noite')
else:
    print('Hora Inválida')
