import sys
import random
from random import choice
import re
from pymarkovchain import MarkovChain
import os


def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    chain = {}
    words = corpus.split()

    for i in range(len(words)-2):
        pair = (words[i], words[i+1])
        if (pair in chain):
            chain[pair] += [words[i+2]]
        else:
            chain[pair] = [words[i+2]]

    return chain


def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    # To start, we want a word that starts with a capital letter
    start = 'x'

    while (start[0][0] != start[0][0].title()):
        #print(start)
        #print(start[0][0])
        chains_keys = list(chains.keys())
        start = random.choice(chains_keys)
        start_title = start[0].lower()
        #print("Title", start_title)
        if start_title.endswith(".") or start_title[0].isnumeric():
            print("PUNTO", start[0])
            start = 'x'
            # chains_keys = list(chains.keys())
            # start = random.choice(chains_keys)


        # print(chains.keys())

    line = list(start)

    last = line[-1][-1]
#    while (len(line) < 10):
    while (not line[-1][-1] in ['.', '?']):
        # print("LINE START", line)
        # print("LINE [:]", tuple(line[:]))
        # print("LINE [-2:]", tuple(line[-1:]))
        # print("LINE [-3:]", tuple(line[-2:]))
        # print("LINE [-1:]", tuple(line[-3:]))
        next = chains[tuple(line[-2:])]
        # print("NEXT", next)
        line += [choice(next)]
        # print("LINE", line)
#    	print "line: %r" % line

#    print "line: %r" % line

    return " ".join(line)


def main(texto):

    chain_dict = make_chains(texto)
    markov_1 = make_text(chain_dict)

    list_markov = markov_1
    #print(list_markov)
    flag = True

    while flag:
        if re.search(markov_1, texto):
            markov_1 = make_text(chain_dict)
            flag = True
        else:
            print(markov_1)
            frase_markov = markov_1
            flag = False


    return frase_markov


def markov_chain(texto):

    mc = MarkovChain()
    mc.generateDatabase(texto)
    result = mc.generateString()

    flag = True
    file_t = "frases_final.txt"
    basedir = os.path.abspath(os.path.dirname(__file__))
    file_txt = os.path.join(basedir, file_t)
    print("FILE_T", file_txt)

    while flag:
        result = f'{result}.'
        if re.search(result, texto):
            result = mc.generateString()
            flag = True
            continue
        else:
            with open(file_txt, 'r') as file:
                file = file.readlines()
                #print("READ FILE", file)
                for line in file:
                    print("READ LINE", line)
                    if re.search(result, line):
                        print("REPETIDO!!!!", result)
                        result = ''
                        flag = True
                        break
                    else:
                        result = result

                print("RESULT to file", result)
                with open(file_txt, 'a') as file:
                    file.write(result)
                    file.write("\n")

                frase_markov = result
                flag = False

    return frase_markov
