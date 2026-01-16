def opcoes_dev(palavra, p_tentativa, letras_tentadas):
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