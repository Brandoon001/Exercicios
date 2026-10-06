import tkinter as tk
import tkinter.messagebox as messagebox
from pathlib import Path

alunos = {}

def cadastrar_aluno():
    nome = entrada_nome.get()
    sexo = entrada_sexo.get()
    endereco = entrada_endereco.get()
    data_nascimento = entrada_data_nascimento.get()
    rg = entrada_rg.get()

    if cadastrado(rg):
            messagebox.showerror("Erro", "Aluno já cadastrado.")

    aluno = {
          "nome": nome,
          "sexo": sexo,
          "endereco": endereco,
          "data_nascimento": data_nascimento,
          "rg": rg
      }

    alunos[rg] = aluno
    messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")

def cadastrado(rg):
    """Verifica se o aluno já está cadastrado com base no RG.

    Args:
        rg (str): RG do aluno.

    Returns:
        bool: True se o aluno já estiver cadastrado, False caso contrário.
    """
    return rg in alunos
    
    limpar_campos()

def limpar_campos():
    entrada_nome.delete(0, tk.END)
    entrada_sexo.delete(0, tk.END)
    entrada_endereco.delete(0, tk.END)
    entrada_data_nascimento.delete(0, tk.END)
    entrada_rg.delete(0, tk.END)

def sair():
    respota = messagebox.askyesno("Sair", "Deseja realmente sair?")

    if respota:
        janela.destroy()
def menu(opcao):
    match opcao:
        case "1":
            cadastrar_aluno()

        case "2":
            mostrar_alunos()

        case "3":
            sair()

        case _:
            messagebox.showwarning(
                "Opção inválida",
                "Escolha uma opção válida."
            )

janela = tk.Tk()
janela.title("Cadastro de Alunos")
janela.geometry("500x550")
janela.resizable(False, False)


janela.mainloop()