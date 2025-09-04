class Carro():

    def __init__(self, marca ,modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def dadosCompleto(self):
        return 'Dados Completo: '+self.marca+' , '+self.marca+' - ano: '+ self.ano

carro1 = Carro('Ford','Mustang Shelby GT500', '2023')
carro2 = Carro('Volkswagen','Golf GTI', '2018')
carro3 = Carro('Nissan','GT-r 35', '2020')

carro1 = Carro()
print(carro1.dadosCompleto())
print(carro1.marca)
print(carro2.modelo)
print(carro3.ano)
