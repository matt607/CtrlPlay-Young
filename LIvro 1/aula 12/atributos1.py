
class Casa():

    def __init__(self, rua ,bairro, cep):
        self.rua = 'Blue Street'
        self.bairro = 'Good Neighborhood'
        self.CEP = '123654'

    def enderecoCompleto(self):
        return 'Endereço Completo: '+self.rua+' , '+self.bairro+' - CEP: '+ self.CEP

casa1 = Casa()
print(casa1.enderecoCompleto())
print(casa1.bairro)
print(casa1.rua)
print(casa1.CEP)
