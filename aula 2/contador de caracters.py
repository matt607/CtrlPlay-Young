#veja quantas carcters formam a frase a seguir:
frase = 'Ctrl+Play - Escola de Programação e Robótica'
print(len(frase))

senha = input('Digite sua Senha: ')
if len(senha) < 8:
    print('Senha menor que 8 digítos')
else:
    print('Senha cadastrada com sucesso')

nome = 'Matheus Sartner'
#imprimindo a primeira letra do nome
print(nome[0])
#imprimindo a partir  de um caractere
print(nome[7:])
#imprimindo a partir  de um caractere
print(nome[:7])
#imprimindo uma parte de um string
print(nome[10:15])
#também pode ser usado número negativos para retroceder
print(nome[-1])
#tudo menos a última letra
print(nome[:-1])
