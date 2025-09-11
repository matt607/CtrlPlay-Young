def pergunta_Numero():
    try:
        val = int(input('Entre un inteiro: '))
    except:
        print('Parece que você não digitou um inteiro')
    finally:
        print('Executei!')
pergunta_Numero()
