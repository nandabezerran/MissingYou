#!flask/bin/python
from flask import Flask
from flask import jsonify
from datetime import date
import psycopg2

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

@app.route('/missingYou/api/v1.0/selecionarUsuario/<int:idUser>', methods=['GET'])
def selecionarUsuario(idUser):
	try:
		conexao = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503

	cur = conexao.cursor()
	sql = 'SELECT * FROM usuario WHERE idUser =' + str(idUser)
	cur.execute(sql)
	consulta = cur.fetchall()
	consultaEmDict = [{'idUser': elemento[0], 'nomeUser': elemento[1], 'emailUser': elemento[2],
			   'cpfUser':elemento[3], 'contatoUser': elemento[4], 'senhaUser': elemento[5], 
			   'imagemUser':elemento[6]} for elemento in consulta]
	return jsonify(consultaEmDict)

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


@app.route('/missingYou/api/v1.0/validarCpf/<string:cpf>', methods=['GET'])
def validarCpf(cpf):
	if (len(cpf) == 11):
		# Calcular primeiro digito verificador
		sm = 0
		peso = 10
		for i in range(0, 9):
			sm = sm + (int(cpf[i]) * peso)
			peso = peso - 1
		primeiroDigito = 11 - (sm % 11)
		if ((primeiroDigito == 10) or (primeiroDigito == 11)):
			primeiroDigito = 0

		# calculo do segundo digito vefiricado
		sm = 0
		peso = 11
		for i in range(0, 10):
			sm = sm + (int(cpf[i]) * peso)
			peso = peso - 1

		segundoDigito = 11 - (sm % 11)
		if ((segundoDigito == 10) or (segundoDigito == 11)):
			segundoDigito = 0

		if ((primeiroDigito == int(cpf[9])) and (segundoDigito == int(cpf[10]))):
			return 'operacao foi realizada com sucesso',200
		else:
			return 'cpf invalido',412
	else:
		return 'cpf invalido',412

@app.route('/missingYou/api/v1.0/attImagem/<int:idUser>/<string:imagem>', methods=['GET'])
def attImagem(idUser, imagem):
	
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
		sql = 'UPDATE usuario SET imagem = ' + "'" + imagem + "'" + " WHERE idUser = " + str(idUser)
		cur.execute(sql)
		conexao.commit()
		return 'operacao foi realizada com sucesso',200
	else:
		return 'id nao foi encontrado',412

@app.route('/missingYou/api/v1.0/attNomeUser/<int:idUser>/<string:nomeUser>', methods=['GET'])
def attNomeUser(idUser, nomeUser):
	
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
		sql = 'UPDATE usuario SET nomeUser = ' + "'" + nomeUser + "'" + " WHERE idUser = " + str(idUser)
		cur.execute(sql)
		conexao.commit()
		return 'operacao foi realizada com sucesso',200
	else:
		return 'id nao foi encontrado',412

@app.route('/missingYou/api/v1.0/attContatoUsuario/<int:idUser>/<string:contatoUser>', methods=['GET'])
def UpdateContatoUser(idUser, contatoUser):
	
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
		if(len(contatoUser) == 11):
			sql = 'UPDATE usuario SET contatoUser = ' + "'" + str(contatoUser) + "'" + " WHERE idUser = " + str(idUser)
			cur.execute(sql)
			conexao.commit()
			return 'operacao foi realizada com sucesso',200
		return 'contato invalido',412
	return 'id nao foi encontrado',412

@app.route('/missingYou/api/v1.0/attSenhaUsuario/<int:idUser>/<string:senhaUser>', methods=['GET'])
def attSenhaUsuario(idUser, senhaUser):
	
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

@app.route('/missingYou/api/v1.0/attEmailUsuario/<int:idUser>/<string:emailUser>', methods=['GET'])
def attEmailUsuario(idUser, emailUser):

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
		if(validarEmail(emailUser) == 'operacao foi realizada com sucesso',200):
			sql = 'UPDATE usuario SET emailUser = ' + "'" + emailUser + "'" + " WHERE idUser = " + str(idUser)
			cur.execute(sql)
			conexao.commit()
			return 'operacao foi realizada com sucesso',200
		return 'email invalido',412
	return 'id nao foi encontrado',412

@app.route('/missingYou/api/v1.0/excluirUsuario/<int:idUser>', methods=['GET'])
def excluirUsuario(idUser):
	
	try:
		conexao = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503

	cur = conexao.cursor()
	sql = 'SELECT * FROM usuario WHERE idUser =' + str(idUser)
	cur.execute(sql)
	consulta = cur.fetchall()

	if(consulta):
		cur = conexao.cursor()

		sql1 = "DELETE FROM notificacoes WHERE idusuario = " + str(idUser)
		cur.execute(sql1)
		conexao.commit()
		sql2 = "SELECT idcampanhasperdidos from campanhasperdidos WHERE iduser =" + str(idUser)
		cur.execute(sql2)
		res = cur.fetchall()
		id = None
		for linha in res:
			id = linha[0]
			sql3 = "DELETE FROM notificacoes WHERE idcampanhasperdidos = " + str(id)
			sql4 = "DELETE FROM campanhassalvas WHERE idcampanhasperdidos = " + str(id)
			cur.execute(sql3)
			cur.execute(sql4)
			conexao.commit()

		sql7 = "DELETE FROM campanhassalvas WHERE idusuario = " + str(idUser)
		sql5 = "DELETE FROM campanhasperdidos WHERE idUser = " + str(idUser)
		sql6 = "DELETE FROM usuario WHERE idUser = " + str(idUser)
		cur.execute(sql7)
		cur.execute(sql5)
		cur.execute(sql6)
		conexao.commit()
		return 'operacao foi realizada com sucesso',200

	else:
		return 'id nao foi encontrado',412

@app.route('/missingYou/api/v1.0/cadastrarUsuario/<int:idUser>/<string:senhaUser>/<string:emailUser>/<string:contatoUser>/<string:cpfUser>/<string:imagem>/<string:nomeUser>', methods=['GET'])
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
