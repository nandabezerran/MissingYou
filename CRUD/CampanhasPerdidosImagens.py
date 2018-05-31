#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
import psycopg2
from datetime import date
app = Flask(__name__)


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