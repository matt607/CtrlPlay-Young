def pergunta_Numero():
    numero = 1
    while True:
        try:
            val = int(input('Entre un inteiro: '))
        except:
            print('Parece que você não digitou um inteiro')
            continue
        else:
            print('Parece que você não digitou um inteiro!')
            break
        finally:
            print('Tentativa numero: ', numero)
            numero = numero + 1

    print(val)
    
pergunta_Numero()