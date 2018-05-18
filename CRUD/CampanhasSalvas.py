import psycopg2

class CampanhasSalvas(object):
    banco = psycopg2.connect(host = 'localhost', database = 'MissingYou', user = 'postgres',  password = 'and123')
    # mudar para host = 'missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com', database = 'missingyoudb', user = 'Missingyouufc', password = 'missingyouufc2018'
    
    """
            retorno == 1 siginifica que a operacao foi realizada com sucesso
            retorno == 2 id_campanha nao foi encontrado
            retorno == 3 id_usario nao foi encontrado
            retorno 4 == camapnha ja cadastrada
    """

    def _init_(self):
        # ATENÇÃO: CASO HAJA AS CONFIGURAÇÕES DO BANCO SEJA DIFERENTE DAS CONFIGURAÇÕES ACIMA, MUDE OS VALORES DAS VARIAVEIS
        self.banco = psycopg2.connect(host = 'localhost', database = 'MissingYou', user = 'postgres',  password = 'and123')
        # mudar para host = 'missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com', database = 'missingyoudb', user = 'Missingyouufc', password = 'missingyouufc2018'

    def inserirCampanha(self, id_campanha, id_user): # ver se precisa tratar o caso da campanha ja estar cadastrada
        #   VERIFICANDO SE O USUÁRIO EXISTE
        cur = self.banco.cursor()
        sql = "SELECT * FROM usuario WHERE usuario.iduser = " + str(id_user)
        resultado = None
        cur.execute(sql)
        resultado = cur.fetchall();
        cur.close()

        if(resultado):
            #   VERIFICANDO SE CAMPANHA EXISTE
            cur = self.banco.cursor()
            sql = "SELECT * FROM campanhasperdidos WHERE campanhasperdidos.idcampanhasperdidos = " + str(id_campanha)
            resultado = None
            cur.execute(sql)
            resultado = cur.fetchall();
            cur.close()
            
            if(resultado):
                cur = self.banco.cursor()
                sql = "SELECT * FROM campanhassalvas WHERE campanhassalvas.idusuario = " + str(id_user) + "and campanhassalvas.idcampanhasperdidos =  " + str(id_campanha)
                resultado = None
                cur.execute(sql)
                resultado = cur.fetchall();
                cur.close()
                if(resultado):
                    return 4
                else:
                    cur = self.banco.cursor()
                    sql = "INSERT INTO campanhassalvas(idusuario, idcampanhasperdidos) VALUES("+ str(id_user)  + ", " + str(id_campanha)  + ")"
                    cur.execute(sql)
                    self.banco.commit()
                    cur.close()
                    return 1
            else:
                return 2
        else:
            return 3
    
    def selecionarCampanhaIdCampanha(self, id_campanha): #seleciona campanha daquele id
        sql = "SELECT * FROM campanhassalvas " + " WHERE campanhassalvas.idcampanhasperdidos = " + str(id_campanha)
        resultado = None
        cur = self.banco.cursor()
        cur.execute(sql)
        resultado = cur.fetchall();
        if(resultado):
            return resultado
        else:
            return 2

    def selecionarCampanhaIdUser(self, id_user): #seleciona as campanhas cadastradas por um usuário
        sql = "SELECT * FROM campanhassalvas" + " WHERE campanhassalvas.idusuario = " + str(id_user)
        cur = self.banco.cursor()
        cur.execute(sql)
        resultado = cur.fetchall();
        cur.close()
        if(resultado):
            return resultado
        else:
            return 3
    
    def excluirCampanhasDoUsuario(self, id_user):  # exclui todas as campanhas cadastradas por aquele usuario
        sql = "SELECT * FROM campanhassalvas" + " WHERE campanhassalvas.idusuario = " + str(id_user)
        cur = self.banco.cursor()
        cur.execute(sql)
        resultado = cur.fetchall();
        cur.close()
        if(resultado):
            id = None
            for linha in resultado:
                id = linha[0]
                sql = "DELETE FROM campanhassalvas WHERE campanhassalvas.idcampanhasperdidos = " + str(id) 
                cur = self.banco.cursor()
                cur.execute(sql)
                self.banco.commit()
                cur.close();
            return 1
        else:
            return 3

    def excluirCampanha(self, id_campanha): #exclui a campanha
        sql = "SELECT * FROM campanhassalvas " + " WHERE campanhassalvas.idcampanhasperdidos = " + str(id_campanha)
        resultado = None
        cur = self.banco.cursor()
        cur.execute(sql)
        resultado = cur.fetchall();
        if(resultado):
            sql = "DELETE FROM campanhassalvas WHERE campanhassalvas.idcampanhasperdidos = " + str(id_campanha) 
            cur = self.banco.cursor()
            cur.execute(sql)
            self.banco.commit()
            cur.close();
            return 1
        else:
            return 2

nova = CampanhasSalvas()
print(nova.inserirCampanha(1, 3))
print(nova.inserirCampanha(4, 3))
print(nova.selecionarCampanhaIdUser(3))
print(nova.selecionarCampanhaIdUser(4))
print(nova.selecionarCampanhaIdCampanha(10))
print(nova.selecionarCampanhaIdCampanha(1))
print(nova.excluirCampanha(2))
print(nova.excluirCampanha(1))