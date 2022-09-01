import sqlite3

class Curso:

    def __init__ (self, nome, classificacao, descricao):

        self.nome = nome
        self.classificacao = classificacao
        self.descricao = descricao

        self.salvar()

    @property
    def codigo (self):

        return self.__codigo
    
    @classmethod
    def listar(cls):

        conexao = sqlite3.connect("gestao_escolar.db")

        cursor = conexao.cursor()

        sql = """
            SELECT *
            FROM Cursos
            ORDER BY nome
        """
        cursor.execute(sql)

        lista_cursos = cursor.fetchall()

        conexao.close()

        return lista_cursos

    @classmethod
    def listarCursoCodigo(cls, codigo):

            # Abrindo conexao
            conexao = sqlite3.connect("gestao_escolar.db")

            # Utilizando o metodo cursor para fazer
            # alguma ação no banco de dados
            cursor = conexao.cursor()

            sql = f"""
                SELECT * FROM Cursos WHERE codigo = '{codigo}'
            """
            # Executando a ação
            cursor.execute(sql)

            # Lista de aluno recuperado do banco de dados
            listaCurso = cursor.fetchone()

            # Fechando a conexão com o banco de dados
            conexao.close()

            return listaCurso

    @classmethod
    def atualizar(cls, codigo, nome, classificacao, ativo, descricao):
        # Habilitando a conexão com o banco de dados
        # Metodo poara abrir a conexao
        conexao = sqlite3.connect("gestao_escolar.db")

        # Utilizando o metodo cursor para fazer
        # alguma ação no banco de dados
        cursor = conexao.cursor()

        sql = f"""
            UPDATE Cursos SET
            nome = '{nome}',
            classificacao = '{classificacao}',
            ativo = '{ativo}',
            descricao = '{descricao}'
            WHERE codigo = '{codigo}'
        """
        # Executando a ação
        cursor.execute(sql)

        # Salvando a alteração da tabela (confrima)
        conexao.commit()

        # Fechando a conexão com o banco de dados
        conexao.close()

        
    def salvar(self):

        conexao = sqlite3.connect ("gestao_escolar.db")

        cursor = conexao.cursor()

        sql = f"""
            INSERT INTO Cursos (
                nome,
                classificacao,
                descricao
            )
            VALUES
            (
                '{self.nome}',
                '{self.classificacao}',
                '{self.descricao}'
            )
            """

        cursor.execute(sql)

        self.__codigo = cursor.lastrowid

        conexao.commit()

        conexao.close()

    def __repr__ (self):

        return f"Codigo: {self.__codigo},Nome: {self.nome}, Classificação: {self.classificacao}, Descrição: {self.descricao}"

if __name__ == '__main__':

    print( Curso.listar() )