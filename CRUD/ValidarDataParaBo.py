#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
import psycopg2
from datetime import date
app = Flask(__name__)

@app.route('/missingYou/api/v1.0/validaDataParaBo/<string:dataDes>', methods=['GET'])
def validarDataParaBO(dataDes):
	"""
	return 1 -> nao precisa informar B.O.
	return 2 -> precisa informar B.O. 
	"""
	hoje = date.today()
	desap = dataDes.split("-")
	#formato -> date(ano,mes, dia)
	desap_date = date(int(desap[2]), int(desap[1]), int(desap[0]))
	prazo = hoje - desap_date
	if(prazo.days < 3): # se o prazo for menor que 1 ele nao precisa informar o numero de bo
		return 'nao precisa informar B.O.',200
	else: # se o prazo for maior que 3 ele  precisa informar o numero de bo
		return 'precisa informar B.O.',412


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
