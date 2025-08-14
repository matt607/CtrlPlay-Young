import calculadora 

def menu():
    while True:
        print('* [1] - Soma *')
        print('* [2] - Subtrair *') 
        print('* [3] - Multiplicar *')
        print('* [4] - Dividir *')
        print('* [5] - Sair *')
        opt = int(input('Obção Desejada:  '))

        if opt == 1:
            num1 = int(input('Digite nº 1:  '))
            num2 = int(input('Digite nº 2:  '))
            print(calculadora.soma(num1,num2))
            pause = input('')
        elif opt == 2:
            num1 = int(input('Digite nº 1:  '))
            num2 = int(input('Digite nº 2:  '))
            print(calculadora.subtrair(num1,num2))
            pause = input('')
        elif opt == 3:
            num1 = int(input('Digite nº 1:  '))
            num2 = int(input('Digite nº 2:  '))
            print(calculadora.multiplicar(num1,num2))
            pause = input('')
        elif opt == 4:
            num1 = int(input('Digite nº 1:  '))
            num2 = int(input('Digite nº 2:  '))
            print(calculadora.dividir(num1,num2))
            pause = input('')
        elif opt ==5:
            break
        else:
            menu()