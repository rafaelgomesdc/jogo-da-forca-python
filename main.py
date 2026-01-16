#from game.program import game_loop
from game.verificacao import Verificar_Letra, Tenta_Letra
from game.palavra import Palavra
from data.dtbs import lista_de_palavras as lista
from game.opcoes_dev import opcoes_dev
from game.menu import Menu

def game_loop():
    p = Palavra()
    p.definir_palavra(lista)
    p_tentativa = [] #Palavra com as letras tentadas incluídas
    letras_tentadas = [] #Lista de letras tentadas
    erros = 0

    for l in range(len(p.palavra)):
        p_tentativa.append("_")

    #print(f"Palavra de {len(p.palavra)} letras.")
    #print("_"*len(p.palavra),"\n")

    opcao = Menu(p_tentativa, letras_tentadas, p, erros)

    while opcao > 0 and opcao <= 4  or opcao == 9:
        match opcao:
            case 1:
                erros = Verificar_Letra(Tenta_Letra(letras_tentadas), p_tentativa, p.palavra, erros)
            case 2:
                print("\nDica: ", p.categoria)
            case 3:
                if input("Digite a tentativa: ") == p.palavra:
                    print("Você Acertou!!\n")
                    if int(input("1 = Jogar novamente\n2 = Encerrar\nOpção desejada: ")) == 1:
                        game_loop()
                    else:
                        break
                else:
                    print("Palavra incorreta.")
            case 4:
                break
            case 69:
                opcaoDev = opcoes_dev(p.palavra, p_tentativa, letras_tentadas)
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
                        game_loop()

        if erros >= 6:
            print("\nVocê perdeu!\n")
            if int(input("1 = Jogar novamente\n2 = Encerrar\nOpção desejada: ")) == 1:
                game_loop()
            else:
                break
            

        opcao = Menu(p_tentativa, letras_tentadas, p, erros)

if __name__ == "__main__":
    game_loop()