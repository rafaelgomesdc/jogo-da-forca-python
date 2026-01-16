

def Opcoes(opcao, Verificar_Letra, Tenta_Letra, letras_tentadas, p_tentativa, p, erros):
    match opcao:
            case 1:
                erros = Verificar_Letra(Tenta_Letra(letras_tentadas), p_tentativa, p.palavra, erros)
            case 2:
                print("\nDica: ", p.categoria)
            case 3:
                if input("Digite a tentativa: ") == p.palavra:
                    print("Você Acertou!!\n")
                    if int(input("1 = Jogar novamente\n2 = Encerrar\nOpção desejada: ")) == 1:
                        game_loop() #Atencao
                    else:
                        break #Atencao
                else:
                    print("Palavra incorreta.")
            case 4:
                break #Atencao
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
                        game_loop() #Atencao