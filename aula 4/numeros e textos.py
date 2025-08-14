numero1 = 10
numero2 = 50
texto1 = 'Crtl'
texto2 = 'Play'

numero1 * 5 == numero2
print(numero1 * 5 == numero2)
texto1 == texto2
print(texto1 == texto2)

numero1 != numero2
print(numero1 != numero2)
texto1 != texto2
print(texto1 != texto2)

print(numero1 > numero2)
print(texto1 >= texto2)
print(numero1 < numero2)
print(texto1 <= texto2)

print('12' < 'doze')
print(1<2<3)

nota = 8
if nota >= 7:
    print('APROVADO!')
elif nota > 4 and nota < 7:
    print('RECUPERAÇÃO')
else:
    print('REPROVADO!')
