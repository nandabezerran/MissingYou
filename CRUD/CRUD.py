#!flask/bin/python
#coding=utf-8
from flask import Flask
from flask import request
from flask import jsonify
from datetime import date
import collections
import psycopg2

app = Flask(__name__)


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

def validarDados(senhaUser, emailUser, contatoUser):

	if(len(contatoUser)!= 11):
		return 'contato invalido',412

	if(len(senhaUser)<= 5):
		return 'senha invalida',412

	if(validarEmail(emailUser) == 'email invalido',412):
		return 'email invalido',412

	return 'operacao realizada com sucesso',200

@app.route('/missingYou/api/v1.0/validarLogin', methods=['POST'])
def validarLogin():
	try:
		conexao = psycopg2.connect(database="MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
                                   host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
 		return 'nao conectou ao banco', 503

	data = request.get_json()
	cur = conexao.cursor()
	sql = 'SELECT * FROM usuario WHERE emailUser =' + "'" + str(data["emailUser"]) + "'" + 'and senhaUser=' + "'" + str(
        data["senhaUser"]) + "'"
	cur.execute(sql)
	consulta = cur.fetchall()
		
	if (consulta):
		consultaEmDict = [{'idUser': elemento[0], 'nomeUser': elemento[1], 'emailUser': elemento[2],
			   'cpfUser':elemento[3], 'contatoUser': elemento[4], 
			   'imagemUser':elemento[6]} for elemento in consulta]
		return jsonify(consultaEmDict)

	else:
		return 'operacao falhou, email ou senha incorretos', 412

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
			   'cpfUser':elemento[3], 'contatoUser': elemento[4], 'imagemUser':elemento[6]} for elemento in consulta]
	return jsonify(consultaEmDict)


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

@app.route('/missingYou/api/v1.0/attImagem/<int:idUser>/<string:imagem>', methods=['PUT'])
def attImagem(idUser):
	
	try:
		conexao = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503
	data = request.get_json()
	cur = conexao.cursor()
	sql = 'SELECT * FROM usuario WHERE idUser =' + str(idUser)
	cur.execute(sql)
	consulta = cur.fetchall()

	if (consulta):
		sql = 'UPDATE usuario SET imagem = ' + "'" + data["imagem"] + "'" + " WHERE idUser = " + str(idUser)
		cur.execute(sql)
		conexao.commit()
		return 'operacao foi realizada com sucesso',200
	else:
		return 'id nao foi encontrado',412

@app.route('/missingYou/api/v1.0/attNomeUser/<int:idUser>', methods=['PUT'])
def attNomeUser(idUser):
	
	try:
		conexao = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503
	data = request.get_json()
	cur = conexao.cursor()
	sql = 'SELECT * FROM usuario WHERE idUser =' + str(idUser)
	cur.execute(sql)
	consulta = cur.fetchall()

	if (consulta):
		sql = 'UPDATE usuario SET nomeUser = ' + "'" + data["nomeUser"] + "'" + " WHERE idUser = " + str(idUser)
		cur.execute(sql)
		conexao.commit()
		return 'operacao foi realizada com sucesso',200
	else:
		return 'id nao foi encontrado',412

@app.route('/missingYou/api/v1.0/attContatoUsuario/<int:idUser>', methods=['PUT'])
def UpdateContatoUser(idUser):
	
	try:
		conexao = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503

	data = request.get_json()
	cur = conexao.cursor()
	sql = 'SELECT * FROM usuario WHERE idUser =' + str(idUser)
	cur.execute(sql)
	consulta = cur.fetchall()

	if (consulta):
		if(len(contatoUser) == 11):
			sql = 'UPDATE usuario SET contatoUser = ' + "'" + str(data["contatoUser"]) + "'" + " WHERE idUser = " + str(idUser)
			cur.execute(sql)
			conexao.commit()
			return 'operacao foi realizada com sucesso',200
		return 'contato invalido',412
	return 'id nao foi encontrado',412

@app.route('/missingYou/api/v1.0/attSenhaUsuario/<int:idUser>', methods=['PUT'])
def attSenhaUsuario(idUser):
	
	try:
		conexao = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503
	data = request.get_json()
	cur = conexao.cursor()
	sql = 'SELECT * FROM usuario WHERE idUser =' + str(idUser)
	cur.execute(sql)
	consulta = cur.fetchall()

	if (consulta):
		if(len(senhaUser) >= 6):
			sql = 'UPDATE usuario SET senhauser = ' + str(data["senhaUser"]) + " WHERE idUser = " + str(idUser)
			cur.execute(sql)
			conexao.commit()
		return 'operacao foi realizada com sucesso',200
		return 'senha invalida',412
	return 'id nao foi encontrado',412

