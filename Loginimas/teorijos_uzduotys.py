import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('asmenys.log')
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s',)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

class Asmuo:
    
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde
        logger.info(f"Sukurtas darbuotojas su vardu {self.vardas} ir pavarde: {self.pavarde}")
        print(f"Sukurtas darbuotojas su vardu {self.vardas} ir pavarde: {self.pavarde}")

vardenis = Asmuo("Vardenis", "Vardavicius")
pavardenis = Asmuo("Pavardenis", "Pavardauskas")