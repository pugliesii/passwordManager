# Bibliotecas
import customtkinter as ct # Importar a biblioteca como "ct"
import string # Caracteres aleatórios
import random # Aleatoridade
from functions import askingSize # Arquivo ".py"
from functions2 import ownPassword # Arquivo ".py"
from functions3 import exitFrom # Arquivo ".py"
from functions4 import changeTheme # Arquivo ".py"

root = ct.CTk() # Janela
root.geometry("400x400") # Tamanho
root.resizable(False, False) # Não redimensionável 
root.title("Last Pass") # Título
root.iconbitmap("favicon.ico") # Ícone

label = ct.CTkLabel(root, text="Welcome to\nLast Pass",
width=120, height=40, corner_radius=10,
font=("Times New Roman",30, "bold")).place(x=115, y=20) # Primeiro texto na primeira janela

buttonPC = ct.CTkButton(root, text="Generated password\nby computer",
command=askingSize, width=5, height=25, corner_radius=20).place(x=210, y =120) # Primeiro botão na primeira janela

buttonUser = ct.CTkButton(root, text="Create your\nown password",
corner_radius=20, height=25, width=5, command=ownPassword).place(x=50, y=120) # Segundo botão na primeira janela

switch = ct.CTkSwitch(root,width=20,
height=20,text="", corner_radius=20,
command=changeTheme).place(x=50, y=330) # Switch na primeira janela

buttonExit = ct.CTkButton(root,text="Exit",
width=80,height=25,command=exitFrom, border_color="red", border_width=1).place(x= 270, y=325) # Botão na primeira janela

root.mainloop() # Condição para rodar esta janela