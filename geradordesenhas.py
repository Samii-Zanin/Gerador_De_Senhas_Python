import string
import random
import customtkinter as ctk

def gerar_senha(tamanho, incluir_simbolos=False):
    caracteres = string.ascii_letters + string.digits
    if incluir_simbolos:
        caracteres += string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho)) 
    return senha

def transfomar_em_nmr(nmr):
    try:
        return int(nmr)
    except ValueError:
        return 8
def incluir_simbolos():
    if incluir_smbl.select():
        return True
    else:
        return False
def gerar_senha_click():
    entry_senha.configure(state="normal")
    tamanho = transfomar_em_nmr(entry_tamaho.get())

    incluir_simbolos = incluir_smbl_var.get() == 1

    senha = gerar_senha(tamanho, incluir_simbolos)
    entry_senha.delete(0, ctk.END)
    entry_senha.insert(0, senha)
    entry_senha.configure(state="readonly")
def copiar_senha():
    senha = entry_senha.get()
    janela.clipboard_clear()
    janela.clipboard_append(senha)

ctk.set_appearance_mode('Dark')
janela = ctk.CTk()
janela.geometry("400x300")
janela.title("Gerador de Senha")
janela.resizable(False, False)

label_senha = ctk.CTkLabel(janela, text="Gerador de Senhas", font=("Arial", 24, "bold"))
label_senha.pack(pady=10, padx=10)

entry_senha = ctk.CTkEntry(janela, width=300)
entry_senha.pack(padx=10,pady=10)
entry_senha.configure(state="disabled")

incluir_smbl_var = ctk.IntVar()
incluir_smbl = ctk.CTkCheckBox(janela, text="Incluir Símbolos", fg_color="#9370DB", bg_color="#2E2E2E",variable=incluir_smbl_var, onvalue=1, offvalue=0)
incluir_smbl.pack(pady=10, padx=10)

label_tamanho = ctk.CTkLabel(janela, text="Tamanho da senha", font=("Arial", 24, "bold"))
label_tamanho.pack(pady=10, padx=10)

entry_tamaho = ctk.CTkEntry(janela, width=300)
entry_tamaho.pack(pady=10, padx=10)


botao_copiar = ctk.CTkButton(janela,width=80, height=50, text="Copiar Senha", font=("Arial", 18), fg_color="#9370DB", hover_color="#8A2BE2", command=copiar_senha)
botao_copiar.place(x=30,y=250)

botao_gerar = ctk.CTkButton(janela, width=80, height=50, text="Gerar Senha", font=("Arial", 18),
                            command=gerar_senha_click, fg_color="#9370DB", hover_color="#8A2BE2")
botao_gerar.place(x=230,y=250)

janela.mainloop()