@app.route('/missingYou/api/v1.0/attCpfUsuario/<int:idUser>', methods=['PUT'])
def attCpfUsuario(idUser):
	try:
		conexao = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503
	data = request.get_json()
	cur = conexao.cursor()
	sql = 'SELECT cpfUser FROM usuario WHERE idUser =' + str(idUser)
	cur.execute(sql)
	consulta = cur.fetchall()
	if(consulta):
		if(validarCpf(cpfUser) == 'operacao foi realizada com sucesso',200):
			sql = 'UPDATE usuario SET cpfUser = ' + "'" + str(data["cpfUser"]) + "'" + " WHERE idUser = " + str(idUser)
			cur.execute(sql)
			conexao.commit()
			return 'operacao foi realizada com sucesso',200
		return 'cpf invalido',412
	return 'id nao foi encontrado',412

@app.route('/missingYou/api/v1.0/attEmailUsuario/<int:idUser>', methods=['PUT'])
def attEmailUsuario(idUser):

	try:
		conexao = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503
	data = request.get_json()
	cur = conexao.cursor()
	sql = 'SELECT * FROM usuario WHERE idUser =' + str(idUser)
	cur.execute(sql)
	consulta = cur.fetchall()

	if (consulta):
		if(validarEmail(emailUser) == 'operacao foi realizada com sucesso',200):
			sql = 'UPDATE usuario SET emailUser = ' + "'" + data["emailUser"] + "'" + " WHERE idUser = " + str(idUser)
			cur.execute(sql)
			conexao.commit()
			return 'operacao foi realizada com sucesso',200
		return 'email invalido',412
	return 'id nao foi encontrado',412

@app.route('/missingYou/api/v1.0/excluirUsuario/<int:idUser>', methods=['DELETE'])
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

@app.route('/missingYou/api/v1.0/cadastrarUsuario', methods=['POST'])
def cadastrarUsuario():
	
	try:
		conexao = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503
	data = request.get_json()
	#data = data.load()

	cur = conexao.cursor()
	sql = 'SELECT * FROM usuario WHERE idUser =' + str(data["idUser"])
	cur.execute(sql)
	consulta = cur.fetchall()

	cur = conexao.cursor()
	sql2 = 'SELECT * FROM usuario WHERE emailUser = ' + "'" +  str(data["emailUser"]) + "'"
	cur.execute(sql2)
	consulta2 = cur.fetchall()
	

	if(not consulta):
		if(not consulta2):
			if(validarDados(data["senhaUser"],["emailUser"],["contatoUser"]) == 'operacao realizada com sucesso',200):
				if(validarCpf(data["cpfUser"]) == 'operacao realizada com sucesso',200 or cpfUser == 'NULL'):
					sql = "INSERT INTO usuario (idUser,nomeUser, emailUser,cpfUser,contatoUser,senhaUser, imagem ) VALUES" + "(" + str(data["idUser"]) + "," + "'"+data["nomeUser"] + "'"+ "," + "'"+ data["emailUser"] + "'"+"," + "'"+data["cpfUser"] + "'"+"," + "'"+  data["contatoUser"] + "'" + "," + "'"+ data["senhaUser"] + "'"+ "," + "'"+data["imagemUser"] + "'" ")"
					cur.execute(sql)
					conexao.commit()
					return 'operacao foi realizada com sucesso',200
				return 'cpf invalido',412
			return validarDados(data["senhaUser"], data["emailUser"], data["contatoUser"])
		return 'email invalido ou email ja cadastrado no sistema',412
	return 'id nao foi encontrado',412

@app.route('/missingYou/api/v1.0/cadastrarCampanha', methods=['POST'])
def cadastrarCampanha():
	try:
		banco = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503

	data = request.get_json()
	cur = banco.cursor()
	sql = "SELECT * FROM usuario WHERE usuario.iduser = " + str(data["idUser"])
	resultado = None
	cur.execute(sql)
	resultado = cur.fetchall();
	cur.close()
	data_camp = date.today()
	if(resultado):
		#verificando se a campanha ja esta cadastrada
		cur = banco.cursor()
		sql = "SELECT * FROM campanhasperdidos WHERE campanhasperdidos.idcampanhasperdidos = " + str(data["idCampanhas"])
		resultado = None
		cur.execute(sql)
		resultado = cur.fetchall();
		cur.close()
            
		if(resultado):
			return 'campanha ja cadastrada',412
		else:
			if(validarDataParaBO(data["dataDesaparecimento"]) == 'nao precisa informar B.O.',200):
				cur = banco.cursor()                                                                                                                                                     
				sql = "INSERT INTO campanhasperdidos(idcampanhasperdidos, iduser, statuscampanhasperdidos, datanascimento, nomedesaparecido, idadedesaparecido, sexodesaparecido, olhosdesaparecido, racadesaparecido, cabelodesaparecido, datadesaparecimento, datacampanha, bo, descricao) values (" + str(data["idCampanhas"]) + ", " + str(data["idUser"]) + ", " + "'"+str(data["statusCampanhas"])+"'"+ ", " + "'"+str(data["dataNasc"])+"'"+ ", " + "'"+str(data["nomeDesaparecido"])+"'" + ", " + "'"+str(data["idadeDesaparecido"])+"'"+ ", "+ "'"+str(data["sexoDesaparecido"])+"'" + ", " + "'"+str(data["olhosDesaparecido"])+"'"+ ", "+ "'"+str(data["racaDesaparecido"])+"'" + ", " + "'"+str(data["cabeloDesaparecido"])+"'" + ", " + "'"+str(data["dataDesaparecimento"])+"'" + ", " + "'"+str(data_camp)+"'" + ", " + "'"+str(data["bo"])+"'"+  ", " + "'"+str(data["descricao"])+"'" + ")"
				cur.execute(sql)
				banco.commit()
				cur.close()
				return 'operacao foi realizada com sucesso',200

			else:
				return 'precisa informar B.O.',412
	else:
		return 'nao ha usuario com essa id',412

