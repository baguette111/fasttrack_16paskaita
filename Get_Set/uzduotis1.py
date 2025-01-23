class Namas:
    def __init__(self, plotas, verte):
        self.plotas = plotas
        self.__verte = verte
    
    def plotas(self):
        return self.plotas
    
    @property
    def verte(self):
        return self.__verte
    
    @verte.setter
    def verte(self, nauja):
        if nauja < 0:
            print("Verte negali buti neigiama")
        if nauja > 0:
            self.__verte = nauja
            
namas = Namas(100,100)

namas.verte = -200
print(namas.verte)

    
    