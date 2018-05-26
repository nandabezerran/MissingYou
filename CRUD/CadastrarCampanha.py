#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
import psycopg2
from ValidarDataParaBo import validarDataParaBO
from datetime import date
app = Flask(__name__)

@app.route('/missingYou/api/v1.0/cadastrarCampanha/<int:id_campanha>/<int:id_user>/<string:status>/<string:datanasc>/<string:nome_des>/<string:idade_des>/<string:sexo_des>/<string:olhos>/<string:raca>/<string:cabelo>/<string:data_des>/<string:bo>/<string:descricao>', methods=['GET'])
def cadastrarCampanha(id_campanha, id_user,  status, datanasc, nome_des, idade_des, sexo_des, olhos, raca, cabelo, data_des, bo, descricao):
	#verificando se o usuario existe
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



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