@app.route('/missingYou/api/v1.0/selecionarCampanhasBoNull/', methods=['GET'])
def selecionarCampanhasBoNull():
	try:
		banco = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503

	sql = "SELECT idcampanhasperdidos FROM campanhasperdidos WHERE campanhasperdidos.bo = 'null' "
	resultado = None
	cur = banco.cursor()
	cur.execute(sql)
	resultado = cur.fetchall();
	resultList = []
	if(resultado):
		for elemento in resultado:
			consultaEmDict = collections.OrderedDict()
			consultaEmDict = {'idCampanhas': elemento[0], 'idUser': elemento[1], 'statusCampanhas': elemento[2],
			   'dataNasc':elemento[3], 'nomeDesaparecido': elemento[4], 'idadeDesaparecido': elemento[5], 
			   'sexoDesaparecido':elemento[6],'olhosDesaparecido':elemento[7], 'racaDesaparecido':elemento[8],
			   'cabeloDesaparecido':elemento[9], 'dataDesaparecimento':elemento[10], 'dataCampanha':elemento[11],
			   'bo':elemento[12], 'descricao':elemento[13]} 
			resultList.append(consultaEmDict)

		return jsonify(resultList)
	else: 
		return 'id_campanha nao foi encontrado', 412

@app.route('/missingYou/api/v1.0/selecionarCampanhasId/<int:id_campanha>', methods=['GET'])
def selecionarCampanhaId(id_campanha): #seleciona campanha daquele id
	try:
		banco = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503

	sql = "SELECT * FROM campanhasperdidos " + " WHERE campanhasperdidos.idcampanhasperdidos = " + str(id_campanha)
	resultado = None
	cur = banco.cursor()
	cur.execute(sql)
	resultado = cur.fetchall();
	resultList = []
	if(resultado):
		for elemento in resultado:
			consultaCollec = collections.OrderedDict()
			consultaCollec = {'idCampanhas': elemento[0], 'idUser': elemento[1], 'statusCampanhas': elemento[2],
			   'dataNasc':elemento[3], 'nomeDesaparecido': elemento[4], 'idadeDesaparecido': elemento[5], 
			   'sexoDesaparecido':elemento[6],'olhosDesaparecido':elemento[7], 'racaDesaparecido':elemento[8],
			   'cabeloDesaparecido':elemento[9], 'dataDesaparecimento':elemento[10], 'dataCampanha':elemento[11],
			   'bo':elemento[12], 'descricao':elemento[13]}
			resultList.append(consultaCollec)
		return jsonify(resultList)

	else:
		return'id_campanha nao foi encontrado', 412

@app.route('/missingYou/api/v1.0/selecionarCampanhasUser/<int:id_user>', methods=['GET'])
def selecionarCampanhaUser(id_user): #seleciona as campanhas cadastradas por um usuario
	try:
		banco = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503

	sql = "SELECT * FROM campanhasperdidos" + " WHERE campanhasperdidos.iduser = " + str(id_user)
	cur = banco.cursor()
	cur.execute(sql)
	resultado = cur.fetchall();
	resultList = []
	cur.close()
	if(resultado):
		for elemento in resultado:
			consultaCollec = collections.OrderedDict()
			consultaCollec = {'idCampanhas': elemento[0], 'idUser': elemento[1], 'statusCampanhas': elemento[2],
			   'dataNasc':elemento[3], 'nomeDesaparecido': elemento[4], 'idadeDesaparecido': elemento[5], 
			   'sexoDesaparecido':elemento[6],'olhosDesaparecido':elemento[7], 'racaDesaparecido':elemento[8],
			   'cabeloDesaparecido':elemento[9], 'dataDesaparecimento':elemento[10], 'dataCampanha':elemento[11],
			   'bo':elemento[12], 'descricao':elemento[13]}
			resultList.append(consultaCollec)
		return jsonify(resultList)

	else:
		return 'id_usuario nao encontrado',412

