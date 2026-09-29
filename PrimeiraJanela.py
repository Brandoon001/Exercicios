import tkinter as tk

janela = tk.Tk()
janela.title("Primeira Janela")
janela.geometry("400x300")
janela.configure(bg="lightblue")

label = tk.Label(janela,
        text="Bem vindo a minha primeira janela!",
        font=("Arial", 16), bg="lightblue",
        fg="black")

label.grid(row=0, column=0, padx=35, pady=50)

def on_button_click():
    print("O botão foi clicado!")
    label2.config(text="Você clicou no botão!")
    
button = tk.Button(janela,
        text="Clique Aqui", command=on_button_click, activebackground="yellow")

button.grid(row=1, column=0, pady=20)

label2 = tk.Label(janela,
        text="", font=("Arial", 12), bg="lightblue", fg="black")

label2.grid(row=2, column=0, pady=20)

janela.mainloop()