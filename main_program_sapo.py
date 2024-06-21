from sapo_class import Sapo
def ler_sapao():
    with open ("sapo.txt", 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("Sapo*"):
                atributos = line.split("Sapo*")[1]
                nome = atributos.split("*")[1]
                idade = atributos.split("*")[3]
                olho = atributos.split("*")[5]
                sapo1 = Sapo(nome,idade,olho)
                return sapo1

sapo = ler_sapao()
print(sapo)