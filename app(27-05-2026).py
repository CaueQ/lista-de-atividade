from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/recebedados', methods=['POST'])
def recebedados():
    nome = request.form.get('nome')
    email = request.form.get('email')
    estado = request.form.get('estado')
    formacao = request.form.get('formacao')
    modalidades = request.form.getlist('modalidades')

    resultado = f"""
    Nome: {nome}<br>
    E-mail: {email}<br>
    Estado: {estado}<br>
    Formação: {formacao}<br>
    Modalidades: {', '.join(modalidades)}
    """
    return resultado


# NOVA ROTA
@app.route('/formregistrar')
def formregistrar():
    return render_template('registrar.html')


# NOVA ROTA
@app.route('/registrar', methods=['POST'])
def registrar():
    usuario = request.form.get('usuario')
    email = request.form.get('email')
    senha = request.form.get('senha')
    confirmar = request.form.get('confirmar')

    if senha == confirmar:
        return "Usuário registrado com sucesso"
    else:
        return "As senhas não conferem"


if __name__ == '__main__':
    app.run(debug=True)