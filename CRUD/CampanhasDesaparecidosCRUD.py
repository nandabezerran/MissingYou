#!flask/bin/python
from flask import Flask
from flask import jsonify
from datetime import date
import collections
import psycopg2

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


@app.route('/missingYou/api/v1.0/cadastrarCampanha/<int:id_campanha>/<int:id_user>/<string:status>/<string:datanasc>/<string:nome_des>/<string:idade_des>/<string:sexo_des>/<string:olhos>/<string:raca>/<string:cabelo>/<string:data_des>/<string:bo>/<string:descricao>', methods=['GET'])
def cadastrarCampanha(id_campanha, id_user,  status, datanasc, nome_des, idade_des, sexo_des, olhos, raca, cabelo, data_des, bo, descricao):
	try:
		banco = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503

	cur = banco.cursor()
	sql = "SELECT * FROM usuario WHERE usuario.iduser = " + str(id_user)
	resultado = None
	cur.execute(sql)
	resultado = cur.fetchall();
	cur.close()
	data_camp = date.today()
	if(resultado):
		#verificando se a campanha ja esta cadastrada
		cur = banco.cursor()
		sql = "SELECT * FROM campanhasperdidos WHERE campanhasperdidos.idcampanhasperdidos = " + str(id_campanha)
		resultado = None
		cur.execute(sql)
		resultado = cur.fetchall();
		cur.close()
            
		if(resultado):
			return 'campanha ja cadastrada',412
		else:
			if(validarDataParaBO(data_des) == 'nao precisa informar B.O.',200):
				cur = banco.cursor()                                                                                                                                                     
				sql = "INSERT INTO campanhasperdidos(idcampanhasperdidos, iduser, statuscampanhasperdidos, datanascimento, nomedesaparecido, idadedesaparecido, sexodesaparecido, olhosdesaparecido, racadesaparecido, cabelodesaparecido, datadesaparecimento, datacampanha, bo, descricao) values (" + str(id_campanha) + ", " + str(id_user) + ", " + "'"+str(status)+"'"+ ", " + "'"+str(datanasc)+"'"+ ", " + "'"+str(nome_des)+"'" + ", " + "'"+str(idade_des)+"'"+ ", "+ "'"+str(sexo_des)+"'" + ", " + "'"+str(olhos)+"'"+ ", "+ "'"+str(raca)+"'" + ", " + "'"+str(cabelo)+"'" + ", " + "'"+str(data_des)+"'" + ", " + "'"+str(data_camp)+"'" + ", " + "'"+str(bo)+"'"+  ", " + "'"+str(descricao)+"'" + ")"
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

@app.route('/missingYou/api/v1.0/alterarStatusCampanha/<int:id_campanha>/<string:status>', methods=['GET'])
def alterarStatus(id_campanha, status): #altera o status de uma campanha
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
		sql = "UPDATE campanhasperdidos" + " SET statuscampanhasperdidos = " + "'"+str(status)+"'" + " WHERE idcampanhasperdidos = " + str(id_campanha)
		cur = banco.cursor()
		cur.execute(sql)
		banco.commit()
		cur.close();
		return 'operacao realizada com sucessa', 200
	else:
		return 'id_campanha nao foi encontrada', 412

@app.route('/missingYou/api/v1.0/alterarNomeDesaparecido/<int:id_campanha>/<string:nome>', methods=['GET'])
def alterarNome(id_campanha, nome):
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
		sql = "UPDATE campanhasperdidos" + " SET nomedesaparecido = " + "'"+str(nome)+"'" + " WHERE idcampanhasperdidos = " + str(id_campanha)
		cur = banco.cursor()
		cur.execute(sql)
		banco.commit()
		cur.close();
		return 'operacao realizada com sucessa', 200
	else:
		return 'id_campanha nao foi encontrada', 412

