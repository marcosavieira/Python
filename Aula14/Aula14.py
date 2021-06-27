num1 = input('Digite o primeiro numero: ')
num2 = input('Digite o segundo numero: ')

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
else:
    print('Error')
