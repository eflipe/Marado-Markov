from open_txt import open_txt
import random
from random import choice
import re
from pymarkovchain import MarkovChain
import os


def markov_chain():
    resultado_frases = []
    texto = open_txt("frases_maradona.txt")
    texto_final = open_txt("frases_final.txt")
    mc = MarkovChain()
    mc.generateDatabase(texto)
    print("TXT", texto, type(texto))

    file_t = "frases_final.txt"
    file_set = "frases_final_set.txt"
    basedir = os.path.abspath(os.path.dirname(__file__))
    file_txt = os.path.join(basedir, file_t)
    file_txt_set = os.path.join(basedir, file_set)

    cont = 0
    for frase in range(22222):
        cont += 1
        result = mc.generateString()
        result = f'{result}.'
        if re.search(result, texto):
            continue
        if re.search(result, texto_final):
            # print("REPETIDO!!!!", result)
            continue
        if result in resultado_frases:
            continue
        print("RESULT to write: ", result)
        resultado_frases.append(result)
        print(cont)

    print("LEN LIST: ", len(resultado_frases))
    with open('frases_final_set.txt', mode='w') as file:
        resultado_set = set(resultado_frases)
        print("LEN SET: ", len(resultado_set))
        file.write('\n'.join(resultado_set))

    return


markov_chain()
