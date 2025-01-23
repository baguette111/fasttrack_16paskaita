# surasti pelningiausia preke
# surasti pelningiausia preke pagal prekes tipa
# surasti, kurios pakuotes dydis yra maziausias

def nuskaityti_duomenis(failo_vieta):
    """
    nuskaityti duomenys is txt failo
    :param failo vieta: kelias iki failo
    :return: sarasa su dict tipo eilutemis
    """
    sarasas = []
    with open(failo_vieta, 'r') as f:
        for i, eilute in enumerate(f):
            if i > 0:
                isskaidyta = eilute.split(', ')
                preke = {'prekes_pavadinimas': isskaidyta[0],
                         'prekes_tipas': isskaidyta[1],
                         'kaina': int(isskaidyta[2]),
                         'pakuotes_turis': int(isskaidyta[3]),
                         'pagaminimo_kastai': int(isskaidyta[4].replace('\n', ''))}
                sarasas.append(preke)
    return sarasas

def pelningiausia(duomenys):
    """
    randa pelningiausia preke
    :param dumenys: sarasas su dict elementais(prekem)
    :retur:"""
    didziausias_iki_siol_sutiktas_pelnas = 0
    pelningiausia_preke = ''
    for preke in duomenys:
        prekes_pelnas = preke['kaina'] - preke['pagaminimo_kastai']
        if prekes_pelnas > didziausias_iki_siol_sutiktas_pelnas:
            pelningiausia_preke = preke['prekes_pavadinimas']
            didziausias_iki_siol_sutiktas_pelnas = prekes_pelnas
            
    return pelningiausia_preke

def rasti_pelningiausia_pagal_kategorija(duomenys):
    pelningiausia_pagal_tipa = {}
    
    for preke in duomenys:
        if preke['prekes_tipas'] not in pelningiausia_pagal_tipa:
            pelningiausia_pagal_tipa[preke['prekes_tipas']] = ''
            
    for tipas in pelningiausia_pagal_tipa.keys():
        print(tipas)
    

if __name__ == '__main__':
    duomenys = []
    duomenys = nuskaityti_duomenis(failo_vieta="C:/Users/Debiliukas/Desktop/prekes.txt")
    
    pelningiausia_preke = rasti_pelningiausia(duomenys)
    print(f'Pelningiausia_preke: {pelningiausia_preke}')
    
    rasti_pelningiausia_pagal_tipa(duomenys)