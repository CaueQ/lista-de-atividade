from flask import flask, render_template
from flask import request

app = flask(_name_)

@app.route('/')
@app.route('/index')
def index():
 return render_template('index.html')

@app.route('/autenticar', methods = ['GET'])
def autenticar():
   usuario = request.args.get('usuario')
   curso = request.args.get('curso')
   cidade = request.args.get('cidade')
   return render_template(
      'autenticar.html',
      usuario=usuario,
      curso=curso,
      cidade=cidade
   )

if _name== 'main_':
    app.run(debug = True)