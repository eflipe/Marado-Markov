from flask import Flask, render_template, url_for, redirect, request
from models.open_txt import open_set, write_frase, delete_frase


app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET', 'POST'])
def marado_markov():
    artist = 'Marado'

    txt_frase = open_set("frases_final_set.txt")
    contador = len(txt_frase)
    msj = ''

    result = txt_frase[0] #To do: cambiar a aleatorio

    if request.method == 'POST':
        frase_marado_markov = request.form['guardar_frase']
        print('FRASE> ', frase_marado_markov)
        write_frase(frase_marado_markov)
        delete_frase(frase_marado_markov)
        txt_frase = open_set("frases_final_set.txt")
        contador = len(txt_frase)

        msj = "Frase guardada"

        return render_template('marado_markov.html', contador=contador,
                                                     artist=artist,
                                                     msj = msj)
    
    delete_frase(result)

    return render_template('marado_markov.html', result=result, artist=artist, contador=contador)


if __name__ == '__main__':
    app.run()
