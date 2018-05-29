#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
import psycopg2
from datetime import date
app = Flask(__name__)

@app.route('/missingYou/api/v1.0/validaDataParaBo/<string:dataDes>', methods=['GET'])
def validarDataParaBO(dataDes):
	"""
	return 1 -> nao precisa informar B.O.
	return 2 -> precisa informar B.O. 
	"""
	hoje = date.today()
	desap = dataDes.split("-")
	#formato -> date(ano,mes, dia)
	desap_date = date(int(desap[2]), int(desap[1]), int(desap[0]))
	prazo = hoje - desap_date
	if(prazo.days < 3): # se o prazo for menor que 1 ele nao precisa informar o numero de bo
		return 'nao precisa informar B.O.',200
	else: # se o prazo for maior que 3 ele  precisa informar o numero de bo
		return 'precisa informar B.O.',412


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



class campanhasperdidos_imagens(object):
    banco = psycopg2.connect(host = 'missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com', database = 'missingyoudb', user = 'Missingyouufc',  password = 'missingyouufc2018')
    # mudar para host = 'missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com', database = 'missingyoudb', user = 'Missingyouufc', password = 'missingyouufc2018'
    
    """
            retorno == 1 siginifica que a operacao foi realizada com sucesso
            retorno == 2 imagem nao encontrada
            retorno == 3 id_campanha nao foi encontrado
            retorno 4 == camapnha ja cadastrada
    """

    def _init_(self):
        # ATENÇÃO: CASO HAJA AS CONFIGURAÇÕES DO BANCO SEJA DIFERENTE DAS CONFIGURAÇÕES ACIMA, MUDE OS VALORES DAS VARIAVEIS
        self.banco = psycopg2.connect(host = 'localhost', database = 'MissingYou', user = 'postgres',  password = 'and123')
        # mudar para host = 'missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com', database = 'missingyoudb', user = 'Missingyouufc', password = 'missingyouufc2018'

    def inserirCampanha(self, id_campanha, imagem): # ver se precisa tratar o caso da campanha ja estar cadastrada
        #   VERIFICANDO SE CAMPANHA EXISTE
        cur = self.banco.cursor()
        sql = "SELECT * FROM campanhasperdidos WHERE campanhasperdidos.idcampanhasperdidos = " + str(id_campanha)
        resultado = None
        cur.execute(sql)
        resultado = cur.fetchall();
        cur.close()
            
        if(resultado):
            cur = self.banco.cursor()
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
                    return 4
                else:
                    cur = self.banco.cursor()
                    sql = "INSERT INTO CampanhasPerdidos_Imagens(idCampanhasPerdidos, imagem) VALUES("+ str(id_campanha)  + ", " + "'"+str(imagem)+"'"  + ")"
                    cur.execute(sql)
                    self.banco.commit()
                    cur.close()
                    return 1
            else:
                return 2
        else:
            return 3
    
    def selecionarImagemCampanha(self, id_campanha): #seleciona campanha daquele id
        sql = "SELECT imagem FROM CampanhasPerdidos_Imagens " + " WHERE CampanhasPerdidos_Imagens.idcampanhasperdidos = " + str(id_campanha)
        resultado = None
        cur = self.banco.cursor()
        cur.execute(sql)
        resultado = cur.fetchall();
        if(resultado):
            return resultado
        else:
            return 2
    
    def excluirImagem(self, id_campanha, imagem):  # exclui todas as campanhas cadastradas por aquele usuario
        sql = "SELECT * FROM CampanhasPerdidos_Imagens" + " WHERE CampanhasPerdidos_Imagens.idCampanhasPerdidos = " + str(id_campanha)
        cur = self.banco.cursor()
        cur.execute(sql)
        resultado = cur.fetchall();
        cur.close()
        if(resultado):
            sql = "DELETE FROM CampanhasPerdidos_Imagens WHERE CampanhasPerdidos_Imagens.idcampanhasperdidos = " + str(id_campanha) + "and CampanhasPerdidos_Imagens.imagem = " + "'"+str(imagem)+"'"
            cur = self.banco.cursor()
            cur.execute(sql)
            self.banco.commit()
            cur.close();
            return 1
        else:
            return 3

nova = campanhasperdidos_imagens()