@app.route('/missingYou/api/v1.0/alterarCabeloDesaparecido/<int:id_campanha>/<string:cabelo>', methods=['GET'])
def alterarCabelo(id_campanha, cabelo):
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
		sql = "UPDATE campanhasperdidos" + " SET cabelodesaparecido = " + "'"+str(cabelo)+"'" + " WHERE idcampanhasperdidos = " + str(id_campanha)
		cur = banco.cursor()
		cur.execute(sql)
		banco.commit()
		cur.close();
		return 'operacao realizada com sucessa', 200
	else:
		return 'id_campanha nao foi encontrada', 412

@app.route('/missingYou/api/v1.0/alterarRacaDesaparecido/<int:id_campanha>/<string:raca>', methods=['GET'])
def alterarRaca(id_campanha, raca):
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
		sql = "UPDATE campanhasperdidos" + " SET racadesaparecido = " + "'"+str(raca)+"'" + " WHERE idcampanhasperdidos = " + str(id_campanha)
		cur = banco.cursor()
		cur.execute(sql)
		banco.commit()
		cur.close();
		return 'operacao realizada com sucessa', 200
	else:
		return 'id_campanha nao foi encontrada', 412

@app.route('/missingYou/api/v1.0/alterarIdadeDesaparecido/<int:id_campanha>/<string:idade>', methods=['GET'])
def alterarIdade(id_campanha, idade):
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
		sql = "UPDATE campanhasperdidos" + " SET idadedesaparecido = " + "'"+str(idade)+"'" + " WHERE idcampanhasperdidos = " + str(id_campanha)
		cur = banco.cursor()
		cur.execute(sql)
		banco.commit()
		cur.close();
		return 'operacao realizada com sucessa', 200
	else:
		return 'id_campanha nao foi encontrada', 412

@app.route('/missingYou/api/v1.0/alterarSexoDesaparecido/<int:id_campanha>/<string:sexo>', methods=['GET'])
def alterarSexo(id_campanha, sexo):
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
		sql = "UPDATE campanhasperdidos" + " SET sexodesaparecido = " + "'"+str(sexo)+"'" + " WHERE idcampanhasperdidos = " + str(id_campanha)
		cur = banco.cursor()
		cur.execute(sql)
		banco.commit()
		cur.close();
		return 'operacao realizada com sucessa', 200
	else:
		return 'id_campanha nao foi encontrada', 412

@app.route('/missingYou/api/v1.0/excluirCampanha/<int:id_campanha>', methods=['GET'])
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

@app.route('/missingYou/api/v1.0/alterarBO/<int:id_campanha>/<string:bo>', methods=['GET'])
def alterarBO(id_campanha, bo): #altera o B.O. de uma campanha
	try:
		banco = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503

	sql = "SELECT * FROM campanhasperdidos " + " WHERE campanhasperdidos.bo = 'null' and campanhasperdidos.idcampanhasperdidos = " + str(id_campanha) 
	resultado = None
	cur = banco.cursor()
	cur.execute(sql)
	resultado = cur.fetchall();
	if(resultado):
		sql = "UPDATE campanhasperdidos" + " SET bo = " + "'"+str(bo)+"'" + " WHERE idcampanhasperdidos = " + str(id_campanha)
		cur = banco.cursor()
		cur.execute(sql)
		banco.commit()
		cur.close();
		return 'operacao realizada com sucessa', 200
	else:
		return 'id_campanha nao foi encontrada', 412

@app.route('/missingYou/api/v1.0/alterarDescricao/<int:id_campanha>/<string:descricao>', methods=['GET'])
def alterarDescricao(id_campanha, descricao):
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
		sql = "UPDATE campanhasperdidos" + " SET descricao = " + "'"+str(descricao)+"'" + "WHERE idcampanhasperdidos = " + str(id_campanha)
		cur = banco.cursor()
		cur.execute(sql)
		banco.commit()
		cur.close();
		return 'operacao realizada com sucessa', 200
	else:
		return 'id_campanha nao foi encontrada', 412



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
	

