'''



#Aula 7

def boas_vindas():
    print('Bem-Vindo à CTRL+Play!')

boas_vindas()

def boas_vindas(nomeDeUsuario):
    print('Bem-vindo(a),', nomeDeUsuario , 'à Ctrl+Play!')

    boas_vindas('Renner')

def filme_favorito(titulo):
    print(f'Meu filme favorito é {titulo}.')

    filme_favorito('Como treinar seu Dragão')

def velocidade(distancia,tempo):
    print(distancia/tempo)
velocidade(10,20)
velocidade(distancia=100 , tempo=10 )

def menor(a, b): 
    if a<=b:
        return a
    else:
        return b
    
    a=5
    b=1

print(f'O menor valor entre {a} e {b} é {menor(a,b)}')


def prepara_acai(*ingredientes, tamanho='medio'):
    print('\n Preparando um Açaí', tamanho, 'com os seguintes ingredientes: ')
    for ingrediente in ingredientes:
        print('-', ingrediente)
         
prepara_acai('banana', 'granola')

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

maiorEMenor([4,5,6,2,1,3])

def dobraLencol(lencol,gaveta):
    if(lencol<gaveta):
        return 0
    else:
        return 1 + dobraLencol(lencol/2,gaveta)
    
print(dobraLencol(200,25))
'''

#Aula 8

#1 atividade IMC

def IMC(peos,altura):
    IMC = peso / (altura**2)
    return round(IMC, 2)

peso=float(input('Digite seu peso(kg): '))
altura = float(input('Digite sua altura(m): '))
IMC= IMC(peso, altura)
print(f'Seu imc é: {IMC}')
if IMC < 18.5:
    print('Abaixo do peso')
elif IMC < 24.5:
    print('Peso normal')
elif IMC < 29.9:
    print('Sobrepeso')
elif IMC < 34.9:
    print('Obesidade grau 1')
elif IMC <39.9:
    print('Obsidade grau 2')
else:
    print('Obsidade grau 3')

#2 Atividade calcular comprimento de uma string

