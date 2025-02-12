import re  # Importa o módulo re

def is_valid_credit_card(card_number):  # Define a função is_valid_credit_card
    card_number = re.sub(r'\D', '', card_number)  # Remove caracteres não numéricos
    n_digits = len(card_number)  # Calcula o número de dígitos
    n_sum = 0  # Inicializa a soma (n_sum)
    is_second = False  # Inicializa a flag is_second

    for i in range(n_digits - 1, -1, -1):  # Itera sobre os dígitos do número do cartão
        d = int(card_number[i])

        if is_second:  # Converte o dígito para um número inteiro
            d *= 2
            if d > 9:
                d -= 9

        n_sum += d  # Acumula o valor do dígito
        is_second = not is_second  # Alterna a flag is_second

    return n_sum % 10 == 0  # Verifica a validade do cartão
