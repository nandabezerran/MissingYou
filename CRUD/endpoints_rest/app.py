import db_utils, usuario_db
import error_codes
from flask import Flask, jsonify, abort

app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
	return "Test"


###############################
########### Usuario ###########
###############################

@app.route('/missingYou/api/v1.0/selecionarUsuario/<int:idUser>', methods=['GET'])
def selecionarUsuario(idUser):
	try:
		conexao = db_utils.connect_db()
	except:
		return 'Nao conectou ao banco', error_codes.SERVICE_UNAVAILABLE #503

	result = usuario_db.seleciona_usuario(idUser, conexao)
	return jsonify(result)


#################################
########### Campanhas ###########
#################################







if __name__ == '__main__':
    app.run(host="127.0.0.1", port=80)