def sakinys_atvirksciai(sakinys):
    sakinio_zodziai = sakinys.split()
    sarasas_atvirkciai = sakinio_zodziai[::-1]
    return " ".join(sarasas_atvirkciai)

print(sakinys_atvirksciai("Jau pavasaris atėjo, kas čia plytų tiek pridėjo?"))
