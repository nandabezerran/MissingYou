#!flask/bin/python
from flask import Flask
from flask import jsonify
from datetime import date
import collections
import psycopg2

app = Flask(__name__)

@app.route('/missingYou/api/v1.0/cadastrarNotificacoes/<int:idnotificacao>/<int:idusuario>/<int:idcampanhasperdidos>/<string:descricao>/<string:dataatt>', methods=['GET'])
def cadastraNotificacoes(idnotificacao, idusuario, idcampanhasperdidos, descricao, dataatt):
	try:
		conexao = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503


	cur = conexao.cursor()
	sql = 'SELECT * FROM campanhasperdidos WHERE idcampanhasperdidos =' + str(idcampanhasperdidos)
	cur.execute(sql)
	consulta1 = cur.fetchall()

	cur = conexao.cursor()
	sql1 = 'SELECT * FROM usuario WHERE iduser =' + str(idusuario)
	cur.execute(sql1)
	consulta = cur.fetchall()
	print(consulta1)
	print(consulta)
	if (consulta1 and consulta):
		sql = "INSERT INTO Notificacoes(idnotificacao, idusuario, idcampanhasperdidos,descricao, dataatt) VALUES" + "(" + str(idnotificacao) + "," + str(idusuario) + "," + str(
		idcampanhasperdidos) + "," + "'" + descricao + "'" + "," + "'" + dataatt + "'" + ")"
		cur.execute(sql)
		conexao.commit()
		return 'operacao realizada com sucesso', 200
	else:
		return 'id nao foi encontrado', 412


@app.route('/missingYou/api/v1.0/excluirNotificacoes/<int:idUser>', methods=['GET'])
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
