with open ('teste1.txt', 'w', encoding='utf-8') as boas_vindas:
    boas_vindas.write('Hello World! My name is "Andrew"\n Are you ready?')
    print('Arquivo criado com sucesso!')

with open ('teste1.txt', 'r', encoding='utf-8') as ler_msg:
    print(ler_msg.read())

with open ('teste1.txt', 'a', encoding='utf-8') as acrescentar:
    acrescentar.write('\nEssa linha foi acrescentar depois!')
 #atividade 1 - 
