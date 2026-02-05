import unicodedata

def acentuacao_letra(palavra):
    return ''.join(
        c for c in unicodedata.normalize('NFD', palavra)
        if unicodedata.category(c) != 'Mn'
    )

def remove_acentuacao(palavra: str) -> str:
    return ''.join(
        c for c in unicodedata.normalize('NFD', palavra)
        if unicodedata.category(c) != 'Mn'
    )