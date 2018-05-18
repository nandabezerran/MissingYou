import psycopg2
class Usuario(object):

    """
        codigo de retorno
        se:
            retorno == 1 siginifica que a operacao foi realizada com sucesso
            retornO == 0 id nao foi encontrado / ou o cadastro ou exclusao falhou
            retorno == 2 email invalido ou email já cadastrado no sistema
            retorno == 3 cpf invalido
            retorno == 4 contato invalido
            retorno == 5 senha invalida
    """

    conexao = None

    def __init__(self):
        self.conexao = psycopg2.connect(host='missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com', database= 'missingyoudb', user='Missingyouufc', password='missingyouufc2018)')



    def validarCpf(self, cpf):
        if (len(cpf) == 11):
            # Calcular primeiro digito verificador
            sm = 0
            peso = 10
            for i in range(0, 9):
                sm = sm + (int(cpf[i]) * peso)
                peso = peso - 1

            primeiroDigito = 11 - (sm % 11)
            if ((primeiroDigito == 10) or (primeiroDigito == 11)):
                primeiroDigito = 0

            # calculo do segundo digito vefiricado
            sm = 0
            peso = 11
            for i in range(0, 10):
                sm = sm + (int(cpf[i]) * peso)
                peso = peso - 1

            segundoDigito = 11 - (sm % 11)
            if ((segundoDigito == 10) or (segundoDigito == 11)):
                segundoDigito = 0

            if ((primeiroDigito == int(cpf[9])) and (segundoDigito == int(cpf[10]))):
                return 1
            else:
                return 3
        else:
            return 3

    def validarEmail(self, email):
        try:
            indexAroba = email.index('@')
            if (indexAroba > 0):
                indexPonto = email.index(".")
                if (indexPonto - 1 > indexAroba):
                    if (indexPonto + 1 < len(email)):
                        return 1
            return 2
        except:
            return 2


    def validarDados(self, senhaUser, emailUser, contatoUser):

        if(len(contatoUser)!= 11):
            return 4

        if(len(senhaUser)<= 5):
            return 5

        if(self.validarEmail(emailUser) == 2):
            return 2

        return 1

    def validarSenha(self, emailUser, senhaUser):
        cur = self.conexao.cursor()
        sql = 'SELECT * FROM usuario WHERE emailUser =' + "'" + str(emailUser) + "'" + 'and senhaUser=' + "'" + str(senhaUser) + "'"
        cur.execute(sql)
        consulta = cur.fetchall()

        if (consulta):
            return 5
        else:
            return 0



    def cadastrarUsuario(self, idUser, nomeUser, emailUser, cpfUser, contatoUser, senhauser,imagem):

        cur = self.conexao.cursor()
        sql = 'SELECT * FROM usuario WHERE idUser =' + str(idUser)
        cur.execute(sql)
        consulta = cur.fetchall()

        cur = self.conexao.cursor()
        sql2 = 'SELECT * FROM usuario WHERE emailUser = ' + "'" +  str(emailUser) + "'"
        cur.execute(sql2)
        consulta2 = cur.fetchall()

        if(not consulta):
            if( not consulta2):
                if(self.validarDados(senhauser, emailUser, contatoUser) == 1):
                    if(self.validarCpf(cpfUser) == 1 or cpfUser == 'NULL'):
                        sql = "INSERT INTO usuario (idUser, nomeUser, emailUser, cpfUser, contatoUser, senhaUser, imagem ) VALUES" + "(" + str(idUser) + "," + "'"+nomeUser + "'"+ "," + "'"+ emailUser + "'"+"," + "'"+cpfUser + "'"+"," + "'"+  contatoUser + "'" + "," + "'"+ senhauser + "'"+ "," + "'"+imagem + "'" ")"
                        cur.execute(sql)
                        self.conexao.commit()
                        return 1
                    return 3
                return self.validarDados(senhauser, emailUser, contatoUser)
            return 2
        return 0

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

    def selcionarUsuario(self, idUser):

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

