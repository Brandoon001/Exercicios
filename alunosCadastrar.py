import tkinter
import tkinter.messagebox

alunos = {}

def listar_alunos():
  print("Alunos cadastrados:")
  for nome, (matricula, idade, sexo, cep, endereco, cidade, uf, mae, pai, fone, cpf, rg, data_nascimento) in alunos.items():
    print(f"Nome: {nome}, Idade: {idade}, Sexo: {sexo}")
  

def buscar_aluno():
  nome = input("Digite o nome do aluno que deseja buscar: ")
  if nome in alunos:
    matricula, idade, sexo, cep, endereco, cidade, uf, mae, pai, fone, cpf, rg, data_nascimento = alunos[nome]
    print(f"Aluno encontrado! Nome: {nome}, Idade: {idade}, Sexo: {sexo}")
  else:
    print("Aluno não encontrado.")

match input("Escolha uma opção:\n1 - Cadastrar Aluno\n2 - Listar Alunos\n3 - Buscar Aluno\n4 - Sair\n"):
  case "1":
    cadastrar_aluno()
  case "2":
    listar_alunos()
  case "3":
    buscar_aluno()
  case "4":
    print("Saindo...")
    break
  case _:
    print("Opção inválida.")

janela = tkinter.Tk()
janela.title("Sistema de Alunos")

entrada_nome = tkinter.Entry(janela)
entrada_nome.pack()

label_nome = tkinter.Label(janela, text="Nome do Aluno")
label_nome.pack()

label_idade = tkinter.Label(janela, text="Idade do Aluno")
label_idade.pack()

label_sexo = tkinter.Label(janela, text="Sexo do Aluno")
label_sexo.pack()

label_cep = tkinter.Label(janela, text="CEP do Aluno")
label_cep.pack()

label_endereco = tkinter.Label(janela, text="Endereço do Aluno")
label_endereco.pack()

label_cidade = tkinter.Label(janela, text="Cidade do Aluno")
label_cidade.pack()

label_uf = tkinter.Label(janela, text="UF do Aluno")
label_uf.pack()

label_mae = tkinter.Label(janela, text="Nome da Mãe do Aluno")
label_mae.pack()

label_pai = tkinter.Label(janela, text="Nome do Pai do Aluno")
label_pai.pack()

label_fone = tkinter.Label(janela, text="Telefone do Aluno")
label_fone.pack()

label_cpf = tkinter.Label(janela, text="CPF do Aluno")
label_cpf.pack()

label_rg = tkinter.Label(janela, text="RG do Aluno")
label_rg.pack()

label_data_nascimento = tkinter.Label(janela, text="Data de Nascimento do Aluno")
label_data_nascimento.pack()

label_matricula = tkinter.Label(janela, text="Matrícula do Aluno")
label_matricula.pack()

botao_cadastrar = tkinter.Button(janela, text="Cadastrar Aluno", command=cadastrar_aluno)
botao_cadastrar.pack()

botao_listar = tkinter.Button(janela, text="Listar Alunos", command=listar_alunos)
botao_listar.pack()

botao_buscar = tkinter.Button(janela, text="Buscar Aluno", command=buscar_aluno)
botao_buscar.pack()

botao_sair = tkinter.Button(janela, text="Sair", command=janela.quit)
botao_sair.pack()

janela.mainloop()