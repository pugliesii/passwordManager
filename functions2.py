# Bibliotecas
import customtkinter as ct # Importar a biblioteca com "ct"
import sys # Sistema
import random # Aleatoridade 
import string # Caracteres aleatórios
import pyperclip # Clipboard
from cryptography.fernet import Fernet # Incriptação e descriptação

def ownPassword():
    root = ct.CTk() # Janela 
    root.geometry("400x200") # Tamanho
    root.resizable(False, False) # Não redimensionável 
    root.title("Last Pass") # Título
    root.iconbitmap("favicon.ico") # Ícone


    def transformStr():
        entryPasswordStr = str(entryPassword.get()) # Peguei o Input e transformei em String
            
        fileNameReturn = fileName.get() # "fileNameReturn" recebe o valor de "fileName"
        fileNameReturn = fileNameReturn + ".txt" # "fileNameReturn" recebe o valor de "fileNameReturn" mais a concatenação de ".txt" 

        key = Fernet.generate_key() # Criação da chave
        fernet = Fernet(key) # "fernet" recebe o método Fernet()
        encryptedPasswordUser = fernet.encrypt(entryPasswordStr.encode()) # "encryptedPasswordUser" recebe a senha encriptada

        f = open(fileNameReturn, "w") # "f" recebe o método "open", criando um arquivo com o nome do valor de "fileNameReturn"
        f.write(str(encryptedPasswordUser)) # A variável "encryptedPasswordUser" será escrita dentro do arquivo
        f.close() # Fechamento do arquivo

    def copyPast():
        entryPasswordStr = str(entryPassword.get()) # Variável "entryPasswrodStr" recebe a string do valor de "entryPassword"
        pyperclip.copy(entryPasswordStr) # Fixação de "entryPasswordStr" no clipboard

    ct.CTkLabel(root, text="Type your password").place(x=20, y=20) # Primeiro texto na terceira janela

    fileName = ct.CTkEntry(root, placeholder_text="", width=120,height=10, corner_radius=20) # Input na terceira janela
    fileName.place(x=117,y=93) # Ajuste do Input
    ct.CTkLabel(root, text="Name of the file:").place(x=20, y=90) # Texto na terceira janela

    entryPassword = ct.CTkEntry(root, placeholder_text="", width=200,height=20, 
    corner_radius=20) # Criação de Input na terceira janela

    entryPassword.place(x=20, y=50) # Ajuste de Input na terceira janela
    # Usar .place() na segunda linha para o programa retorna um valor um valor aceitável (str; float; int)
    # Se usar .place() direto no objeto, o programa retorna NoneType

    button = ct.CTkButton(root, text="Copy", corner_radius=20, width=30,height=30, command=copyPast).place(x=20,y=150) # Primeiro botão na terceira janela

    button2 = ct.CTkButton(root, text="Save", corner_radius=20, command=transformStr, width=30,height=30).place(x=100,y=150) # Segundo botão na terceira janela


    root.mainloop() # Condição para rodar esta janela
