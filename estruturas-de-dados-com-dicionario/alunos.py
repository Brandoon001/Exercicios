'''
# Estrutura de dados com dicionarios

1. Criação: Crie um dicionário chamado alunos contendo 3 alunos como chaves e seus respectivos dicionários internos com nome, idade e curso.

    1 - Criar um dicionário alunos com 3 alunos

    2 - cada aluno vai ter dicionários com nome, idade e curso

2. Acesso: Exiba no console o nome e o curso do primeiro aluno do dicionário alunos.

    1 - retorne o nome e o curso do primeiro aluno do dicionário

3. Métodos: Utilize o método .update() para adicionar um novo aluno ao dicionário alunos.

    1 - adicionar novo aluno usando .update()

4. Iteração: Utilize um laço for junto com o método .items() para imprimir cada chave e valor do dicionário alunos no formato: Chave: X - Dados: Y.

    1 - Fazer um laço for

    2 - utilizar o for junto com o método .item()

    3 - retornar cada chave e valor do dicionário alunos no formato: Chave: X - Dados: Y.
'''

Alunos = {"Brandoon": {"Nome": "Brandoon", "Idade": 24, "Curso": "Programador de Sistemas"},
          "Lebron": {"Nome": "Lebron", "Idade": 38, "Curso": "Programador com IA"},
          "Naldo": {"Nome": "Naldo", "Idade": 42, "Curso": "Programador do Futuro"}
          }

primeiro_aluno_nome = Alunos["Brandoon"]["Nome"]
primeiro_aluno_curso = Alunos["Brandoon"]["Curso"]

Aluno = {"Joaquin": {"Nome": "Joaquin", "Idade": 25, "Curso": "Programador de Sistemas"}}
Alunos.update(Aluno)

print(Alunos)
print(f"Nome do primeiro aluno: {primeiro_aluno_nome}")
print(f"Curso do primeiro aluno: {primeiro_aluno_curso}")

for chave, valor in Alunos.items():
    print(f"Chave: {chave} - Dados: {valor}")