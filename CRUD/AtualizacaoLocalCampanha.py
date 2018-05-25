import psycopg2

class AtualizacaoLocalCampanha(object):
    """
            retorno == 1 siginifica que a operacao foi realizada com sucesso
            retornO == 0 id_campanha nao foi encontrado
    """

    banco = psycopg2.connect(host = 'missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com', database = 'missingyoudb', user = 'Missingyouufc', password = 'missingyouufc2018')
    # mudar para host = 'missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com', database = 'missingyoudb', user = 'Missingyouufc', password = 'missingyouufc2018'

    def _init_(self):
        # ATENÇÃO: CASO HAJA AS CONFIGURAÇÕES DO BANCO SEJA DIFERENTE DAS CONFIGURAÇÕES ACIMA, MUDE OS VALORES DAS VARIAVEIS
        self.banco = psycopg2.connect(host = 'localhost', database = 'MissingYou', user = 'postgres',  password = 'and123')
        # mudar para host = 'missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com', database = 'missingyoudb', user = 'Missingyouufc', password = 'missingyouufc2018'
        
    def inserirLocalCampanha(self, id_campanha, lat, lon, data, bairro):
        # Checando se campanha existe
        sql = "SELECT * FROM campanhasperdidos " + " WHERE campanhasperdidos.idcampanhasperdidos = " + str(id_campanha)
        resultado = None
        cur = self.banco.cursor()
        cur.execute(sql)
        resultado = cur.fetchall();

        if(resultado):
            cur = self.banco.cursor()
            sql = "INSERT INTO attlocalizacaocampanhasperdidos(idcampanhasperdidos, latitude, longitude, attdata, attbairro) VALUES("+ str(id_campanha) + ", "  + str(lat) + ", " + str(lon) + ", " + "'"+str(data)+"'" + ", " + "'"+str(bairro)+"'" + ")"
            cur.execute(sql)
            self.banco.commit()
            cur.close()
            return 1
        else:
            return 2 
    
    def selecionarCampanhaId(self, id_campanha): #seleciona a campanha daquele id
        sql = "SELECT * FROM attlocalizacaocampanhasperdidos " + " WHERE attlocalizacaocampanhasperdidos.idcampanhasperdidos = " + str(id_campanha)
        resultado = None
        cur = self.banco.cursor()
        cur.execute(sql)
        resultado = cur.fetchall();
        cur.close()
        if(resultado):
            return resultado
        else:
            return 2

    def selecionarCampanhaBairro(self, bairro): #seleciona as campanhas por bairro
        sql = "SELECT * FROM attlocalizacaocampanhasperdidos " + " WHERE attlocalizacaocampanhasperdidos.attbairro = " + "'"+str(bairro)+"'"
        resultado = None
        cur = self.banco.cursor()
        cur.execute(sql)
        resultado = cur.fetchall();
        cur.close()
        if(resultado):
            return resultado
        else:
            return 2

    def alterarLocal(self, id_campanha, lat, lon, data, bairro):
        # VERIFICANDO SE A CAMPANHA EXISTE
        sql = "SELECT * FROM attlocalizacaocampanhasperdidos " + " WHERE attlocalizacaocampanhasperdidos.idcampanhasperdidos = " + str(id_campanha)
        resultado = None
        cur = self.banco.cursor()
        cur.execute(sql)
        resultado = cur.fetchall();
        cur.close()

        if(resultado):
            sql = "UPDATE attlocalizacaocampanhasperdidos" + " SET latitude = " + str(lat) + ", longitude = " + str(lon) + ", attdata = " + "'"+str(data)+"'" + ", attbairro = " + "'"+str(bairro)+"'" + " WHERE idcampanhasperdidos = " + "'"+str(id_campanha)+"'"
            cur = self.banco.cursor()
            cur.execute(sql)
            self.banco.commit()
            cur.close()
            return 1
        else:
            return 2
    def excluirCampanha(self, id_campanha):
        # VERIFICANDO SE A CAMPANHA EXISTE
        sql = "SELECT * FROM attlocalizacaocampanhasperdidos " + " WHERE attlocalizacaocampanhasperdidos.idcampanhasperdidos = " + str(id_campanha)
        resultado = None
        cur = self.banco.cursor()
        cur.execute(sql)
        resultado = cur.fetchall();
        cur.close()
        if(resultado): 
            sql = "DELETE FROM attlocalizacaocampanhasperdidos WHERE attlocalizacaocampanhasperdidos.idcampanhasperdidos = " + str(id_campanha)
            cur = self.banco.cursor()
            cur.execute(sql)
            self.banco.commit()
            cur.close()
            return 1
        else:
            return 2
    
nova = AtualizacaoLocalCampanha()