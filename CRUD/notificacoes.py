import psycopg2

class Notificacoes(object):

    conexao = None

    def __init__(self):
        self.conexao = psycopg2.connect(host='missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com', database= 'missingyoudb', user='Missingyouufc', password='missingyouufc2018)')


    def cadastrarotificacoes(self, idusuario, idcampanhasperdidos, descricao, dataatt):

        cur = self.conexao.cursor()

        cur = self.conexao.cursor()
        sql = 'SELECT * FROM campanhasperdidos WHERE idcampanhasperdidos =' + str(idcampanhasperdidos)
        cur.execute(sql)
        consulta1 = cur.fetchall()

        cur = self.conexao.cursor()
        sql1 = 'SELECT * FROM usuario WHERE iduser =' + str(idusuario)
        cur.execute(sql1)
        consulta = cur.fetchall()
        print(consulta1)
        print(consulta)
        if (consulta1 and consulta):
            sql = "INSERT INTO Notificacoes(idusuario, idcampanhasperdidos,descricao, dataatt) VALUES" + "(" + str(idusuario) + "," + str(
                idcampanhasperdidos) + "," + "'" + descricao + "'" + "," + "'" + dataatt + "'" + ")"
            cur.execute(sql)
            self.conexao.commit()
            return 1
        else:
            return 0



    def excluirNotificacoes(self, idUser):
        cur = self.conexao.cursor()
        sql = "DELETE FROM notificacoes WHERE idusuario = " + str(idUser)
        cur.execute(sql)
        self.conexao.commit()
        return 1


    def selecionarNotificacao(self, idUser):
        cur = self.conexao.cursor()
        sql = 'SELECT * FROM notificacoes WHERE idusuario =' + str(idUser)
        cur.execute(sql)
        consulta = cur.fetchall()
        return consulta

