import re
from unidecode import unidecode

def substituir_caracteres_especiais(nome):
    # Substitui caracteres acentuados por caracteres normais
    nome_sem_acentos = unidecode(nome)
    # Substitui todos os caracteres não alfanuméricos (exceto espaços) por um traço (-)
    nome_substituido = re.sub(r'[^a-zA-Z0-9\s]', '-', nome_sem_acentos)
    return nome_substituido