@app.route('/missingYou/api/v1.0/alterarStatusCampanha/<int:id_campanha>', methods=['PUT'])
def alterarStatus(id_campanha): #altera o status de uma campanha
	try:
		banco = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503
	data = request.get_json()
	sql = "SELECT * FROM campanhasperdidos " + " WHERE campanhasperdidos.idcampanhasperdidos = " + str(id_campanha) 
	resultado = None
	cur = banco.cursor()
	cur.execute(sql)
	resultado = cur.fetchall();
        
	if(resultado):
		sql = "UPDATE campanhasperdidos" + " SET statuscampanhasperdidos = " + "'"+str(dat["status"])+"'" + " WHERE idcampanhasperdidos = " + str(id_campanha)
		cur = banco.cursor()
		cur.execute(sql)
		banco.commit()
		cur.close();
		return 'operacao realizada com sucessa', 200
	else:
		return 'id_campanha nao foi encontrada', 412

@app.route('/missingYou/api/v1.0/alterarNomeDesaparecido/<int:id_campanha>', methods=['PUT'])
def alterarNome(id_campanha):
	try:
		banco = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503
	data = request.get_json()
	sql = "SELECT * FROM campanhasperdidos " + " WHERE campanhasperdidos.idcampanhasperdidos = " + str(id_campanha)
	resultado = None
	cur = banco.cursor()
	cur.execute(sql)
	resultado = cur.fetchall();
        
	if(resultado):
		sql = "UPDATE campanhasperdidos" + " SET nomedesaparecido = " + "'"+str(data["nome"])+"'" + " WHERE idcampanhasperdidos = " + str(id_campanha)
		cur = banco.cursor()
		cur.execute(sql)
		banco.commit()
		cur.close();
		return 'operacao realizada com sucessa', 200
	else:
		return 'id_campanha nao foi encontrada', 412

@app.route('/missingYou/api/v1.0/alterarCabeloDesaparecido/<int:id_campanha>', methods=['PUT'])
def alterarCabelo(id_campanha):
	try:
		banco = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503
	data = request.get_json()
	sql = "SELECT * FROM campanhasperdidos " + " WHERE campanhasperdidos.idcampanhasperdidos = " + str(id_campanha)
	resultado = None
	cur = banco.cursor()
	cur.execute(sql)
	resultado = cur.fetchall();
        
	if(resultado):
		sql = "UPDATE campanhasperdidos" + " SET cabelodesaparecido = " + "'"+str(data["cabelo"])+"'" + " WHERE idcampanhasperdidos = " + str(id_campanha)
		cur = banco.cursor()
		cur.execute(sql)
		banco.commit()
		cur.close();
		return 'operacao realizada com sucessa', 200
	else:
		return 'id_campanha nao foi encontrada', 412

@app.route('/missingYou/api/v1.0/alterarRacaDesaparecido/<int:id_campanha>', methods=['PUT'])
def alterarRaca(id_campanha):
	try:
		banco = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503
	
	data = request.get_json()
	sql = "SELECT * FROM campanhasperdidos " + " WHERE campanhasperdidos.idcampanhasperdidos = " + str(id_campanha) 
	resultado = None
	cur = banco.cursor()
	cur.execute(sql)
	resultado = cur.fetchall();
        
	if(resultado):
		sql = "UPDATE campanhasperdidos" + " SET racadesaparecido = " + "'"+str(data["raca"])+"'" + " WHERE idcampanhasperdidos = " + str(id_campanha)
		cur = banco.cursor()
		cur.execute(sql)
		banco.commit()
		cur.close();
		return 'operacao realizada com sucessa', 200
	else:
		return 'id_campanha nao foi encontrada', 412

@app.route('/missingYou/api/v1.0/alterarIdadeDesaparecido/<int:id_campanha>', methods=['PUT'])
def alterarIdade(id_campanha):
	try:
		banco = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503
	data = request.get_json()
	sql = "SELECT * FROM campanhasperdidos " + " WHERE campanhasperdidos.idcampanhasperdidos = " + str(id_campanha) 
	resultado = None
	cur = banco.cursor()
	cur.execute(sql)
	resultado = cur.fetchall();
        
	if(resultado):
		sql = "UPDATE campanhasperdidos" + " SET idadedesaparecido = " + "'"+str(data["idade"])+"'" + " WHERE idcampanhasperdidos = " + str(id_campanha)
		cur = banco.cursor()
		cur.execute(sql)
		banco.commit()
		cur.close();
		return 'operacao realizada com sucessa', 200
	else:
		return 'id_campanha nao foi encontrada', 412

@app.route('/missingYou/api/v1.0/alterarSexoDesaparecido/<int:id_campanha>', methods=['PUT'])
def alterarSexo(id_campanha):
	try:
		banco = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503

	data = request.get_json()
	sql = "SELECT * FROM campanhasperdidos " + " WHERE campanhasperdidos.idcampanhasperdidos = " + str(id_campanha) 
	resultado = None
	cur = banco.cursor()
	cur.execute(sql)
	resultado = cur.fetchall();
        
	if(resultado):
		sql = "UPDATE campanhasperdidos" + " SET sexodesaparecido = " + "'"+str(data["sexo"])+"'" + " WHERE idcampanhasperdidos = " + str(id_campanha)
		cur = banco.cursor()
		cur.execute(sql)
		banco.commit()
		cur.close();
		return 'operacao realizada com sucessa', 200
	else:
		return 'id_campanha nao foi encontrada', 412

