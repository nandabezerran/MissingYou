#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
from ValidarDados import validarDados
from ValidarCpf   import validarCpf
import psycopg2
app = Flask(__name__)

@app.route('/missingYou/api/v1.0/attSenha/<int:idUser>/<string:senhaUser>', methods=['GET'])
def attSenha(idUser, senhaUser):
	
	try:
		conexao = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503

	cur = conexao.cursor()
	sql = 'SELECT * FROM usuario WHERE idUser =' + str(idUser)
	cur.execute(sql)
	consulta = cur.fetchall()

	if (consulta):
		if(len(senhaUser) >= 6):
			sql = 'UPDATE usuario SET senhauser = ' + str(senhaUser) + " WHERE idUser = " + str(idUser)
			cur.execute(sql)
			conexao.commit()
		return 'operacao foi realizada com sucesso',200
		return 'senha invalida',412
	return 'id nao foi encontrado',412

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
