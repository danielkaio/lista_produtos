from flask import Flask, redirect, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+mysqlconnector://daniel:Dani1234!@localhost:3306/compras'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.secret_key = ["jogo"]
db = SQLAlchemy(app)


class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    nome = db.Column(db.String(60))

    def __init__(self, nome):
        self.nome = nome

db.create_all()
 
@app.route("/")
def lista():
    produto = Produto.query.all()
    return render_template("lista.html", produto=produto)


@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/criar", methods=["POST"])
def criar():
    if request.method == "POST":
        nome = request.form['nome']
        produto = Produto(nome)
        db.session.add(produto)
        db.session.commit()
        return redirect(url_for("lista"))


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    produto = Produto.query.get(id)
    if request.method == "POST":
        produto.nome = request.form['nome']
        db.session.commit()
        return redirect(url_for("lista"))
    return render_template("edit.html", produto=produto)


@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    produto = Produto.query.get(id)
    db.session.delete(produto)
    db.session.commit()
    return redirect(url_for("lista"))



if __name__ == "__main__":
    app.run(debug=True, port=5000)
