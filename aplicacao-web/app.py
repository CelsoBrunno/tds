from flask import Flask, render_template

app = Flask(__name__)


@app.route('/portfolio')
def portifolio():
    return render_template('portfolio.html')



@app.route('/inicio')
def ola():
    lista = ['Fifa 2025','PK Fire Red','Detroid','Vigilant']
    return render_template('lista.html',
                           titulo = 'Epic Games',
                            titulo_2 = 'Lista de jogos',
                            jogos = lista
    )



@app.route('/final')
def final():
    return 'acabou'



app.run(debug=True)
