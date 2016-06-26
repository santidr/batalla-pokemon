#!/usr/bin/python3
# -*- coding: utf-8 -*-

from Modelos import pokemon
import random

Pokemon = pokemon.Pokemon

pikachu = Pokemon("pikachu", 100, 25)
charmandel = Pokemon("charmandel", 100, 22)

while (pikachu.vida > 0 and charmandel.vida > 0):
    turno = random.randint(0, 10)

    if (turno % 2 == 0):  # Numero par, turno de pikachu para atacar
        pikachu.Atacar(charmandel)
        print("¡Picachu ataca!")
    else:
        charmandel.Atacar(pikachu)
        print("¡Charmandel ataca!")

    print("Vida de pikachu: {0}".format(pikachu.vida),
          "\nVida de charmandel: {0}".format(charmandel.vida),
          "\n------------------------")

    input("Presiona una tecla...\n")

# Determinar el vencedor de la batalla
if (pikachu.vida > 0):
    pikachu.Celebrar()
else:
    charmandel.Celebrar()
