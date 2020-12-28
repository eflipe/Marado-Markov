import requests
import re
from bs4 import BeautifulSoup

from random import choice
import sys


class Calle:
    def __init__(self, autor_str: str):
        self.calle_url = f'https://es.wikiquote.org/wiki/{autor_str}'
        self.tag_name = '.mw-parser-output li'
        self.frases = []
        self.palabras = ''

    def load_calle(self) -> str:
        response = requests.get(self.calle_url)
        soup = BeautifulSoup(response.text, "lxml")
        element = soup.select(".mw-parser-output li")
        cont = 0
        frase_total = ''
        pattern = r'\[.*?\]'
        # frase_completa = []
        for frase in element:
            if '↑' in frase.text:
                continue
            cont += 1
            frase_total = frase.text.replace("\"", "")
            frase_total = re.sub(pattern, "", frase_total)
            self.frases.append(frase_total.strip())

        return (' ').join(self.frases)

    def wiki_calle(self) -> str:
        return self.calle_url


autor_frase = Calle('maradona')
autor_frase = autor_frase.load_calle()
