
class Preke:
    def __init__(self, pavadinimas, tipas, kaina, pakuotes_turis, pagaminimo_kastai):
        self.pavadinimas = pavadinimas
        self.tipas = tipas
        self.kaina = kaina
        self.pakuotes_turis = pakuotes_turis
        self.pagaminimo_kastai = pagaminimo_kastai
        self.pelningumas = self.rasti_pelninguma()
        
    def rasti_pelninguma(self):
        return self.kaina - self.pagaminimo_kastai
    
class Produktai:
    def __init__(self):
        self.prekes = []
        
    
    