#!flask/bin/python
from flask import Flask
from flask import jsonify
from datetime import date
import collections
import psycopg2

app = Flask(__name__)
@app.route('/missingYou/api/v1.0/inserirLocalCampanha/<int:id_campanha>/<int:lat>/<int:lon>/<string:data>/<string:bairro>', methods=['GET'])
def inserirLocalCampanha(id_campanha, lat, lon, data, bairro):
	try:
		banco = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503

	# Checando se campanha existe
	sql = "SELECT * FROM campanhasperdidos " + " WHERE campanhasperdidos.idcampanhasperdidos = " + str(id_campanha)
	resultado = None
	cur = banco.cursor()
	cur.execute(sql)
	resultado = cur.fetchall();

	if(resultado):
		cur = banco.cursor()
		sql = "INSERT INTO attlocalizacaocampanhasperdidos(idcampanhasperdidos, latitude, longitude, attdata, attbairro) VALUES("+ str(id_campanha) + ", "  + str(lat) + ", " + str(lon) + ", " + "'"+str(data)+"'" + ", " + "'"+str(bairro)+"'" + ")"
		cur.execute(sql)
		banco.commit()
		cur.close()
		return 'operacao realizada com sucesso', 200
	else:
		return 'id_campanha nao foi encontrado', 412

@app.route('/missingYou/api/v1.0/selecionarCampanhaIdLocalizacao/<int:id_campanha>', methods=['GET'])
def selecionarCampanhaId(id_campanha): #seleciona a campanha daquele id
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

	sql = "SELECT * FROM attlocalizacaocampanhasperdidos " + " WHERE attlocalizacaocampanhasperdidos.attbairro = " + "'"+str(bairro)+"'"
	resultado = None
	cur = self.banco.cursor()
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

@app.route('/missingYou/api/v1.0/alterarLocal/<int:id_campanha>/<int:lat>/<int:lon>/<string:data>/<string:bairro>', methods=['GET'])
def alterarLocal(id_campanha, lat, lon, data, bairro):
	try:
		banco = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503

	# VERIFICANDO SE A CAMPANHA EXISTE
	sql = "SELECT * FROM attlocalizacaocampanhasperdidos " + " WHERE attlocalizacaocampanhasperdidos.idcampanhasperdidos = " + str(id_campanha)
	resultado = None
	cur = banco.cursor()
	cur.execute(sql)
	resultado = cur.fetchall();
	cur.close()

	if(resultado):
		sql = "UPDATE attlocalizacaocampanhasperdidos" + " SET latitude = " + str(lat) + ", longitude = " + str(lon) + ", attdata = " + "'"+str(data)+"'" + ", attbairro = " + "'"+str(bairro)+"'" + " WHERE idcampanhasperdidos = " + "'"+str(id_campanha)+"'"
		cur = self.banco.cursor()
		cur.execute(sql)
		banco.commit()
		cur.close()
		return 'operacao realizada com sucesso', 200
	else:
		return 'id_campanha nao foi encontrado', 412

@app.route('/missingYou/api/v1.0/excluirCampanha/<int:id_campanha>', methods=['GET'])
def excluirCampanha(id_campanha):
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

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)