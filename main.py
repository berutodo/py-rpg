from flask import Flask
from Player import Personagem, batalha
from flask import Flask, render_template
from routes import index
app = Flask(__name__)
app.add_url_rule("/", "index", view_func=index.index)

@app.route("/criar_personagem")
def criar_personagem():
    return render_template("criar_personagem.html")
@app.route("/batalha")
def batalha():
    personagem_principal = Personagem("Herói", 100, 15, 10)
    inimigo = Personagem("Inimigo", 80, 12, 8)

    batalha(personagem_principal, inimigo)

    return render_template('batalha.html', personagem=personagem_principal, oponente=inimigo)
if __name__ == '__main__':
    app.run(debug=True)