@app.route('/missingYou/api/v1.0/excluirCampanha/<int:id_campanha>', methods=['DELETE'])
def excluirCampanha(id_campanha): #exclui a campanha
	try:
		banco = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503

	sql = "SELECT * FROM campanhasperdidos " + " WHERE campanhasperdidos.idcampanhasperdidos = " + str(id_campanha) 
	resultado = None
	cur = banco.cursor()
	cur.execute(sql)
	resultado = cur.fetchall();
        
	if(resultado):
		sql = "DELETE FROM campanhasperdidos WHERE campanhasperdidos.idcampanhasperdidos = " + str(id_campanha)
		cur = banco.cursor()
		cur.execute(sql)
		banco.commit()
		cur.close()
		return 'operacao realizada com sucessa', 200

	else:
		return 'id_campanha nao foi encontrada', 412

@app.route('/missingYou/api/v1.0/alterarBO/<int:id_campanha>', methods=['PUT'])
def alterarBO(id_campanha): #altera o B.O. de uma campanha
	try:
		banco = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503

	data = request.get_json()
	sql = "SELECT * FROM campanhasperdidos " + " WHERE campanhasperdidos.bo = 'null' and campanhasperdidos.idcampanhasperdidos = " + str(id_campanha) 
	resultado = None
	cur = banco.cursor()
	cur.execute(sql)
	resultado = cur.fetchall();
	if(resultado):
		sql = "UPDATE campanhasperdidos" + " SET bo = " + "'"+str(data["bo"])+"'" + " WHERE idcampanhasperdidos = " + str(id_campanha)
		cur = banco.cursor()
		cur.execute(sql)
		banco.commit()
		cur.close();
		return 'operacao realizada com sucessa', 200
	else:
		return 'id_campanha nao foi encontrada', 412

@app.route('/missingYou/api/v1.0/alterarDescricao/<int:id_campanha>', methods=['PUT'])
def alterarDescricao(id_campanha):
	try:
		banco = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503
	data = request.get_json()
	sql = "SELECT * FROM campanhasperdidos " + " WHERE campanhasperdidos.idcampanhasperdidos = " + str(id_campanha)
	resultado = None
	cur = banco.cursor()
	cur.execute(sql)
	resultado = cur.fetchall();
        
	if(resultado):
		sql = "UPDATE campanhasperdidos" + " SET descricao = " + "'"+str(data["descricao"])+"'" + "WHERE idcampanhasperdidos = " + str(id_campanha)
		cur = banco.cursor()
		cur.execute(sql)
		banco.commit()
		cur.close();
		return 'operacao realizada com sucessa', 200
	else:
		return 'id_campanha nao foi encontrada', 412

@app.route('/missingYou/api/v1.0/inserirLocalCampanha', methods=['POST'])
def inserirLocalCampanha():
	try:
		banco = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503

	# Checando se campanha existe
	data = request.get_json()
	sql = "SELECT * FROM campanhasperdidos " + " WHERE campanhasperdidos.idcampanhasperdidos = " + str(data["id_campanha"])
	resultado = None
	cur = banco.cursor()
	cur.execute(sql)
	resultado = cur.fetchall();

	if(resultado):
		cur = banco.cursor()
		sql = "INSERT INTO attlocalizacaocampanhasperdidos(idcampanhasperdidos, latitude, longitude, attdata, attbairro) VALUES("+ str(data["id_campanha"]) + ", "  + str(data["latitude"]) + ", " + str(data["longitude"]) + ", " +"'"+str(data["attdata"])+"'"+ ", " + "'"+str(data["attbairro"])+"'" + ")"
		cur.execute(sql)
		banco.commit()
		cur.close()
		return 'operacao realizada com sucesso', 200
	else:
		return 'id_campanha nao foi encontrado', 412

@app.route('/missingYou/api/v1.0/selecionarCampanhaIdLocalizacao/<int:id_campanha>', methods=['GET'])
def selecionarCampanhaIdLocalizacao(id_campanha): #seleciona a campanha daquele id
	try:
		banco = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503

	sql = "SELECT * FROM attlocalizacaocampanhasperdidos " + " WHERE attlocalizacaocampanhasperdidos.idcampanhasperdidos = " + str(id_campanha)
	resultado = None
	cur = banco.cursor()
	cur.execute(sql)
	resultado = cur.fetchall();
	cur.close()
	resultList = []
	if(resultado):
		for elemento in resultado:
			consultaCollec = collections.OrderedDict()
			consultaCollec = {'idCampanhas': elemento[0], 'longitude': elemento[1], 'latitude': elemento[2],
			   'data':elemento[3], 'bairro': elemento[4]}
			resultList.append(consultaCollec)
		return jsonify(resultList)
	else:
		return 'id_campanha nao foi encontrado', 412

