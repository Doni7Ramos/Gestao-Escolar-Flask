import sqlite3


class Turma:

    def __init__(self, periodo, data_inicio, data_fim, codigo_curso, matricula_professor, alunos):

        self.__codigo = 0

        self.periodo = periodo

        self.data_inicio = data_inicio

        self.data_fim = data_fim

        self.codigo_curso = codigo_curso

        self.matricula_professor = matricula_professor

        self.alunos = alunos

        self.salvar()

    @property
    def codigo(self):

        return self.__codigo

    def salvar(self):

        self.verificaPeriodo()

        conexao = sqlite3.connect("gestao_escolar.db")

        cursor = conexao.cursor()

        sql = f"""
            INSERT INTO
            Turmas (
                periodo,
                data_inicio,
                data_fim,
                codigo_curso,
                matricula_professor
            )
            VALUES (
                '{self.periodo}',
                '{self.data_inicio}',
                '{self.data_fim}',
                '{self.codigo_curso}',
                '{self.matricula_professor}'
            )
        """

        cursor.execute(sql)

        self.__codigo = cursor.lastrowid

        conexao.commit()

        for aluno in self.alunos:

            sql_2 = f"""
                INSERT INTO
                Turmas_alunos (
                    codigo_turma,
                    matricula_aluno
                )
                VALUES (
                    '{self.__codigo}',
                    '{aluno}'
                )
            """

            cursor.execute(sql_2)

            conexao.commit()


        conexao.close()

    def verificaPeriodo(self):

        conexao = sqlite3.connect("gestao_escolar.db")

        cursor = conexao.cursor()
        # Verificando o intervalo entre as datas
        # Se DATA_INICIO e DATA_FIM estiverem entre as datas armazenadas
        # no banco de dados e se tiverem o mesmo periodo e professor, a
        # turma nao é criada
        
        sql = f"""
                SELECT codigo FROM Turmas
                WHERE data_inicio AND data_fim
                BETWEEN '{self.data_inicio}'
                AND '{self.data_fim}'
                AND matricula_professor = '{self.matricula_professor}'
                AND periodo = '{self.periodo}'


            """

        cursor.execute(sql)

        codigo = cursor.fetchall()

        if codigo != []:
            raise ValueError('Professor já está em uma turma nesse periodo')

        conexao.close()

    def __repr__(self):

        return f"Código: {self.codigo}, Periodo: {self.periodo}, Data Inicio: {self.data_inicio}, Data Fim: {self.data_fim}, Código_curso: {self.codigo_curso}, Matricula_professor: {self.matricula_professor}"

    @classmethod
    def listar(cls):

        conexao = sqlite3.connect("gestao_escolar.db")

        cursor = conexao.cursor()

        sql = """
            SELECT tm.codigo, tm.periodo, tm.data_inicio, tm.data_fim, 
            tm.codigo_curso, cs.nome, tm.matricula_professor, pf.nome
            FROM Turmas AS tm
            INNER JOIN Cursos AS cs ON tm.codigo_curso = cs.codigo
            INNER JOIN Professores AS pf ON tm.matricula_professor = pf.matricula
        """
        cursor.execute(sql)

        lista_turmas = cursor.fetchall()

        conexao.close()

        return lista_turmas

    @classmethod
    def listar_alunos(cls, codigo_turma):

        conexao = sqlite3.connect("gestao_escolar.db")

        cursor = conexao.cursor()

        sql = f"""
    	    SELECT al.matricula, al.nome, al.cpf, al.telefone, al.email
            FROM Alunos AS al
            INNER JOIN Turmas_Alunos AS ta on al.matricula = ta.matricula_aluno
            WHERE ta.codigo_turma = '{codigo_turma}'
        """
        cursor.execute(sql)

        lista_alunos = cursor.fetchall()

        conexao.close()

        return lista_alunos
    



if __name__ == '__main__':

    python_caldeira = Turma(
        periodo='Tarde',
        data_inicio='2022-07-01',
        data_fim='2022-07-31',
        codigo_curso='1',
        matricula_professor='6'
    )

    print(python_caldeira)