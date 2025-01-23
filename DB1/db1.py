import sqlite3

conn = sqlite3.connect("duomenu_baze.db")
c = conn.cursor()

with conn:
    c.execute("""
            CREATE TABLE IF NOT EXISTS darbuotojai (
                vardas text,
                pavarde text,
                atlyginimas integer
            )""")

while True:
    print("Iveskite darbuotoja")
    vardas = input("Vardas: ")
    pavarde = input("Pavarde: ")
    atlyginimas = int(input("Atlyginimas: "))
    with conn:    
        c.execute(f"INSERT INTO darbuotojai VALUES ('{vardas}', '{pavarde}', '{atlyginimas}')")
    with conn:
        c.execute("SELECT * FROM darbuotojai")
        print(c.fetchall())
    
   # c.execute("INSERT INTO darbuotojai VALUES ('Domantas', 'Rutkauskas', 1500)")
   # c.execute("INSERT INTO darbuotojai VALUES ('Rimas', 'Radzevicius', 1000)")
    

#nenaudojame:
#conn.commit()
#conn.close()
#, nes pasiraseme "with"