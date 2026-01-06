#Jogo da forca no terminal
from dtbs import lista_de_palavras as lista
import random

#Últimas mudanças:
#1 - Mudança na aparência da interface

class Palavra:
    palavra = []
    categoria = ""
    popularidade = ""

#Define a palavra
def definirPalavra(ls):
    i = random.randint(0, len(ls))
    print(i)
    p_data = ls[i].split("_")
    p = Palavra()
    p.palavra = p_data[0]
    p.categoria = p_data[1]
    p.popularidade = p_data[2]

    return p

#Opções disponíveis apenas durante o desenvolvimento
def opcDev(palavra, p_tentativa, letras_tentadas):
    print("""
          
    ***OPÇÕES DO DESENVOLVEDOR***
    1 - Mostrar palavra
    2 - Mostrar palavra com letras acertadas
    3 - Mostrar letras tentadas
    4 - Mostrar tudo
    5 - Nova Palavra
          
    """)
    opcao = int(input("Digite a opção desejada: "))
    print("\n")

    return opcao

#Menu principal
def Menu(p_tentativa, letras_tentadas, p):
    print("{:<50} {:<5} {:<50}".format("Letras tentadas", "|", "OPÇÕES"))
    print("{:<50} {:<5} {:<50}".format("".join(letras_tentadas), "|", "1 - Tentar letra"))
    print("{:<50} {:<5} {:<50}".format("", "|", "2 - Dica"))
    print("{:<50} {:<5} {:<50}".format("".join(p_tentativa), "|", "3 - Tentar palavra"))
    print("{:<50} {:<5} {:<50}".format("", "|", "4 - Desistir"))
    print("."*100)

    #print("\nOPÇÕES")
    #print("1 = Tentar Letra\n2 = Dica\n3 = Tentar palavra\n4 = Desistir")

    return int(input("\nDigite a opção desejada: "))

#Recebe a letra da tentativa e verifica se ela é repetida ou não
def TentaLetra(vet_letras):
    letra = input("\nDigite a letra: ").lower()
    repetida = False

    for l in range(len(vet_letras)):
        if vet_letras[l] == letra:
            repetida = True
    
    if repetida == True:
        print("\nLetra repetida.\n")
        print("Tente novamente, outra letra.")
        TentaLetra(vet_letras)
    else:
        vet_letras.append(letra)

    return letra

#
def VerificarLetra(letra, p_tentativa, palavra):
    for l in range(len(palavra)):
        if letra == "a":
            match palavra[l]:
                case "á":
                    p_tentativa[l] = palavra[l]
                case "à":
                    p_tentativa[l] = palavra[l]
                case "ã":
                    p_tentativa[l] = palavra[l]
                case "â":
                    p_tentativa[l] = palavra[l]
                case "a":
                    p_tentativa[l] = palavra[l]
        elif letra == "e":
            match palavra[l]:
                case "é":
                    p_tentativa[l] = palavra[l]
                case "è":
                    p_tentativa[l] = palavra[l]
                case "ê":
                    p_tentativa[l] = palavra[l]
                case "e":
                    p_tentativa[l] = palavra[l]
        elif letra == "i":
            match palavra[l]:
                case "í":
                    p_tentativa[l] = palavra[l]
                case "ì":
                    p_tentativa[l] = palavra[l]
                case "î":
                    p_tentativa[l] = palavra[l]
                case "i":
                    p_tentativa[l] = palavra[l]
        elif letra == "o":
            match palavra[l]:
                case "ó":
                    p_tentativa[l] = palavra[l]
                case "ò":
                    p_tentativa[l] = palavra[l]
                case "õ":
                    p_tentativa[l] = palavra[l]
                case "ô":
                    p_tentativa[l] = palavra[l]
                case "o":
                    p_tentativa[l] = palavra[l]
        elif letra == "u":
            match palavra[l]:
                case "ú":
                    p_tentativa[l] = palavra[l]
                case "ù":
                    p_tentativa[l] = palavra[l]
                case "u":
                    p_tentativa[l] = palavra[l]
        
        p_tentativa[0] = p_tentativa[0].upper()

    print("".join(p_tentativa)) #Exibe a palavra após a tentativa

    print("Passou pela verificação.")

def Main():
    p = definirPalavra(lista)
    p_tentativa = [] #Palavra com as letras tentadas incluídas
    letras_tentadas = [] #Lista de letras tentadas

    for l in range(len(p.palavra)):
        p_tentativa.append("_")

    #print(f"Palavra de {len(p.palavra)} letras.")
    #print("_"*len(p.palavra),"\n")

    opcao = Menu(p_tentativa, letras_tentadas, p)

    while opcao > 0 and opcao <= 4  or opcao == 69:
        match opcao:
            case 1:
                VerificarLetra(TentaLetra(letras_tentadas), p_tentativa, p.palavra)
            case 2:
                print(p.categoria)
            case 3:
                if input("Digite a tentativa: ") == p.palavra:
                    print("Você Acertou!!\n")
                    if int(input("1 = Jogar novamente\n2 = Encerrar\nOpção desejada: ")) == 1:
                        Main()
                    else:
                        break
                else:
                    pass
            case 4:
                break
            case 69:
                opcaoDev = opcDev(p.palavra, p_tentativa, letras_tentadas)
                match opcaoDev:
                    case 1:
                        print("".join(p.palavra))
                    case 2:
                        print("".join(p_tentativa))
                    case 3:
                        print("".join(letras_tentadas))
                    case 4:
                        print("".join(p.palavra), "".join(p_tentativa), "".join(letras_tentadas))
                    case 5:
                        Main()
        opcao = Menu(p_tentativa, letras_tentadas, p)


Main()