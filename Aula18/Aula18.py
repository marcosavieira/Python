while True:
    print()

    sair = input('Voce deseja sair? [s]im [n]ão: ')

    if sair == 's':
        print('Fim do programa!')
        break

    num1 = input('Digite um numero:\n')
    oper = input('digite o operador:\n')
    num2 = input('Digite outro numero:\n')

    if not num1.isnumeric() or not num2.isnumeric():
        print('Voce precisa digitar numeros!')
        continue

    num1 = int(num1)
    num2 = int(num2)

    if oper == '+':
        print(num1 + num2)
    elif oper == '-':
        print(num1 - num2)
    elif oper == '*':
        print(num1 * num2)
    elif oper == '/':
        print(f'{num1 / num2:.2f}')
    else:
        print('Operação não válida')
