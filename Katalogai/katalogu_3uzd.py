from datetime import datetime
"""
Sukurti programą, kuri:
Kompiuterio darbalaukyje (Desktop) sukurtų katalogą „Naujas Katalogas“
Šiame kataloge sukurtų tekstinį failą, kuriame būtų šiandienos data ir laikas
Atspausdintų šio tekstinio failo sukūrimo datą ir dydį baitais

Patarimai:
Failo sukūrimo datą galima pasiekti per os.stat(„Failas.txt“).st_ctime
"""

import os
from datetime import datetime

os.chdir('C:\\Users\\Debiliukas\\Desktop')
os.mkdir("Naujas_Katalogas")
os.chdir('C:\\Users\\Debiliukas\\Desktop\\Naujas_Katalogas')

with open("Tekstinis_failas.txt", 'w') as file:
    file.write(datetime.now().strftime("%Y-%m-%d, %H:%M:%S"))

print(os.stat('Tekstinis_failas.txt').st_size)
data = os.stat("Tekstinis_failas.txt").st_mtime
print(datetime.fromtimestamp(data))
