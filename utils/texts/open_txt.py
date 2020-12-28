import os


def open_txt(file_txt=None):
    basedir = os.path.abspath(os.path.dirname(__file__))
    ruta = os.path.join(basedir, file_txt)
    frases = ''
    file_txt = ruta
    with open(file_txt, encoding='latin1') as openfile:
        for line in openfile:
            frases += line.replace('...', '') + ' '

    return frases
