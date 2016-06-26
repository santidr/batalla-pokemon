class Pokemon:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque

    def Atacar(self, rival):
        rival.vida = rival.vida - self.ataque;

    def Celebrar(self):
        print("*** ¡{0} es el ganador de la batalla! ***".format(self.nombre))
