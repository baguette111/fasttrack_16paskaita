def ar_keliamieji2(metai):
    return (metai % 400 == 0) or (metai % 100 != 0 and metai % 4 == 0)

# 1 = True
# 0 = false

print(ar_keliamieji2(2041))