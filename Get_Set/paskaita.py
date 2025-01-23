class Darbuotojas:
    def __init__(self, vardas, pavarde, atlyginimas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.__atlyginimas = atlyginimas
        
    @property        
    def atlyginimas(self):
        return self.__atlyginimas
    
    
    @atlyginimas.setter
    def atlyginimas(self, naujas):
        if naujas < 0:
            print("Altyginimas negali buti neigiamas")
        else:
            self.__atlyginimas = naujas
            
domas = Darbuotojas("Domas", "Rutkauskas", 1200)
print(domas.atlyginimas)

domas.atlyginimas = 1500
print(domas.atlyginimas)

domas.atlyginimas = -1500
print(domas.atlyginimas)



