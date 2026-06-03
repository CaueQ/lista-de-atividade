from flask import Flask, render_template, request

app = Flask(_name_)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    mensagem = ""

    if request.method == 'POST':
        nome = request.form.get('nome')
        if not nome:
            mensagem = "O campo nome é obrigatório!"
        else:
            mensagem = f"Cadastro realizado com sucesso! Bem-vindo, {nome}"
    return render_template('cadastro.html', mensagem=mensagem)

if _name_ == '_main_':
    app.run(debug=True)