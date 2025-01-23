#import this
#pradžioje paleisti šį kodą, kad gauti the Zen of Python tekstą
from datetime import datetime


zen = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

#įrašome zen of Python tekstą į naują failą
with open("Tekstas.txt",'w') as x:
    x.write(zen)
#pridedame datą paskutinėje eilutėje - su open() naudojame 'a' argumentą
dabartine_data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

with open("Tekstas.txt", 'a') as x:
    x.write(f"\n{dabartine_data}")

#pridedame eilučių numerius.
# Pradžioje nusiskaitome ir susitvarkome tekstą,
# tuomet jį visą su 'w' teisėmis įrašome į Tekstas.txt
naujas=""
skaicius=1
with open("Tekstas.txt", 'r') as x:
   for eilute in x:
        naujas += str(skaicius) + " " + eilute
        skaicius+=1

with open("Tekstas.txt", 'w') as x:
    x.write(naujas)


#Sukurtame faile eilutę "Beautiful is better than ugly." pakeistų į "Gražu yra geriau nei bjauru."
with open("Tekstas.txt", 'r') as x:
    a = x.read()
    a = a.replace("Beautiful is better than ugly.","Gražu yra geriau nei bjauru.")


#Atspausdintų visą failo tekstą atbulai
with open("Tekstas.txt", 'w', encoding='utf-8') as x:
    x.write(a)

with open("Tekstas.txt", 'r', encoding='utf-8') as x:
    b = x.read()
    print(b[::-1])

#Atspausdintų, kiek failo tekste yra žodžių, skaičių, didžiųjų ir mažųjų raidžių
with open("Tekstas.txt", 'r', encoding='utf-8') as x:
    zen_tekstas = x.read()
    print("didziuju raidziu skaicius: ", sum(c.isupper() for c in zen_tekstas))
    print("mazuju raidziu skaicius: ", sum(c.islower() for c in zen_tekstas))
    print("skaiciu skaicius: ", sum(c.isdigit() for c in zen_tekstas))
    print("zodziai: ", len(zen_tekstas.split()))

with open("Tekstas.txt", 'r', encoding='utf-8') as x:
    pradinis = x.read()
    didziosios = pradinis.upper()
    with open("Naujas_failas.txt", 'w', encoding='utf-8') as y:
        y.write(didziosios)