@app.route('/missingYou/api/v1.0/selecionarCampanhaBairro/<string:bairro>', methods=['GET'])
def selecionarCampanhaBairro(bairro): #seleciona as campanhas por bairro
	try:
		banco = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503

	sql = "SELECT * FROM campanhasperdidos WHERE campanhasperdidos.idcampanhasperdidos IN (SELECT idcampanhasperdidos FROM attlocalizacaocampanhasperdidos  WHERE attlocalizacaocampanhasperdidos.attbairro = " + "'"+str(bairro)+"'" + ")" 
	resultado = None
	cur = banco.cursor()
	cur.execute(sql)
	resultado = cur.fetchall();
	cur.close()
	resultList = []
	if(resultado):
		for elemento in resultado:
			consultaCollec = collections.OrderedDict()
			consultaCollec = {'idCampanhas': elemento[0], 'idUser': elemento[1], 'statusCampanhas': elemento[2],
			   'dataNasc':elemento[3], 'nomeDesaparecido': elemento[4], 'idadeDesaparecido': elemento[5], 
			   'sexoDesaparecido':elemento[6],'olhosDesaparecido':elemento[7], 'racaDesaparecido':elemento[8],
			   'cabeloDesaparecido':elemento[9], 'dataDesaparecimento':elemento[10], 'dataCampanha':elemento[11],
			   'bo':elemento[12], 'descricao':elemento[13]}
			resultList.append(consultaCollec)
		return jsonify(resultList)
	else:
		return 'id_campanha nao foi encontrado', 412

@app.route('/missingYou/api/v1.0/alterarLocal/<int:id_campanha>', methods=['PUT'])
def alterarLocal(id_campanha):
	try:
		banco = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503

	# VERIFICANDO SE A CAMPANHA EXISTE
	data = request.get_json()
	sql = "SELECT * FROM attlocalizacaocampanhasperdidos " + " WHERE attlocalizacaocampanhasperdidos.idcampanhasperdidos = " + str(id_campanha)
	resultado = None
	cur = banco.cursor()
	cur.execute(sql)
	resultado = cur.fetchall();
	cur.close()

	if(resultado):
		sql = "UPDATE attlocalizacaocampanhasperdidos" + " SET latitude = " + str(data["lat"]) + ", longitude = " + str(data["lon"]) + ", attdata = " + "'"+str(data["data"])+"'" + ", attbairro = " + "'"+str(data["bairro"])+"'" + " WHERE idcampanhasperdidos = " + "'"+str(id_campanha)+"'"
		cur = self.banco.cursor()
		cur.execute(sql)
		banco.commit()
		cur.close()
		return 'operacao realizada com sucesso', 200
	else:
		return 'id_campanha nao foi encontrado', 412

@app.route('/missingYou/api/v1.0/excluirCampanhaLocalizacao/<int:id_campanha>', methods=['DELETE'])
def excluirCampanhaLocalizacao(id_campanha):
        # VERIFICANDO SE A CAMPANHA EXISTE
	try:
		banco = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503

	sql = "SELECT * FROM attlocalizacaocampanhasperdidos " + " WHERE attlocalizacaocampanhasperdidos.idcampanhasperdidos = " + str(id_campanha)
	resultado = None
	cur = banco.cursor()
	cur.execute(sql)
	resultado = cur.fetchall();
	cur.close()
	if(resultado): 
		sql = "DELETE FROM attlocalizacaocampanhasperdidos WHERE attlocalizacaocampanhasperdidos.idcampanhasperdidos = " + str(id_campanha)
		cur = banco.cursor()
		cur.execute(sql)
		banco.commit()
		cur.close()
		return 'operacao realizada com sucesso', 200
	else:
		return 'id_campanha nao foi encontrado', 412

@app.route('/missingYou/api/v1.0/inserirCampanhaSalvas', methods=['POST'])
def inserirCampanhaSalvas(): # ver se precisa tratar o caso da campanha ja estar cadastrada
        #   VERIFICANDO SE O USUARIO EXISTE
	try:
		banco = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503
	data = request.get_json()
	cur = banco.cursor()
	sql = "SELECT * FROM usuario WHERE usuario.iduser = " + str(data["id_user"])
	resultado = None
	cur.execute(sql)
	resultado = cur.fetchall();
	cur.close()

	if(resultado):
		#   VERIFICANDO SE CAMPANHA EXISTE
		cur = banco.cursor()
		sql = "SELECT * FROM campanhasperdidos WHERE campanhasperdidos.idcampanhasperdidos = " + str(data["id_campanha"])
		resultado = None
		cur.execute(sql)
		resultado = cur.fetchall();
		cur.close()
            
		if(resultado):
			cur = banco.cursor()
			sql = "SELECT * FROM campanhassalvas WHERE campanhassalvas.idusuario = " + str(data["id_user"]) + "and campanhassalvas.idcampanhasperdidos =  " + str(data["id_campanha"])
			resultado = None
			cur.execute(sql)
			resultado = cur.fetchall();
			cur.close()
			if(resultado):
				return 'campanha ja salva', 412
			else:
				cur = banco.cursor()
				sql = "INSERT INTO campanhassalvas(idusuario, idcampanhasperdidos) VALUES("+ str(data["id_user"])  + ", " + str(data["id_campanha"])  + ")"
				cur.execute(sql)
				banco.commit()
				cur.close()
				return 'operacao realizada com sucesso', 200
		else:
 			return 'id_campanha nao foi encontrado', 412
	else:
		return 'id_usuario nao foi encontrado', 412


