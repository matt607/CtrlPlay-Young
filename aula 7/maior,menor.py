def menor(lista):
    menorValor = lista[0]
    for x in lista:
        if(x<menorValor):
            menorValor=x
    return menorValor
def maior(lista):
    maiorValor = lista[0]
    for x in lista:
        if(x>maiorValor):
            maiorValor=x
    return maiorValor
def maiorEMenor(lista):
    print('Maior:', maior(lista))
    print('Menor:', menor(lista))