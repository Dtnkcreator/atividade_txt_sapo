class Sapo:
    def __init__(self, nome_s, idade_s, olho_s):
        self.nome = nome_s
        self.idade = idade_s
        self.olho = olho_s

    def __repr__(self):
        return f"Sapo = Nome: {self.nome}, Idade: {self.idade}, Cor do olho: {self.olho}"