class ConexaoBD():

    import pymysql.cursors
    import pymysql.connections

    host='localhost'
    database='financeiro'
    user='root'
    password=''

    def __init__(self, host=host, user=user, pwd=password, bd=database):
        self.host = host
        self.user = user
        self.pwd  = pwd
        self.bd   = bd

    def conecta(self):
        self.conexao = self.pymysql.connect (host = self.host, user = self.user, password = self.pwd, database  = self.bd)
        self.cursor = self.conexao.cursor()

    def desconecta(self):
        self.conexao.close()

    def executa_DQL(self, sql):
        self.conecta()
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        self.desconecta()
        return result

    def executa_DML(self, sql):
        self.conecta()
        self.cursor.execute(sql)
        self.conexao.commit()
        self.desconecta()