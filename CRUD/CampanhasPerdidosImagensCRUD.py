#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
import psycopg2
from datetime import date
app = Flask(__name__)

@app.route('/missingYou/api/v1.0/inserirImgCampanha/<int:id_campanha>/<string:imagem>', methods=['GET'])	
def inserirCampanha(id_campanha, imagem): # ver se precisa tratar o caso da campanha ja estar cadastrada
	try:
		conexao = psycopg2.connect(database= "MissingYouBanco", user="Missingyouufc", password="Missingyouufc2018",
						 host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", port="5432")
	except:
		return 'nao conectou ao banco',503

	#   VERIFICANDO SE CAMPANHA EXISTE
	cur = banco.cursor()
	sql = "SELECT * FROM campanhasperdidos WHERE campanhasperdidos.idcampanhasperdidos = " + str(id_campanha)
	resultado = None
	cur.execute(sql)
	resultado = cur.fetchall();
	cur.close()
            
	if(resultado):
		cur = banco.cursor()
		sql = "SELECT * FROM imagens WHERE imagens.imagem = " + "'"+str(imagem)+"'"
		resultado = None
		cur.execute(sql)
		resultado = cur.fetchall();
		cur.close()
		if(resultado):
			cur = self.banco.cursor()
			sql = "SELECT * FROM CampanhasPerdidos_Imagens WHERE CampanhasPerdidos_Imagens.imagem = " + "'"+str(imagem)+"'" + "and CampanhasPerdidos_Imagens.idcampanhasperdidos = " + str(id_campanha)
			resultado = None
			cur.execute(sql)
			resultado = cur.fetchall();
			cur.close()
			if(resultado):
				return 'campanha ja cadastrada', 412
			else:
				cur = banco.cursor()
				sql = "INSERT INTO CampanhasPerdidos_Imagens(idCampanhasPerdidos, imagem) VALUES("+ str(id_campanha)  + ", " + "'"+str(imagem)+"'"  + ")"
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

@app.route('/missingYou/api/v1.0/ExcluirImagem/<int:id_campanha>/<string:imagem>', methods=['GET'])
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

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
