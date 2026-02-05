#FUNCOES
from game.verificacao import Verificar_Letra, Tenta_Letra
from game.opcoes_dev import Menu_Dev
from game.verificacao_palavra import Verificar_Palavra
import time

def Opcoes(opcao, letras_tentadas, p_tentativa, p, erros):
    erro = False

    match opcao:
            case 1:
                erro = Verificar_Letra(Tenta_Letra(letras_tentadas), p_tentativa, p.palavra)
            case 2:
                match Verificar_Palavra(input("Digite a tentativa: "), p.palavra):
                    case "acertou_reiniciar":
                        return "reiniciar" #Atencao
                    case "acertou_finalizar":
                        return "break" #Atencao
                    case "errou":
                        print("\nPalavra incorreta.")
                        time.sleep(2)
            case 3:
                return "break" #Atencao
            case 9:
                opcaoDev = Menu_Dev()
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
                        return "reiniciar" #Atencao
                return "dev_mode_on"
                    
    if erros >= 6:
            print("\nVocê perdeu!\n")
            if int(input("1 = Jogar novamente\n2 = Encerrar\nOpção desejada: ")) == 1:
                return "reiniciar"
            else:
                return "break"
            
    if erro == True:
        return "erro"
    else:
        pass