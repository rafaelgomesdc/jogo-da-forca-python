#FUNCOES
from game.palavra import Palavra
from game.menu import Menu
from game.opcoes import Opcoes

#DADOS
from data.dtbs import lista_de_palavras as lista

def game_loop(): #Loop principal
    p = Palavra()
    p.definir_palavra(lista)
    p_tentativa = [] #Palavra com as letras tentadas incluídas
    letras_tentadas = [] #Lista de letras tentadas
    erros = 0
    dev_mode = False

    for l in range(len(p.palavra)):
        p_tentativa.append("_")

    opcao = Menu(letras_tentadas, p_tentativa, p, erros, dev_mode)

    while opcao > 0 and opcao <= 3  or opcao == 9:
        opcoes = Opcoes(opcao, letras_tentadas, p_tentativa, p, erros)

        match opcoes:
            case "break":
                break
            case "reiniciar":
                game_loop()
            case "erro":
                erros += 1
            case "dev_mode_on":
                dev_mode = True

        opcao = Menu(p_tentativa, letras_tentadas, p, erros, dev_mode)

if __name__ == "__main__":
    game_loop()