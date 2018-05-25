#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
import psycopg2

app = Flask(__name__)

class Usuario(object):
	@app.route('/missingYou/api/v1.0/validarSenha/<string:emailUser>/<string:senhaUser>', methods=['GET'])
	def validarSenha(emailUser, senhaUser):
		try:
			conexao = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
		except:
			return 'nao conectou ao banco',503
		cur = conexao.cursor()
		sql = 'SELECT * FROM usuario WHERE emailUser =' + "'" + str(emailUser) + "'" + 'and senhaUser=' + "'" + str(senhaUser) + "'"
		cur.execute(sql)
		consulta = cur.fetchall()

		if (consulta):
			return 'senha invalida', 412
		else:
			return 'id nao foi encontrado',412

		return 'operacao foi realizada com sucesso',200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)

