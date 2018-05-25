#!flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/missingYou/api/v1.0/validarEmail/<string:email>', methods=['GET'])
def validarEmail(email):
	try:
		indexAroba = email.index('@')
		if (indexAroba > 0):
			indexPonto = email.index(".")
		if (indexPonto - 1 > indexAroba):
			if (indexPonto + 1 < len(email)):
				return 'operacao foi realizada com sucesso',200
		return 'email invalido',412
	except:
		return 'email invalido',412

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
