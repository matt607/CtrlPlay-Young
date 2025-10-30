def SobrenomeNaOrdem(nome, sobrenome1, sobrenome2):
    if(len(sobrenome1)<len(sobrenome2)):
        return nome + ' ' + sobrenome1 + ' ' + sobrenome2
    else:
        return nome + ' ' + sobrenome1 + ' ' + sobrenome2

print(SobrenomeNaOrdem('Jorge', 'Dolglas', 'da Silva'))
print(SobrenomeNaOrdem('Cristino', 'Ronaldo', 'Junior'))
