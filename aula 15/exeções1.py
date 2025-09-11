try:
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')

    resultado = int(num1) / int(num2)
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero')

except ValueError:
    print('Você precisa digitar apenas números.')
else:
    if int(num1) < 0 or int(num2) < 0:
        print('Números negativos não são permitidos')
    else:
        print(f'O resultado é: {resultado}')