@app.route('/missingYou/api/v1.0/selecionarCampanhaIdCampanha/<int:id_campanha>', methods=['GET'])
def selecionarCampanhaIdCampanha(id_campanha): #seleciona campanha daquele id
	try:
		banco = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503

	sql = "SELECT * FROM campanhassalvas " + " WHERE campanhassalvas.idcampanhasperdidos = " + str(id_campanha)
	resultado = None
	cur = banco.cursor()
	cur.execute(sql)
	resultado = cur.fetchall();
	resultList = []
	if(resultado):
		for elemento in resultado:
			consultaEmDict = collections.OrderedDict()
			consultaEmDict = {'idUsuario': elemento[0]} 
			resultList.append(consultaEmDict)

		return jsonify(resultList)

	else:
		return 'id_campanha nao foi encontrado', 412

@app.route('/missingYou/api/v1.0/selecionarCampanhaIdUser/<int:id_user>', methods=['GET'])
def selecionarCampanhaIdUser(id_user): #seleciona as campanhas cadastradas por um usuario
	try:
		banco = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503

	sql = "SELECT * FROM campanhassalvas" + " WHERE campanhassalvas.idusuario = " + str(id_user)
	cur = banco.cursor()
	cur.execute(sql)
	resultado = cur.fetchall();
	resultList = []
	cur.close()
	if(resultado):
		for elemento in resultado:
			consultaEmDict = collections.OrderedDict()
			consultaEmDict = {'idCampanha': elemento[1]} 
			resultList.append(consultaEmDict)

		return jsonify(resultList)

	else:
		return 'id_campanha nao foi encontrado', 412

@app.route('/missingYou/api/v1.0/excluirCampanhasDoUsuario/<int:id_user>', methods=['DELETE'])
def excluirCampanhasDoUsuario(id_user):  # exclui todas as campanhas cadastradas por aquele usuario
	try:
		banco = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503

	sql = "SELECT * FROM campanhassalvas" + " WHERE campanhassalvas.idusuario = " + str(id_user)
	cur = banco.cursor()
	cur.execute(sql)
	resultado = cur.fetchall();
	cur.close()
	if(resultado):
		id = None
		for linha in resultado:
			id = linha[0]
			sql = "DELETE FROM campanhassalvas WHERE campanhassalvas.idcampanhasperdidos = " + str(id) 
			cur = banco.cursor()
			cur.execute(sql)
			banco.commit()
			cur.close();
			return 'operacao realizada com sucesso',200
	else:
		return 'id_campanha nao foi encontrado', 412

@app.route('/missingYou/api/v1.0/excluirCampanhaSalva/<int:id_campanha>', methods=['DELETE'])
def excluirCampanhaSalva(id_campanha): #exclui a campanha
	try:
		banco = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503

	sql = "SELECT * FROM campanhassalvas " + " WHERE campanhassalvas.idcampanhasperdidos = " + str(id_campanha)
	resultado = None
	cur = banco.cursor()
	cur.execute(sql)
	resultado = cur.fetchall();
	if(resultado):
		sql = "DELETE FROM campanhassalvas WHERE campanhassalvas.idcampanhasperdidos = " + str(id_campanha) 
		cur = banco.cursor()
		cur.execute(sql)
		banco.commit()
		cur.close();
		return 'operacao realizada com sucesso',200
	else:
		return 'id_campanha nao foi encontrado', 412

@app.route('/missingYou/api/v1.0/inserirImgCampanha', methods=['POST'])	
def inserirImgCampanha(): # ver se precisa tratar o caso da campanha ja estar cadastrada
	try:
		conexao = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503

	#   VERIFICANDO SE CAMPANHA EXISTE
	data = request.get_json()
	cur = banco.cursor()
	sql = "SELECT * FROM campanhasperdidos WHERE campanhasperdidos.idcampanhasperdidos = " + str(data["id_campanha"])
	resultado = None
	cur.execute(sql)
	resultado = cur.fetchall();
	cur.close()
            
	if(resultado):
		cur = banco.cursor()
		sql = "SELECT * FROM imagens WHERE imagens.imagem = " + "'"+str(data["imagem"])+"'"
		resultado = None
		cur.execute(sql)
		resultado = cur.fetchall();
		cur.close()
		if(resultado):
			cur = self.banco.cursor()
			sql = "SELECT * FROM CampanhasPerdidos_Imagens WHERE CampanhasPerdidos_Imagens.imagem = " + "'"+str(data["imagem"])+"'" + "and CampanhasPerdidos_Imagens.idcampanhasperdidos = " + str(data["id_campanha"])
			resultado = None
			cur.execute(sql)
			resultado = cur.fetchall();
			cur.close()
			if(resultado):
				return 'campanha ja cadastrada', 412
			else:
				cur = banco.cursor()
				sql = "INSERT INTO CampanhasPerdidos_Imagens(idCampanhasPerdidos, imagem) VALUES("+ str(data["id_campanha"])  + ", " + "'"+str(data["imagem"])+"'"  + ")"
				cur.execute(sql)
				banco.commit()
				cur.close()
				return 'operacao realizada com sucesso', 200
		else:
			return 'id_campanha nao foi encontrado', 412
	else:
		return 'id_campanha nao foi encontrado', 412

