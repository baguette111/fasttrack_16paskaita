import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('dalyba.log')
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s',)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


def dalyba(a,b):
    
    try:
        return a / b
    
    except ZeroDivisionError:
        logger.exception("Na, nedalinkime is nulio")
    
    else:
        return rezultatas
    
a = 10
b = 0

padalinom = dalyba(a,b)
logger.INFO(f"Dalyba: {a} / {b} = {padalinom}")