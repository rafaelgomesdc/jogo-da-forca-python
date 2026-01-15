import random

class Palavra:
    palavra = []
    categoria = ""
    popularidade = ""

    def definir_palavra(self, ls):
        i = random.randint(0, len(ls))
        print(i)
        p_data = ls[i].split("_")
        self.palavra = p_data[0]
        self.categoria = p_data[1]
        self.popularidade = p_data[2]