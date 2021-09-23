
from flask import Flask, redirect, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] ="postgresql://postgres:12345@localhost/jogo"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)

    def __init__(self, nome):
        self.nome = nome


@app.route("/")
def lista():
    all_data = Usuario.query.all()
    return render_template("lista.html", usuario=all_data)


@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/criar", methods=["POST"])
def criar():
    if request.method == "POST":
        nome = request.form['nome']
        usuario = Usuario(nome)
        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for("lista"))


@app.route("/edit")
def edit():

    return render_template("edit.html")


@app.route("/atualizar", methods=["POST"])
def atualizar():
    if request.method == "POST":
        nome = request.form['nome']
        usuario = Usuario(nome)
        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for("lista"))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
