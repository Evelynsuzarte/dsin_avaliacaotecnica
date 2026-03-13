class Pato:
    def __init__(self, nome):
        self.nome = nome

    def get_nome(self):
        print("O nome do pato é: ", self.nome)

    def andar(self):
        print(self.nome, "está andando")

    def nadar(self):
        print(self.nome, "está nadando")

    def voar(self):
        print(self.nome, "está voando")

    def grasnar(self):
        print(self.nome, "quack quack!")
    

pato1 = Pato("Robertinho")

# ações do pato
pato1.get_nome()
pato1.andar()
pato1.nadar()
pato1.voar()
pato1.grasnar()


