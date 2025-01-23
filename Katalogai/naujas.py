import pickle

with open("failas.txt", 'w') as failas:
    failas.write("Test")
    failas.seek(0)
    failas.write("BE")