failiukas = input("Iveskite failo pavadinima: ")

with open(f"{failiukas}.txt", 'a+', encoding='utf8') as x:
    while True:
        eilute = input("\niveskite norima sakini: ")
        if eilute == "":
            print("Failo kurimas baigtas")
            break
        x.write(eilute + '\n')