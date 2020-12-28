from open_txt import open_txt
import re
from pymarkovchain import MarkovChain
import os


def markov_chain():

    texto_final = open_txt("frases_final_set.txt")
    file_t = "frases_final_set.txt"
    basedir = os.path.abspath(os.path.dirname(__file__))
    file_txt = os.path.join(basedir, file_t)

    texto_split = texto_final.strip('\n').split('.')

    texto_set = set(texto_split)

    print("TXT list: ", texto_set)
    print("LEN list split: ", len(texto_split))
    print("LEN Set: ", len(texto_set))


    return texto_set


markov_chain()