@app.route('/missingYou/api/v1.0/selecionarImgCampanha/<int:id_campanha>', methods=['GET'])
def selecionarImagemCampanha(id_campanha): #seleciona campanha daquele id
	try:
		conexao = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503

	sql = "SELECT imagem FROM CampanhasPerdidos_Imagens " + " WHERE CampanhasPerdidos_Imagens.idcampanhasperdidos = " + str(id_campanha)
	resultado = None
	cur = banco.cursor()
	cur.execute(sql)
	resultado = cur.fetchall();
	resultList = []
	if(resultado):
		for elemento in resultado:
			consultaEmDict = collections.OrderedDict()
			consultaEmDict = {'idCampanhas': elemento[0], 'Imagem': elemento[1]} 
			resultList.append(consultaEmDict)

		return jsonify(resultList)
	else:
		return 'imagem nao encontrada', 412

@app.route('/missingYou/api/v1.0/ExcluirImagem/<int:id_campanha>/<string:imagem>', methods=['DELETE'])
def excluirImagem(id_campanha, imagem):  # exclui todas as campanhas cadastradas por aquele usuario
	try:
		conexao = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503

	sql = "SELECT * FROM CampanhasPerdidos_Imagens" + " WHERE CampanhasPerdidos_Imagens.idCampanhasPerdidos = " + str(id_campanha)
	cur = banco.cursor()
	cur.execute(sql)
	resultado = cur.fetchall();
	cur.close()
	if(resultado):
		sql = "DELETE FROM CampanhasPerdidos_Imagens WHERE CampanhasPerdidos_Imagens.idcampanhasperdidos = " + str(id_campanha) + "and CampanhasPerdidos_Imagens.imagem = " + "'"+str(imagem)+"'"
		cur = banco.cursor()
		cur.execute(sql)
		banco.commit()
		cur.close();
		return 'operacao realizada com sucesso', 200
	else:
		return 'id_campanha nao foi encontrado', 412

@app.route('/missingYou/api/v1.0/cadastrarNotificacoes', methods=['POST'])
def cadastraNotificacoes():
	try:
		conexao = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503

	data = request.get_json()
	cur = conexao.cursor()
	sql = 'SELECT * FROM campanhasperdidos WHERE idcampanhasperdidos =' + str(data["idcampanhasperdidos"])
	cur.execute(sql)
	consulta1 = cur.fetchall()

	cur = conexao.cursor()
	sql1 = 'SELECT * FROM usuario WHERE iduser =' + str(data["idusuario"])
	cur.execute(sql1)
	consulta = cur.fetchall()
	print(consulta1)
	print(consulta)
	if (consulta1 and consulta):
		sql = "INSERT INTO Notificacoes(idnotificacao, idusuario, idcampanhasperdidos,descricao, dataatt) VALUES" + "(" + str(data["idnotificacao"]) + "," + str(data["idusuario"]) + "," + str(
		data["idcampanhasperdidos"]) + "," + "'" + data["descricao"] + "'" + "," + "'" + data["dataatt"] + "'" + ")"
		cur.execute(sql)
		conexao.commit()
		return 'operacao realizada com sucesso', 200
	else:
		return 'id nao foi encontrado', 412


@app.route('/missingYou/api/v1.0/excluirNotificacoes/<int:idUser>', methods=['DELETE'])
def excluirNotificacoes(idUser):
	try:
		conexao = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503

	cur = conexao.cursor()
	sql = "DELETE FROM notificacoes WHERE idusuario = " + str(idUser)
	cur.execute(sql)
	conexao.commit()
	return 'operacao realizada com sucesso', 200

@app.route('/missingYou/api/v1.0/selecionarNotificacoes/<int:idUser>', methods=['GET'])
def selecionarNotificacao(idUser):
	try:
		conexao = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503

	cur = conexao.cursor()
	sql = 'SELECT * FROM notificacoes WHERE idusuario =' + str(idUser)
	cur.execute(sql)
	consulta = cur.fetchall()
	resultList = []
	for elemento in consulta:
		consultaEmDict = collections.OrderedDict()
		consultaEmDict = {'idNotificacao': elemento[0], 'idUser': elemento[1], 'idCampanhas': elemento[2],
			   'descricao':elemento[3], 'dataAtt': elemento[4]} 
		resultList.append(consultaEmDict)

	return jsonify(resultList)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
