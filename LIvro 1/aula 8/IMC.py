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