import pickle

with open('failas.txt', 'a', encoding='utf-8') as failas:
    failas.write("Test")
    failas.seek(0)
    failas.write("BE")

a = 10
b = 7
c = 23
with open("abc.pkl", "wb") as pickle_out:
    pickle.dump(a, pickle_out)
    pickle.dump(b, pickle_out)
    pickle.dump(c, pickle_out)

with open("abc.pkl", "rb") as pickle_in:
    nauja_a = pickle.load(pickle_in)
    nauja_b = pickle.load(pickle_in)
    nauja_c = pickle.load(pickle_in)

print(nauja_a)
print(nauja_b)
print(nauja_c)

class Automobilis:
    def __init__(self, marke, modelis):
        self.marke = marke
        self.modelis = modelis

automobiliai = [Automobilis("A", "AB"), Automobilis("A", "AA"), Automobilis("A", "AC")]

with open("automobiliai.pkl", "wb") as file:
    pickle.dump(automobiliai, file)

with open("automobiliai.pkl", "rb") as file:
    automobiliai = pickle.load(file)
    for automobilis in automobiliai:
        print("Marke", automobilis.marke)
        print("Modelis", automobilis.modelis)

