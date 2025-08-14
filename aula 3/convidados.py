convidados = ['José', 'Lucas', 'Ana', 'Enzo', 'Valentina','CR7', 'Messi', 'Neymar Jr']
print(convidados)

print(f'A primeira pessoa da lista é {convidados[0]}')

print(convidados[-3])

convidados[2] = 'Beatriz'
print(convidados)

convidados.append('Joaquim')
print(convidados)

convidados.insert(0, 'João')
print(convidados)

del convidados[3]
print (convidados)

convidadoRemovido = convidados.pop()
print(convidados)

convidadoRemovido2 = convidados.pop(3)
print(convidados)

viajando ='João'
convidados.remove(viajando)
print(f'O {viajando} não vai, pois está viajando!')
print(convidados)


print(sorted(convidados))
print(convidados)

convidados.sort()
print(convidados)
convidados.sort(reverse=True)
print(convidados)

convidados.reverse()
print(convidados.reverse())
print(convidados)
