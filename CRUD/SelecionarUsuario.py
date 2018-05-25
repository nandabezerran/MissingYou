#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
import psycopg2
app = Flask(__name__)
 
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

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
