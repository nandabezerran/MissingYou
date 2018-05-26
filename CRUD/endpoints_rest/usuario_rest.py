import db_utils, usuario_db
from flask import Flask, jsonify
from flask import abort

 
@app.route('/missingYou/api/v1.0/usuario/<int:idUser>', methods=['GET'])
def selecionarUsuario(idUser):
	try:
		conexao = db_utils.connect_db()
	except:
		return 'nao conectou ao banco',503

	result = usuario_db.seleciona_usuario(idUser, conexao)

	return jsonify(consultaEmDict)
