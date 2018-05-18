import psycopg2
from datetime import date

# Ideia para validar campanha:  manda o request pro servidor lá, ai pega o token e aimg do captcha e envia para aplicação pro usuário validar.
# Dai o usuário digita e remanda pro servidor e pum

class CampanhasDesaparecidos(object):
    banco = psycopg2.connect(host = 'localhost', database = 'MissingYou', user = 'postgres',  password = 'and123')
     # mudar para host = 'missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com', database = 'missingyoudb', user = 'Missingyouufc', password = 'missingyouufc2018'
    
    """
            retorno == 1 siginifica que a operacao foi realizada com sucesso
            retorno == 2 id_campanha nao foi encontrado
            retorno == 3 id_usario nao foi encontrado
            retorno == 4 campanha ja cadastrada
            retorno == 5 informar o bo para cadastrar camp
    """
    def _init_(self):
        # ATENÇÃO: CASO HAJA AS CONFIGURAÇÕES DO BANCO SEJA DIFERENTE DAS CONFIGURAÇÕES ACIMA, MUDE OS VALORES DAS VARIAVEIS
        self.banco = psycopg2.connect(host = 'localhost', database = 'MissingYou', user = 'postgres',  password = 'and123')
        # mudar para host = 'missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com', database = 'missingyoudb', user = 'Missingyouufc', password = 'missingyouufc2018'

    def validarDataParaBO(self, datades):
        """
            return 1 -> nao precisa informar B.O.
            return 2 -> precisa informar B.O. 
        """
        hoje = date.today()
        desap = datades.split("-")
        #formato -> date(ano,mes, dia)
        desap_date = date(int(desap[2]), int(desap[1]), int(desap[0]))
        prazo = hoje - desap_date
        if(prazo.days < 3): # se o prazo for menor que 1 ele nao precisa informar o numero de bo
            return 1
        else: # se o prazo for maior que 3 ele  precisa informar o numero de bo
            return 2

    def cadastrarCampanha(self, id_campanha, id_user,  status, datanasc, nome_des, idade_des, sexo_des, olhos, raca, cabelo, data_des, bo, descricao):
        #verificando se o usuario existe
        cur = self.banco.cursor()
        sql = "SELECT * FROM usuario WHERE usuario.iduser = " + str(id_user)
        resultado = None
        cur.execute(sql)
        resultado = cur.fetchall();
        cur.close()
        data_camp = date.today()
        if(resultado):
            #verificando se a campanha ja esta cadastrada
            cur = self.banco.cursor()
            sql = "SELECT * FROM campanhasperdidos WHERE campanhasperdidos.idcampanhasperdidos = " + str(id_campanha)
            resultado = None
            cur.execute(sql)
            resultado = cur.fetchall();
            cur.close()
            
            if(resultado):
                return 4
            else:
                if(self.validarDataParaBO(data_des) == 1):
                    cur = self.banco.cursor()                                                                                                                                                     
                    sql = "INSERT INTO campanhasperdidos(idcampanhasperdidos, iduser, statuscampanhasperdidos, datanascimento, nomedesaparecido, idadedesaparecido, sexodesaparecido, olhosdesaparecido, racadesaparecido, cabelodesaparecido, datadesaparecimento, datacampanha, bo, descricao) values (" + str(id_campanha) + ", " + str(id_user) + ", " + "'"+str(status)+"'"+ ", " + "'"+str(datanasc)+"'"+ ", " + "'"+str(nome_des)+"'" + ", " + "'"+str(idade_des)+"'"+ ", "+ "'"+str(sexo_des)+"'" + ", " + "'"+str(olhos)+"'"+ ", "+ "'"+str(raca)+"'" + ", " + "'"+str(cabelo)+"'" + ", " + "'"+str(data_des)+"'" + ", " + "'"+str(data_camp)+"'" + ", " + "'"+str(bo)+"'"+  ", " + "'"+str(descricao)+"'" + ")"
                    cur.execute(sql)
                    self.banco.commit()
                    cur.close()
                    return 1
                else:
                    return 5
        else:
            return 3

    
    def selecionarCampanhasBoNull(self):
        sql = "SELECT idcampanhasperdidos FROM campanhasperdidos WHERE campanhasperdidos.bo = 'null' "
        resultado = None
        cur = self.banco.cursor()
        cur.execute(sql)
        resultado = cur.fetchall();
        if(resultado):
            return resultado
        else: 
            return 2

    def selecionarCampanhaId(self, id_campanha): #seleciona campanha daquele id
        sql = "SELECT * FROM campanhasperdidos " + " WHERE campanhasperdidos.idcampanhasperdidos = " + str(id_campanha)
        resultado = None
        cur = self.banco.cursor()
        cur.execute(sql)
        resultado = cur.fetchall();
        if(resultado):
            return resultado
        else:
            return 2

    def selecionarCampanhaUser(self, id_user): #seleciona as campanhas cadastradas por um usuário
        sql = "SELECT * FROM campanhasperdidos" + " WHERE campanhasperdidos.iduser = " + str(id_user)
        cur = self.banco.cursor()
        cur.execute(sql)
        resultado = cur.fetchall();
        cur.close()
        if(resultado):
            return resultado
        else:
            return 3

    def alterarStatus(self, id_campanha, status): #altera o status de uma campanha
        sql = "SELECT * FROM campanhasperdidos " + " WHERE campanhasperdidos.idcampanhasperdidos = " + str(id_campanha) 
        resultado = None
        cur = self.banco.cursor()
        cur.execute(sql)
        resultado = cur.fetchall();
        
        if(resultado):
	        sql = "UPDATE campanhasperdidos" + " SET statuscampanhasperdidos = " + "'"+str(status)+"'" + " WHERE idcampanhasperdidos = " + str(id_campanha)
	        cur = self.banco.cursor()
	        cur.execute(sql)
	        self.banco.commit()
	        cur.close();
	        return 1
        else:
    	    return 2

    def alterarNome(self, id_campanha, nome):
        sql = "SELECT * FROM campanhasperdidos " + " WHERE campanhasperdidos.idcampanhasperdidos = " + str(id_campanha)
        resultado = None
        cur = self.banco.cursor()
        cur.execute(sql)
        resultado = cur.fetchall();
        
        if(resultado):
            sql = "UPDATE campanhasperdidos" + " SET nomedesaparecido = " + "'"+str(nome)+"'" + " WHERE idcampanhasperdidos = " + str(id_campanha)
            cur = self.banco.cursor()
            cur.execute(sql)
            self.banco.commit()
            cur.close();
            return 1
        else:
            return 2
    
    def alterarCabelo(self, id_campanha, cabelo):
        sql = "SELECT * FROM campanhasperdidos " + " WHERE campanhasperdidos.idcampanhasperdidos = " + str(id_campanha)
        resultado = None
        cur = self.banco.cursor()
        cur.execute(sql)
        resultado = cur.fetchall();
        
        if(resultado):
            sql = "UPDATE campanhasperdidos" + " SET cabelodesaparecido = " + "'"+str(cabelo)+"'" + " WHERE idcampanhasperdidos = " + str(id_campanha)
            cur = self.banco.cursor()
            cur.execute(sql)
            self.banco.commit()
            cur.close();
            return 1
        else:
            return 2
    
    def alterarOlhos(self, id_campanha, olhos):
        sql = "SELECT * FROM campanhasperdidos " + " WHERE campanhasperdidos.idcampanhasperdidos = " + str(id_campanha) 
        resultado = None
        cur = self.banco.cursor()
        cur.execute(sql)
        resultado = cur.fetchall();
        
        if(resultado):
            sql = "UPDATE campanhasperdidos" + " SET olhosdesaparecido = " + "'"+str(olhos)+"'" + " WHERE idcampanhasperdidos = " + str(id_campanha)
            cur = self.banco.cursor()
            cur.execute(sql)
            self.banco.commit()
            cur.close();
            return 1
        else:
            return 2

    def alterarRaca(self, id_campanha, raca):
        sql = "SELECT * FROM campanhasperdidos " + " WHERE campanhasperdidos.idcampanhasperdidos = " + str(id_campanha) 
        resultado = None
        cur = self.banco.cursor()
        cur.execute(sql)
        resultado = cur.fetchall();
        
        if(resultado):
            sql = "UPDATE campanhasperdidos" + " SET racadesaparecido = " + "'"+str(raca)+"'" + " WHERE idcampanhasperdidos = " + str(id_campanha)
            cur = self.banco.cursor()
            cur.execute(sql)
            self.banco.commit()
            cur.close();
            return 1
        else:
            return 2

    def alterarIdade(self, id_campanha, idade):
        sql = "SELECT * FROM campanhasperdidos " + " WHERE campanhasperdidos.idcampanhasperdidos = " + str(id_campanha) 
        resultado = None
        cur = self.banco.cursor()
        cur.execute(sql)
        resultado = cur.fetchall();
        
        if(resultado):
            sql = "UPDATE campanhasperdidos" + " SET idadedesaparecido = " + "'"+str(idade)+"'" + " WHERE idcampanhasperdidos = " + str(id_campanha)
            cur = self.banco.cursor()
            cur.execute(sql)
            self.banco.commit()
            cur.close();
            return 1
        else:
            return 2

    def alterarSexo(self, id_campanha, sexo):
        sql = "SELECT * FROM campanhasperdidos " + " WHERE campanhasperdidos.idcampanhasperdidos = " + str(id_campanha) 
        resultado = None
        cur = self.banco.cursor()
        cur.execute(sql)
        resultado = cur.fetchall();
        
        if(resultado):
            sql = "UPDATE campanhasperdidos" + " SET sexodesaparecido = " + "'"+str(sexo)+"'" + " WHERE idcampanhasperdidos = " + str(id_campanha)
            cur = self.banco.cursor()
            cur.execute(sql)
            self.banco.commit()
            cur.close();
            return 1
        else:
            return 2

    def excluirCampanha(self, id_campanha): #exclui a campanha
        sql = "SELECT * FROM campanhasperdidos " + " WHERE campanhasperdidos.idcampanhasperdidos = " + str(id_campanha) 
        resultado = None
        cur = self.banco.cursor()
        cur.execute(sql)
        resultado = cur.fetchall();
        
        if(resultado):
            sql = "DELETE FROM campanhasperdidos WHERE campanhasperdidos.idcampanhasperdidos = " + str(id_campanha)
            cur = self.banco.cursor()
            cur.execute(sql)
            self.banco.commit()
            cur.close()
            return 1
        else:
            return 2

    def alterarBO(self, id_campanha, bo): #altera o B.O. de uma campanha
        sql = "SELECT * FROM campanhasperdidos " + " WHERE campanhasperdidos.bo = 'null' and campanhasperdidos.idcampanhasperdidos = " + str(id_campanha) 
        resultado = None
        cur = self.banco.cursor()
        cur.execute(sql)
        resultado = cur.fetchall();
        if(resultado):
	        sql = "UPDATE campanhasperdidos" + " SET bo = " + "'"+str(bo)+"'" + " WHERE idcampanhasperdidos = " + str(id_campanha)
	        cur = self.banco.cursor()
	        cur.execute(sql)
	        self.banco.commit()
	        cur.close();
        	return 1
        else:
            return 2
    
    def alterarDescricao(self, id_campanha, descricao):
        sql = "SELECT * FROM campanhasperdidos " + " WHERE campanhasperdidos.idcampanhasperdidos = " + str(id_campanha) 
        resultado = None
        cur = self.banco.cursor()
        cur.execute(sql)
        resultado = cur.fetchall();
        
        if(resultado):
            sql = "UPDATE campanhasperdidos" + " SET descricao = " + str(descricao) + "WHERE idcampanhasperdidos = " + str(id_campanha)
            cur = self.banco.cursor()
            cur.execute(sql)
            self.banco.commit()
            cur.close();
            return 1
        else:
            return 2
    
    

