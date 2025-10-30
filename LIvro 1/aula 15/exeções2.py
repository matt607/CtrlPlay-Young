try:
    f = open('arquivo.txt', 'r')
    f.write('tente escrever isto')
except IOError:
    #isso só irá verificar se há uma exceção IOError e em seguida6
    #executar essa declaração impressa
    print('Não é possivel localizar o arquivo')
else:
    print('Texto escrito com sucesso!')
    f.close