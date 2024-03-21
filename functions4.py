import customtkinter as ct # Importar a biblioteca como "ct"

switchCheck = True # Variável recebe valor booleano ("True")

def changeTheme():
    global switchCheck # Variável com escopo global
    if switchCheck:
        ct.set_appearance_mode("light") # Mudar a aparência para claro
        switchCheck = False # Variável recebe um novo valor booleano ("False")
    else:
        ct.set_appearance_mode("dark") # Mudar a aparência para escuro
        switchCheck = True # Variável recebe um novo valor booelano ("True")