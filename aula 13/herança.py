class Animal():
    def __init__(self):
        print('Animal criando')

    def oQueSou(self):
        print('Animal')

    def come(self):
        print('Comendo')

class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Cachorro criando')
    
    def oQueSou(self):
        print('Cachorro')

    def late(self):
        print('Auau!')

c = Cachorro()

c.oQueSou()

c.come()

c.late()

class AnimalSelvagem():

    def mover(self):
        print('estou correndo')

    def come(self):
        print('Comendo')

class AnimalDomesticado():
    def mover(self):
        print('estou andando')
    
    def getDono(self):
        return self.dono

class Cachorro(AnimalSelvagem, AnimalDomesticado ):
    def __init__(self,dono):
        self.dono = dono

    def late(self):
        print('Auau!')

c = Cachorro('Luís')

print(c.getDono())
c.come()
c.late()
c.mover()

