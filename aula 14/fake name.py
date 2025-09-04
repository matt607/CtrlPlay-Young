from faker import Faker
fake = Faker('pt-br')

def SobrenomeNaOrdem(nome, sobrenome1, sobrenome2):
    if(len(sobrenome1)<len(sobrenome2)):
        return nome + ' ' + sobrenome1 + ' ' + sobrenome2
    else:
        return nome + ' ' + sobrenome1 + ' ' + sobrenome2

print(SobrenomeNaOrdem(fake.first_name(),fake.last_name(),fake.last_name()))
print(SobrenomeNaOrdem(fake.first_name(),fake.last_name(),fake.last_name()))
print(fake.name())