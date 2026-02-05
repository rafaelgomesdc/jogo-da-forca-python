from game.utils import remove_acentuacao

def Verificar_Palavra(tentativa_palavra, palavra_correta):
    if remove_acentuacao(tentativa_palavra) == remove_acentuacao(palavra_correta):
        print("\nVocê acertou!!")
        print("\n1 - Novo jogo\n2 - Encerrar jogo")
        match int(input("Digite a opção desejada: ")):
            case 1:
                return "acertou_reiniciar"
            case 2:
                return "acertou_finalizar"
    else:
        return "errou"