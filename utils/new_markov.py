import sys
import random
from random import choice
import re


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
    start = 'z'
    while (start[0][0] != start[0][0].upper()):
        chains_keys = list(chains.keys())
        start = random.choice(chains_keys)

    line = list(start)

    last = line[-1][-1]
    while (not line[-1][-1] in ['.', '?']):
        next = chains[tuple(line[-2:])]
        line += [choice(next)]


    return " ".join(line)


def main():
    args = sys.argv
    filename = 'frases_maradona.txt'

    # Change this to read input_text from a file
    f = open(filename, "r")
    file = f.read()
    chain_dict = make_chains(file)

    markov_1 = make_text(chain_dict)
    list_markov = markov_1
    flag = True

    while flag:
        if re.search(markov_1, file):
            markov_1 = make_text(chain_dict)
            flag = True
        else:
            print(markov_1)
            frase_markov = markov_1
            flag = False

    return frase_markov

if __name__ == "__main__":
    main()
