import unicodedata

def Tenta_Letra(vet_letras):
    letra = input("\nDigite a letra: ").lower()
    repetida = False

    for l in range(len(vet_letras)):
        if vet_letras[l] == letra:
            repetida = True
    
    if repetida == True:
        print("\nLetra repetida.\n")
        print("Tente novamente, outra letra.")
        Tenta_Letra(vet_letras)
    else:
        vet_letras.append(letra)

    return letra

def acentuacao(palavra):
    return ''.join(
        c for c in unicodedata.normalize('NFD', palavra)
        if unicodedata.category(c) != 'Mn'
    )

def Verificar_Letra(letra, p_tentativa, palavra):
    erro = True

    for l in range(len(palavra)):    
        if letra == acentuacao(palavra[l]):
            p_tentativa[l] = palavra[l]
            erro = False
        
        p_tentativa[0] = p_tentativa[0].upper()
        
    return erro