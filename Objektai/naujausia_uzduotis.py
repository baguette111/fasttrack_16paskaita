from operator import attrgetter


class Preke:
    def __init__(self, pavadinimas, tipas, kaina,
                 pakuotes_turis, pagaminimo_kastai):
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
     
     
    def prideti_preke(self, eilute):
        eilute_isskaidyta  = eilute.split(', ')
        pavadinimas = eilute_isskaidyta[0]
        tipas = eilute_isskaidyta[1]
        kaina = float(eilute_isskaidyta[2])
        pakuotes_turis = float(eilute_isskaidyta[3])
        pagaminimo_kastai = float(eilute_isskaidyta[4].rstrip('\n'))
        
        preke = Preke(pavadinimas, tipas, kaina, pakuotes_turis, pagaminimo_kastai)
        
        self.prekes.append(preke)
        
    def nuskaityti_txt_duomenis(self, failo_vieta):
        with open(failo_vieta, 'r')  as f:
            for i, eilute in enumerate(f):
                if i > 0:
                    self.prideti_preke(eilute=eilute)
                    
                    
        
    def rasti_pelningiausia(self):
        pelningiausia_iki_siol_verte = self.prekes[0].pelningumas
        pelningiausia_iki_siol = self.prekes[0].pavadinimas
        for preke in self.prekes:
            if preke.pelningumas > pelningiausia_iki_siol_verte:
                pelningiausia_iki_siol_verte = preke.pelningumas
                pelningiausia_iki_siol = preke.pavadinimas
        return pelningiausia_iki_siol
            

    
    def rasti_pelningiausia_pagal_tipa(self):
        unikalus_tipai = list(set([preke.tipas for preke in self.prekes]))
        
        for tipas in unikalus_tipai:
            prekes = [preke for preke in self.prekes if preke.tipas == tipas]
            pelningiausia = max(prekes, key=attrgetter('pelningumas'))
            print(f'{tipas} pelningiausia: {pelningiausia.pavadinimas}')
               
if __name__ == '__main__':
    elektronikos_produktai = Produktai()
    
    elektronikos_produktai.nuskaityti_txt_duomenis('C:/Users/Debiliukas/Desktop/prekes.txt')

    
    print(f'Pelningiausia preke: {elektronikos_produktai.rasti_pelningiausia()}')
    elektronikos_produktai.rasti_pelningiausia_pagal_tipa()
        