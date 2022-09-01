from flask import Flask, render_template, request, redirect, url_for

from aluno import Aluno
from professor import Professor
from curso import Curso

app = Flask (__name__)

@app.route ("/")
def index ():

    return render_template ("index.html")

# Rotas para Alunos
@app.route ("/cadastro/alunos", methods=('GET', 'POST'))
def cadastro_alunos():

    if request.method == 'POST':

        nome = request.form['txt_nome']

        cpf = request.form['txt_cpf']

        telefone = request.form['txt_telefone']

        email = request.form['txt_email']

        Aluno(nome=nome, cpf=cpf, telefone=telefone, email=email)

        return redirect (url_for('listar_alunos') )

    return render_template ("cadastro_alunos.html")

@app.route ("/listar/alunos")
def listar_alunos():

    alunos = Aluno.listar()

    return render_template ("listar_alunos.html", alunos=alunos)

@app.route ("/editar/aluno/<matricula>", methods=('GET','POST'))
def editar_aluno(matricula):

    aluno = Aluno.listarAlunoMatricula (matricula)

    if request.method == 'POST':

        nome = request.form['txt_nome']

        cpf = request.form['txt_cpf']

        telefone = request.form['txt_telefone']

        email = request.form['txt_email']

        Aluno.atualizar(matricula=matricula, nome=nome, cpf=cpf, telefone=telefone, email=email)

        return redirect(url_for('listar_alunos'))
    

    return render_template("editar_aluno.html", aluno=aluno)

#Rotas para Professores

@app.route ("/listar/professores")
def listar_professores():

    professores = Professor.listar()

    return render_template ("listar_professores.html", professores=professores)

@app.route ("/cadastro/professores", methods=('GET', 'POST'))
def cadastro_professores():

    if request.method == 'POST':

        nome = request.form['nome_professor']

        cpf = request.form['txt_cpf']

        telefone = request.form['txt_telefone']

        email = request.form['txt_email']

        formacao = request.form['txt_formacao']

        especialidade = request.form['txt_especialidade']

        Professor(nome=nome, cpf=cpf, telefone=telefone, email=email, formacao=formacao, especialidade=especialidade)

        return redirect (url_for('listar_professores') )

    return render_template ("cadastro_professores.html")

@app.route ("/editar/professor/<matricula>", methods=('GET','POST'))
def editar_profesor(matricula):

    professor = Professor.listaProfessorMatricula (matricula = matricula)

    if request.method == 'POST':

        nome = request.form['nome_professor']

        cpf = request.form['txt_cpf']

        ativo = 0
        if 'txt_ativo' in request.form:
            ativo = 1

        telefone = request.form['txt_telefone']

        email = request.form['txt_email']

        formacao = request.form['txt_formacao']

        especialidade = request.form['txt_especialidade']

        Professor.atualizar(matricula=matricula, nome=nome, cpf=cpf, ativo=ativo, telefone=telefone, email=email, formacao=formacao, especialidade=especialidade)

        return redirect(url_for('listar_professores'))
    

    return render_template("editar_professor.html", professor=professor)

# Rotas para Cursos

@app.route ("/listar/cursos")
def listar_cursos():

    cursos = Curso.listar()

    return render_template ("listar_cursos.html", cursos=cursos)

@app.route ("/cadastro/cursos", methods=('GET', 'POST'))
def cadastro_cursos():

    if request.method == 'POST':

        nome = request.form['nome_curso']

        classificacao = request.form['txt_classificacao']

        descricao = request.form['txt_descricao']

        

        Curso(nome=nome, classificacao=classificacao, descricao=descricao)

        return redirect (url_for('listar_cursos') )

    return render_template ("cadastro_cursos.html")
    
@app.route ("/editar/curso/<codigo>", methods=('GET','POST'))
def editar_curso(codigo):

    curso = Curso.listarCursoCodigo(codigo = codigo)

    if request.method == 'POST':

        nome = request.form['nome_curso']

        classificacao = request.form['txt_classificacao']

        ativo = 0
        if 'txt_ativo' in request.form:
            ativo = 1

        descricao = request.form['txt_descricao']


        Curso.atualizar(codigo=codigo, nome=nome, classificacao=classificacao, ativo=ativo, descricao=descricao)

        return redirect(url_for('listar_cursos'))
    

    return render_template("editar_curso.html", curso=curso)