# Bibliotecas
import random # Aleatoridade
import string # Caracteres aleatórios
import customtkinter as ct # Importar a biblioteca como "ct"
import sys # Sistema
import numbers # Números
import pyperclip # Clipboard
from cryptography.fernet import Fernet # Incriptação e descriptação
import os


def askingSize():
    root = ct.CTk() # Janela
    root.geometry("300x300") # Tamanho 
    root.resizable(False, False) # Não redimensionável
    root.title("Last Pass") # Título
    root.iconbitmap("favicon.ico") # Ícone

    def sliderValue(sliderNew): # Parâmetro para o valor do slide ser guardado
        labelValue.configure(root, text=int(sliderNew)) # Texto para exibir o inteiro do valor do slide
        global passwordPC # Declaração de variável global
        passwordPC = int(sliderNew) # "PasswordPC" recebe o inteiro de "SliderNew"


    # Variáveis para definir se os botões foram clicados:
    checkboxCheckUpper = ct.StringVar(value="off") # Retorna o valor "on" ou "off", nesse caso: "off"
    checkboxCheckLower = ct.StringVar(value="off") # Retorna o valor "on" ou "off", nesse caso: "off"
    checkboxCheckDigits = ct.StringVar(value="off") # Retorna o valor "on" ou "off", nesse caso: "off"
    checkboxCheckEspecial = ct.StringVar(value="off") # Retorna o valor "on" ou "off", nesse caso: "off"


    slider = ct.CTkSlider(root, from_=0, to=30, command=sliderValue,
    number_of_steps=30) # Slide na segunda janela
    slider.place(x=50, y=80) # Ajuste do Slide
    slider.set(0) # Slide com valor 0
    # Usar .place() na segunda linha para o programa retornar um valor aceitável (str; float; int)
    # Se o usar .place() direto no objeto, o programa retorna NoneType

    labelAsking = ct.CTkLabel(root, text="What's the size\nof the password?",
    width=60, height=40, corner_radius=10,
    font=("Times New Roman",20, "bold")) # Texto na segunda janela
    labelAsking.place(x=70, y=20) # Ajuste do texto

    labelValue = ct.CTkLabel(root, text="") # Segundo texto na segunda janela
    labelValue.place(x=140, y=105) # Ajusto de segundo texto na segunda janela

    ct.CTkCheckBox(root, text="Upper", variable=checkboxCheckUpper, onvalue="on", offvalue="off").place(x=20,y=140) # Primeiro botão checkbox na segunda janela
    ct.CTkCheckBox(root, text="Lower", variable=checkboxCheckLower, onvalue="on", offvalue="off").place(x=20,y=165) # Segundo botão checkbox na segunda janela
    ct.CTkCheckBox(root, text="Digits", variable=checkboxCheckDigits, onvalue="on", offvalue="off").place(x=20,y=190) # Terceiro botão checkbox na terceira janela
    ct.CTkCheckBox(root, text="Especial", variable=checkboxCheckEspecial, onvalue="on", offvalue="off").place(x=20,y=215) # Quarto botão checkbox na quarta janela


    def value(): # Outra janela dentro da segunda janela:


        # Verificacão se os botões foram apertados
        # Pegando o valor de cada botão checkbox com o método ".get()" e verificando se ele é igual a "on", ou seja, se o botão foi clicado
        if checkboxCheckLower.get() == "on" and checkboxCheckUpper.get() == "on" and checkboxCheckDigits.get() == "on" and checkboxCheckEspecial.get() == "on":
            passwordComputer = "".join(random.choices(string.ascii_letters+string.digits+string.punctuation, k=passwordPC))
        elif checkboxCheckUpper.get() == "on" and checkboxCheckLower.get() == "on" and checkboxCheckDigits.get() == "on":
            passwordComputer = "".join(random.choices(string.ascii_letters+string.digits, k=passwordPC))
        elif checkboxCheckUpper.get() == "on" and checkboxCheckLower.get() == "on" and checkboxCheckEspecial.get() == "on":
            passwordComputer = "".join(random.choices(string.ascii_letters+string.punctuation, k=passwordPC))
        elif checkboxCheckUpper.get() == "on" and checkboxCheckDigits.get() == "on" and checkboxCheckEspecial.get() == "on":
            passwordComputer = "".join(random.choices(string.ascii_uppercase+string.digits+string.punctuation, k=passwordPC))
        elif checkboxCheckUpper.get() == "on" and checkboxCheckDigits.get() == "on":
            passwordComputer = "".join(random.choices(string.ascii_uppercase+string.digits, k=passwordPC))
        elif checkboxCheckUpper.get() == "on" and checkboxCheckEspecial.get() == "on":
            passwordComputer = "".join(random.choices(string.ascii_uppercase+string.punctuation, k=passwordPC))
        elif checkboxCheckUpper.get() == "on" and checkboxCheckLower.get() == "on":
            passwordComputer = "".join(random.choices(string.ascii_letters, k=passwordPC))
        elif checkboxCheckUpper.get() == "on":
            passwordComputer = "".join(random.choices(string.ascii_uppercase, k=passwordPC))
        elif checkboxCheckLower.get() == "on" and checkboxCheckDigits.get() == "on" and checkboxCheckEspecial.get() == "on":
            passwordComputer = "".join(random.choices(string.ascii_lowercase+string.digits+string.punctuation, k=passwordPC))
        elif checkboxCheckLower.get() == "on" and checkboxCheckEspecial.get() == "on":
            passwordComputer = "".join(random.choices(string.ascii_lowercase+string.punctuation, k=passwordPC))
        elif checkboxCheckLower.get() == "on" and checkboxCheckDigits.get() == "on":
            passwordComputer = "".join(random.choices(string.ascii_lowercase+string.digits, k=passwordPC))
        elif checkboxCheckLower.get() == "on":
            passwordComputer = "".join(random.choices(string.ascii_lowercase, k=passwordPC))
        elif checkboxCheckDigits.get() == "on" and checkboxCheckEspecial.get() == "on":
            passwordComputer = "".join(random.choices(string.digits+string.punctuation, k=passwordPC))
        elif checkboxCheckDigits.get() == "on":
            passwordComputer = "".join(random.choices(string.digits, k=passwordPC))
        elif checkboxCheckEspecial.get() == "on":
            passwordComputer = "".join(random.choices(string.punctuation, k=passwordPC))
        else:
            sys.exit() # Caso nenhum deles for apertado, feche o programa
        # Verificação completa dos botões

        def copyPast():
            pyperclip.copy(passwordComputer) # Copia o conteúdo da variável "passwordComputer"

        def toString():
            fileNameReturn = fileName.get() # Pega o valor de "fileName" e retorna o valor dela dentro de "fileNameReturn"
            fileNameReturn = fileNameReturn + ".txt" # "fileNameReturn" recebe o valor original com o ".txt" no final

            f = open(fileNameReturn, "w") # "f" recebe o método "open", criando um arquivo com o valor de "fileNameReturn"
            f.write(str(encryptedPasswordPC)) # A variável "encryptedPasswordPC" será escrita dentro do arquivo
            f.close() # Fechamento do arquivo

        root2 = ct.CTk() # Janela
        root2.resizable(False, False) # Não redimensionável
        root2.title("LastPass") # Título
        root2.iconbitmap("favicon.ico") # Ícone
        root2.geometry("400x200") # Tamanho

        ct.CTkLabel(root2, text=f"That's your password:\n{passwordComputer}",
        font=("Times New Roman", 20, "bold")).place(x=20,y=10) # Texto na segunda janela

        ct.CTkButton(root2, text="copy",corner_radius=20, command=copyPast, width=30, height=30).place(x=20, y=140) # Primeiro botão na segunda janela

        fileName = ct.CTkEntry(root2,placeholder_text="", width=120, height=10, corner_radius=20) # Input na segunda janela

        ct.CTkLabel(root2, text="Name of the file:").place(x=20, y=80) # Segundo texto na segunda janela

        fileName.place(x=120, y=83) # Ajuste do texto

        ct.CTkButton(root2, text="Save",width=30, height=30, corner_radius=20,command=toString).place(x=100,y=140) # Segundo botão na segunda janela

        key = Fernet.generate_key() # Gera uma chave para a encriptação
        fernet = Fernet(key) # Criando uma variável para facilitar
        encryptedPasswordPC = fernet.encrypt(passwordComputer.encode()) # Utilizando "encrypt()" para encriptar, e "encode()" para compilar
        decryptedPasswordPC = fernet.decrypt(encryptedPasswordPC).decode()

        root2.mainloop() # Condição para rodar esta janela


    button = ct.CTkButton(root, text="Submit", corner_radius=20,
    height=25, width=5, command=value).place(x=117, y=265) # Botão na segunda janela
    root.mainloop() # Condição para rodar esta janela