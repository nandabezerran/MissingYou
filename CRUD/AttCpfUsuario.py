#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
from ValidarCpf import validarCpf
import psycopg2
app = Flask(__name__)

@app.route('/missingYou/api/v1.0/attCpfUsuario/<int:idUser>/<string:cpfUser>', methods=['GET'])
def attCpfUsuario(idUser, cpfUser):
	try:
		conexao = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503

	cur = conexao.cursor()
	sql = 'SELECT cpfUser FROM usuario WHERE idUser =' + str(idUser)
	cur.execute(sql)
	consulta = cur.fetchall()
	if(consulta):
		if(validarCpf(cpfUser) == 'operacao foi realizada com sucesso',200):
			sql = 'UPDATE usuario SET cpfUser = ' + "'" + str(cpfUser) + "'" + " WHERE idUser = " + str(idUser)
			cur.execute(sql)
			conexao.commit()
			return 'operacao foi realizada com sucesso',200
		return 'cpf invalido',412
	return 'id nao foi encontrado',412

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)