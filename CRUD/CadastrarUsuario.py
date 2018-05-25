#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
from ValidarDados import validarDados
from ValidarCpf   import validarCpf
import psycopg2
app = Flask(__name__)

@app.route('/missingYou/api/v1.0/cadastrarUsuario/<int:idUser>/<string:nomeUser>/<string:senhaUser>/<string:emailUser>/<string:contatoUser>/<string:cpfUser>/<string:imagem>', methods=['GET'])
def cadastrarUsuario(idUser, nomeUser, emailUser, cpfUser, contatoUser, senhaUser,imagem):
	
	try:
		conexao = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503

	cur = conexao.cursor()
	sql = 'SELECT * FROM usuario WHERE idUser =' + str(idUser)
	cur.execute(sql)
	consulta = cur.fetchall()

	cur = conexao.cursor()
	sql2 = 'SELECT * FROM usuario WHERE emailUser = ' + "'" +  str(emailUser) + "'"
	cur.execute(sql2)
	consulta2 = cur.fetchall()

	if(not consulta):
		if(not consulta2):
			if(validarDados(senhaUser, emailUser, contatoUser) == 'operacao realizada com sucesso',200):
				if(validarCpf(cpfUser) == 'operacao realizada com sucesso',200 or cpfUser == 'NULL'):
					sql = "INSERT INTO usuario (idUser, nomeUser, emailUser, cpfUser, contatoUser, senhaUser, imagem ) VALUES" + "(" + str(idUser) + "," + "'"+nomeUser + "'"+ "," + "'"+ emailUser + "'"+"," + "'"+cpfUser + "'"+"," + "'"+  contatoUser + "'" + "," + "'"+ senhaUser + "'"+ "," + "'"+imagem + "'" ")"
					cur.execute(sql)
					conexao.commit()
					return 'operacao foi realizada com sucesso',200
				return 'cpf invalido',412
			return validarDados(senhaUser, emailUser, contatoUser)
		return 'email invalido ou email ja cadastrado no sistema',412
	return 'id nao foi encontrado',412


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
