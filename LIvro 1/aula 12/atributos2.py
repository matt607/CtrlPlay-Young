class Casa():
    imobiliaria = "Ctrl Imóveis"
    def __init__(self, rua ,bairro, cep):
        self.rua = rua
        self.bairro = bairro
        self.CEP = cep

    def enderecoCompleto(self):
        return 'Endereço Completo: '+self.rua+' , '+self.bairro+' - CEP: '+ self.CEP

    def getImobiliaria(self):
        return self.imobiliaria
    def getRua(self):
        return self.rua
    def getBairro(self):
        return self.bairro
    def getCEP(self):
        return self.CEP

    def setImobiliaria(self, i):
        self.imobiliaria = i
    def setRua(self, imc):
        self.rua = i
    def setBairro(self, i):
        self.bairro = i
    def setCEP(self, i):
        self.CEP = i

casa1 = Casa('Julio','Nova Monte Seerat', '13288-136')
casa2 = Casa('Antônio','Rios das Pedradas', '13299-158')
casa3 = Casa('Maria','Jd. Angélicas', '13299-798')

print(casa1.enderecoCompleto())
print(casa2.enderecoCompleto())
print(casa3.enderecoCompleto())
print(casa1.imobiliaria)
print(casa2.imobiliaria)
print(casa3.imobiliaria)

casa1.setBairro('Cafezal')
print(casa1.getBairro())
