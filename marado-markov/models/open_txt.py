import os


def ruta_txt(file_txt=None):

    basedir = os.path.abspath(os.path.dirname(__file__))
    ruta = os.path.join(basedir, file_txt)

    return ruta


def open_txt(file_txt=None):
    frases = ''

    file_txt = ruta_txt(file_txt)

    with open(file_txt, encoding='latin1') as openfile:
        for line in openfile:
            frases += line.replace('...', '') + ' '

    return frases


def open_set(file_txt=None):
    frases_list = []
    file_txt = ruta_txt(file_txt)

    with open(file_txt, encoding='latin1') as openfile:
        for line in openfile:
            frases_list.append(line)

    return frases_list


def write_frase(frase=None):

    file_txt = ruta_txt("seleccionadas.txt")

    with open(file_txt, 'a') as file:
        file.write(frase)


def delete_frase(frase=None):
    file_txt = ruta_txt("frases_final_set.txt")
    with open(file_txt, "r") as f:
        lines = f.readlines()
    with open(file_txt, "w") as f:
        print('FRASE DELTE', frase)
        print('FRASE Type', type(frase))
        frase = frase.strip()
        for line in lines:
            if line.strip("\n") != frase:
                f.write(line)
