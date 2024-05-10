import re

def validar_cpf(cpf: str) -> bool:
    """
    Valida um número de CPF.

    Parâmetros:
        cpf (str): Número de CPF a ser validado. Pode conter caracteres não numéricos.

    Retorna:
        bool: True se o CPF for válido, False caso contrário.

    Descrição:
        Esta função verifica se um número de CPF é válido de acordo com as regras de validação brasileiras.
        O CPF pode ser fornecido com ou sem formatação (por exemplo, '123.456.789-00' ou '12345678900').

    Exemplo de Uso:
        >>> validar_cpf('123.456.789-09')
        True
        >>> validar_cpf('12345678909')
        True
        >>> validar_cpf('000.000.000-00')
        False
    """
    # Remover todos os caracteres que não são dígitos
    cpf = re.sub(r'[^0-9]', '', cpf)

    # Verificar se o CPF tem 11 dígitos após a remoção dos caracteres especiais
    if len(cpf) != 11:
        return False

    # Verificar se todos os dígitos são iguais (CPF inválido)
    if cpf == cpf[0] * 11:
        return False

    # Validar o CPF usando o algoritmo específico
    soma = 0
    peso = 10
    for index in range(9):
        soma += int(cpf[index]) * peso
        peso -= 1

    resto = soma % 11
    digito_verificador1 = 0 if resto < 2 else 11 - resto

    soma = 0
    peso = 11
    for index in range(10):
        soma += int(cpf[index]) * peso
        peso -= 1

    resto = soma % 11
    digito_verificador2 = 0 if resto < 2 else 11 - resto

    if int(cpf[9]) != digito_verificador1 or int(cpf[10]) != digito_verificador2:
        return False

    return cpf
