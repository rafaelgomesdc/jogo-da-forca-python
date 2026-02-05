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
        """
        if letra == "a":
            match palavra[l]:
                case "á":
                    p_tentativa[l] = palavra[l]
                    erro = False
                case "à":
                    p_tentativa[l] = palavra[l]
                    erro = False
                case "ã":
                    p_tentativa[l] = palavra[l]
                    erro = False
                case "â":
                    p_tentativa[l] = palavra[l]
                    erro = False
                #case "a":
                #    p_tentativa[l] = palavra[l]
                #erro = False
        elif letra == "e":
            match palavra[l]:
                case "é":
                    p_tentativa[l] = palavra[l]
                    erro = False
                case "è":
                    p_tentativa[l] = palavra[l]
                    erro = False
                case "ê":
                    p_tentativa[l] = palavra[l]
                    erro = False
                #case "e":
                #    p_tentativa[l] = palavra[l]
                #erro = False
        elif letra == "i":
            match palavra[l]:
                case "í":
                    p_tentativa[l] = palavra[l]
                    erro = False
                case "ì":
                    p_tentativa[l] = palavra[l]
                    erro = False
                case "î":
                    p_tentativa[l] = palavra[l]
                    erro = False
                #case "i":
                #    p_tentativa[l] = palavra[l]
                #erro = False
        elif letra == "o":
            match palavra[l]:
                case "ó":
                    p_tentativa[l] = palavra[l]
                    erro = False
                case "ò":
                    p_tentativa[l] = palavra[l]
                    erro = False
                case "õ":
                    p_tentativa[l] = palavra[l]
                    erro = False
                case "ô":
                    p_tentativa[l] = palavra[l]
                    erro = False
                #case "o":
                #    p_tentativa[l] = palavra[l]
                #erro = False
        elif letra == "u":
            match palavra[l]:
                case "ú":
                    p_tentativa[l] = palavra[l]
                    erro = False
                case "ù":
                    p_tentativa[l] = palavra[l]
                    erro = False
                #case "u":
                #    p_tentativa[l] = palavra[l]
        """
        
        if letra == acentuacao(palavra[l]):
            p_tentativa[l] = letra
            erro = False
        
        p_tentativa[0] = p_tentativa[0].upper()
        
    return erro