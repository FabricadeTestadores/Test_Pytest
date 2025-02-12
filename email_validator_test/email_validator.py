import re                                                           #Importa o módulo re

def is_valid_email(email):                                          #Define a Função is_valid_email
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'     #Define a Expressão Regular
    return re.match(regex, email) is not None                       #Verifica a Correspondência do Padrão
