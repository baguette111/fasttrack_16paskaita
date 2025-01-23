"""print(sudetis(1,2, 3, 10))
print(saknis(16))
print(sakinio_simboliu_kiekis('aš noriu miego 2'))
print(dalyba(6, 2))"""

import logging
logging.basicConfig(filename = f'Uzduotis_Nr1.log', level=logging.DEBUG, encoding='utf-8', format='%(asctime)s:%(filename)s:%(levelname)s:%(message)s')
# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL

def sudetis(*args):
    return sum(args)

import math
def saknis(n):
    try:
        math.sqrt(n)
    except TypeError:
        logging.exception(n)
        
    else:
        logging.info(f"{n} saknis lygi {math.sqrt(n)}")
        return math.sqrt(n)
        
        # 3 paskaitos tema
        

def sakinio_simboliu_kiekis(sakinys):
    return len(sakinys)

def dalyba(x, y):
    try:
        7 / 0
    except ZeroDivisionError:
        logging.exception(y)
    else:
        logging.info("dalyba is nulio negalima")
    return x / y


n=9

m=10
o=11

x=7
y=0


print(dalyba(x,y))
#logging.warning(f'sudėjom skaičius {m} ir {o} ir gavom {sudetis(m, o)}')

#logging.debug(f'padalinom skaičius {m} ir {o} ir gavom {dalyba(m, o)}')
#logging.info(f'padalinom skaičius {m} ir {o} ir gavom {dalyba(m, o)}')