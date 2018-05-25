#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
import psycopg2

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)

