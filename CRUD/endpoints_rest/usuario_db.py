
def seleciona_usuario(idUser, conexao):
	cur = conexao.cursor()
	sql = 'SELECT * FROM usuario WHERE idUser =' + str(idUser)
	cur.execute(sql)
	consulta = cur.fetchall()
	consultaEmDict = [{'idUser': elemento[0], 'nomeUser': elemento[1], 'emailUser': elemento[2],
			   'cpfUser':elemento[3], 'contatoUser': elemento[4], 'senhaUser': elemento[5], 
			   'imagemUser':elemento[6]} for elemento in consulta]
	return consultaEmDict
