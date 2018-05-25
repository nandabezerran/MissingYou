#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
from ValidarEmail import validarEmail

app = Flask(__name__)

@app.route('/missingYou/api/v1.0/validarDados/<string:senhaUser>/<string:emailUser>/<string:contatoUser>', methods=['GET'])
def validarDados(senhaUser, emailUser, contatoUser):

	if(len(contatoUser)!= 11):
		return 'contato invalido',412

	if(len(senhaUser)<= 5):
		return 'senha invalida',412

	if(validarEmail(emailUser) == 'email invalido',412):
		return 'email invalido',412

	return 'operacao realizada com sucesso',200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)