#!flask/bin/python
from flask import Flask
from flask import jsonify
from datetime import date
import collections
import psycopg2

app = Flask(__name__)

@app.route('/missingYou/api/v1.0/inserirCampanha/<int:id_campanha>/<int:id_user>', methods=['GET'])
def inserirCampanha(id_campanha, id_user): # ver se precisa tratar o caso da campanha ja estar cadastrada
        #   VERIFICANDO SE O USUARIO EXISTE
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

	if(resultado):
		#   VERIFICANDO SE CAMPANHA EXISTE
		cur = banco.cursor()
		sql = "SELECT * FROM campanhasperdidos WHERE campanhasperdidos.idcampanhasperdidos = " + str(id_campanha)
		resultado = None
		cur.execute(sql)
		resultado = cur.fetchall();
		cur.close()
            
		if(resultado):
			cur = banco.cursor()
			sql = "SELECT * FROM campanhassalvas WHERE campanhassalvas.idusuario = " + str(id_user) + "and campanhassalvas.idcampanhasperdidos =  " + str(id_campanha)
			resultado = None
			cur.execute(sql)
			resultado = cur.fetchall();
			cur.close()
			if(resultado):
				return 'campanha ja salva', 412
			else:
				cur = banco.cursor()
				sql = "INSERT INTO campanhassalvas(idusuario, idcampanhasperdidos) VALUES("+ str(id_user)  + ", " + str(id_campanha)  + ")"
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

@app.route('/missingYou/api/v1.0/excluirCampanhasDoUsuario/<int:id_user>', methods=['GET'])
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

@app.route('/missingYou/api/v1.0/excluirCampanha/<int:id_campanha>', methods=['GET'])
def excluirCampanha(id_campanha): #exclui a campanha
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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)