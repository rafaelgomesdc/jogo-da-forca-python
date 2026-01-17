import os

def Menu(p_tentativa, letras_tentadas, p, erros, dev_mode):
    if dev_mode == False:
        Clear()
    else:
        pass

    print("."*100, "\n")
    print("{:<40} {:<5} {:<50}".format(f"Dica: {p.categoria}", "|", "OPÇÕES"))
    print("{:<40} {:<5} {:<50}".format("", "|", ""))
    print("{:<40} {:<5} {:<50}".format("Letras tentadas", "|", "1 - Tentar letra"))
    print("{:<40} {:<5} {:<50}".format(f"Erros: {erros}", "|", "2 - Tentar palavra"))
    print("{:<40} {:<5} {:<50}".format("".join(letras_tentadas), "|", "3 - Desistir"))
    print("{:<40} {:<5} {:<50}".format("".join(p_tentativa), "|", ""))
    print("."*100)

    return int(input("\nDigite a opção desejada: "))

def Clear():
    os.system("cls" if os.name == "nt" else "clear")