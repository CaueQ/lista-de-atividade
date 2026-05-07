from flask import Flask, render_template

app = Flask(_name_)

@app.route('/pizzaria/<sabor>')
def pizzaria(sabor):
    sabores = ["calabresa", "margherita", "frango"]

    if sabor in sabores:
        return render_template("pizza.html", sabor=sabor)
    else:
        return "Sabor não disponível"

app.run(debug=True)