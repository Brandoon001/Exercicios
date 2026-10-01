from datetime import datetime

alunos = {}
contador_matricula = 1

while True:

    print("\n==============================")
    print("       SISTEMA DE ALUNOS")
    print("==============================")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar aluno")
    print("4 - Sair")
    print("==============================")

    opcao = input("Escolha uma opção: ")

    match opcao:

      case "1":
          print("\n--- CADASTRO DE ALUNO ---")

          nome = input("Digite o nome do aluno: ")

          aluno = {}

          ano = datetime.now().year
          matricula = f"{ano}{contador_matricula:04d}"

          aluno["matricula"] = matricula
          aluno["nome"] = nome
          aluno["sexo"] = input("Digite o sexo: ")
          aluno["endereco"] = input("Digite o endereço: ")
          aluno["cidade"] = input("Digite a cidade: ")
          aluno["uf"] = input("Digite a UF: ")
          aluno["pai"] = input("Digite o nome do pai: ")
          aluno["mae"] = input("Digite o nome da mãe: ")
          aluno["fone"] = input("Digite o telefone: ")
          aluno["cep"] = input("Digite o CEP: ")
          aluno["rg"] = input("Digite o RG: ")
          aluno["cpf"] = input("Digite o CPF: ")
          aluno["data_nascimento"] = input("Digite a data de nascimento: ")

          alunos[matricula] = aluno

          contador_matricula += 1

          print("\nAluno cadastrado com sucesso!")
          print(f"Matrícula do aluno: {matricula}")

      case "2":
          print("\n--- ALUNOS CADASTRADOS ---")

          if not alunos:
              print("Nenhum aluno cadastrado.")

          else:
              for matricula, dados in alunos.items():

                  print("\n------------------------------")
                  print(f"Matrícula: {dados['matricula']}")
                  print(f"Nome: {dados['nome']}")
                  print(f"Sexo: {dados['sexo']}")
                  print(f"Endereço: {dados['endereco']}")
                  print(f"Cidade: {dados['cidade']}")
                  print(f"UF: {dados['uf']}")
                  print(f"Pai: {dados['pai']}")
                  print(f"Mãe: {dados['mae']}")
                  print(f"Telefone: {dados['fone']}")
                  print(f"CEP: {dados['cep']}")
                  print(f"RG: {dados['rg']}")
                  print(f"CPF: {dados['cpf']}")
                  print(f"Data de nascimento: {dados['data_nascimento']}")

      case "3":
          print("\n--- BUSCAR ALUNO ---")

          matricula_busca = input("Digite a matrícula do aluno: ")

          if matricula_busca in alunos:

              dados = alunos[matricula_busca]

              print("\nAluno encontrado!")
              print("------------------------------")
              print(f"Matrícula: {dados['matricula']}")
              print(f"Nome: {dados['nome']}")
              print(f"Sexo: {dados['sexo']}")
              print(f"Endereço: {dados['endereco']}")
              print(f"Cidade: {dados['cidade']}")
              print(f"UF: {dados['uf']}")
              print(f"Pai: {dados['pai']}")
              print(f"Mãe: {dados['mae']}")
              print(f"Telefone: {dados['fone']}")
              print(f"CEP: {dados['cep']}")
              print(f"RG: {dados['rg']}")
              print(f"CPF: {dados['cpf']}")
              print(f"Data de nascimento: {dados['data_nascimento']}")

          else:
              print("Aluno não encontrado.")

      case "4":
          print("\nSistema encerrado.")
          break

      case _:
          print("\nOpção inválida! Escolha uma opção de 1 a 4.")