nova = CampanhasDesaparecidos()
print(nova.cadastrarCampanha(7, 3, 'ativado', '14-03-1998', 'Andreza', '19', 'f', 'azul', 'parda', 'castanho', '11-05-2018', '38t37326', 'ksksksk'))
# ---------------------------------- TESTES
#OK - tem que só que ver a comparação, pois pra dar certo to setando os bo sem numero como null print(nova.selecionarCampanhasBoNull())
# OK - print(nova.selecionarCampanhaId(1))
#OK - print(nova.selecionarCampanhaUser(3))
#print(nova.alterarStatus(1, "ta aqui"))
#print(nova.alterarSexo(1, "teste"))
#print(nova.alterarIdade(1, "teste"))
#print(nova.alterarBO(1, "teste"))
#print(nova.alterarRaca(1, "teste"))
#print(nova.alterarOlhos(1, "teste"))
#print(nova.alterarCabelo(1, "teste"))
#print(nova.alterarStatus(10, "ta aqui"))
#print(nova.alterarSexo(10, "teste"))
#print(nova.alterarIdade(10, "teste"))
#print(nova.alterarBO(10, "teste"))
#print(nova.alterarRaca(10, "teste"))
#print(nova.alterarOlhos(10, "teste"))
#print(nova.alterarCabelo(10, "teste"))
#print(nova.excluirCampanha(1))
#print(nova.excluirCampanha(40))
#print(nova.excluirCampanhasDoUsuario(2))
#print(nova.excluirCampanhasDoUsuario(3))