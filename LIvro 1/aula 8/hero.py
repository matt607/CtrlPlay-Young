import os 
if not os.path.exists('hero.txt'):
    with open('hero.txt', 'w', encoding='utf-8') as hero:
        hero.write('Homem-Aranha - Marvel')
    print('Arquivo criado.')
else:
    print('Arquivo Existente.')

with open('hero.txt', 'a', encoding='utf-8') as hero:
    hero.write('\n')
    hero.write(input('Digite um filme: '))
 
with open('hero.txt', 'r', encoding='utf-8') as hero:
    print(hero.seek(2))
    print(hero.read())