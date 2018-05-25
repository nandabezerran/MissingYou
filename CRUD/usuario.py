#!flask/bin/python
from flask import Flask, jsonify
from flask import abort

app = Flask(__name__)

class Usuario(object):

    """
        codigo de retorno
        se:
            retorno == 1 siginifica que a operacao foi realizada com sucesso
            retorno == 0 id nao foi encontrado ou o cadastro ou exclusao falhou
            retorno == 2 email invalido ou email ja cadastrado no sistema
            retorno == 3 cpf invalido
            retorno == 4 contato invalido
            retorno == 5 senha invalida
    """

    conexao = None

def __init__(self):
	self.conexao = psycopg2.connect(host='missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com', database= 'missingyoudb', user='Missingyouufc', password='missingyouufc2018')



def excluirUsuario(self, idUser):

        cur = self.conexao.cursor()
        sql = 'SELECT * FROM usuario WHERE idUser =' + str(idUser)
        cur.execute(sql)
        consulta = cur.fetchall()

        if(consulta):
            cur = self.conexao.cursor()

            sql1 = "DELETE FROM notificacoes WHERE idusuario = " + str(idUser)
            cur.execute(sql1)
            self.conexao.commit()
            sql2 = "SELECT idcampanhasperdidos from campanhasperdidos WHERE iduser =" + str(idUser)
            cur.execute(sql2)
            res = cur.fetchall()
            id = None
            for linha in res:
                id = linha[0]
                sql3 = "DELETE FROM notificacoes WHERE idcampanhasperdidos = " + str(id)
                sql4 = "DELETE FROM campanhassalvas WHERE idcampanhasperdidos = " + str(id)
                cur.execute(sql3)
                cur.execute(sql4)
                self.conexao.commit()

            sql7 = "DELETE FROM campanhassalvas WHERE idusuario = " + str(idUser)
            sql5 = "DELETE FROM campanhasperdidos WHERE idUser = " + str(idUser)
            sql6 = "DELETE FROM usuario WHERE idUser = " + str(idUser)
            cur.execute(sql7)
            cur.execute(sql5)
            cur.execute(sql6)
            self.conexao.commit()
            return 1
        else:
            return 0

def selecionarUsuario(self, idUser):

        cur = self.conexao.cursor()
        sql = 'SELECT * FROM usuario WHERE idUser =' + str(idUser)
        cur.execute(sql)
        consulta = cur.fetchall()
        return consulta


def UpdateSenha(self, idUser, senhauser):

        cur = self.conexao.cursor()
        sql = 'SELECT * FROM usuario WHERE idUser =' + str(idUser)
        cur.execute(sql)
        consulta = cur.fetchall()

        if (consulta):
            if(len(senhauser) >= 6):
                sql = 'UPDATE usuario SET senhauser = ' + str(senhauser) + " WHERE idUser = " + str(idUser)
                cur.execute(sql)
                self.conexao.commit()
                return 1
            return 5
        return 0



def UpdateNomeUser(self, idUser, nomeUser):

        cur = self.conexao.cursor()
        sql = 'SELECT * FROM usuario WHERE idUser =' + str(idUser)
        cur.execute(sql)
        consulta = cur.fetchall()

        if (consulta):
            sql = 'UPDATE usuario SET nomeUser = ' + "'" + nomeUser + "'" + " WHERE idUser = " + str(idUser)
            cur.execute(sql)
            self.conexao.commit()
            return 1
        else:
            return 0

def UpdateImagem(self, idUser, imagem):

        cur = self.conexao.cursor()
        sql = 'SELECT * FROM usuario WHERE idUser =' + str(idUser)
        cur.execute(sql)
        consulta = cur.fetchall()

        if (consulta):
            sql = 'UPDATE usuario SET imagem = ' + "'" + imagem + "'" + " WHERE idUser = " + str(idUser)
            cur.execute(sql)
            self.conexao.commit()
            return 1
        else:
            return 0


def UpdateEmailUser(self, idUser, emailUser):

        cur = self.conexao.cursor()
        sql = 'SELECT * FROM usuario WHERE idUser =' + str(idUser)
        cur.execute(sql)
        consulta = cur.fetchall()

        if (consulta):
            if(self.validarEmail(emailUser) == 1):
                sql = 'UPDATE usuario SET emailUser = ' + "'" + emailUser + "'" + " WHERE idUser = " + str(idUser)
                cur.execute(sql)
                self.conexao.commit()
                return 1
            return 2
        return 0


def UpdateContatoUser(self, idUser, contatoUser):

        cur = self.conexao.cursor()
        sql = 'SELECT * FROM usuario WHERE idUser =' + str(idUser)
        cur.execute(sql)
        consulta = cur.fetchall()

        if (consulta):
            if(len(contatoUser) == 11):
                sql = 'UPDATE usuario SET contatoUser = ' + "'" + str(contatoUser) + "'" + " WHERE idUser = " + str(idUser)
                cur.execute(sql)
                self.conexao.commit()
                return 1
            return 4
        return 0


def UpdateCPF(self, idUser, cpfUser):
        cur = self.conexao.cursor()
        sql = 'SELECT cpfUser FROM usuario WHERE idUser =' + str(idUser)
        cur.execute(sql)
        consulta = cur.fetchall()
        if(consulta[0][0] == 'NULL'):
            if(self.validarCpf(cpfUser) == 1):
                sql = 'UPDATE usuario SET cpfUser = ' + "'" + str(cpfUser) + "'" + " WHERE idUser = " + str(idUser)
                cur.execute(sql)
                self.conexao.commit()
                return 1
            return 3
        return 0

def fechar(self):
        self.conexao.close()
"""

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
