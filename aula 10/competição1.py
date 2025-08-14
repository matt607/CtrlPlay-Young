n = input('Digite uma sequência de numeros:  ')
if len(n) < 5:
    print('Sequência tem que ter pelo menos 5 digítos')
else:
    print('Sequência validada com sucesso')

contador = 0
for digito in str(n):
    if int(digito) % 2 == 0:
        contador += 1

print(f'A Sequência tem {contador} numeros pares')
