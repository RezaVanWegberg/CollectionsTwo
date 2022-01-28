from cgitb import lookup
from operator import truediv
from os import name
import random

a = True

NamenDeelnemers = []
Lootjes = []


while True:
    VraagNamen = input("Vul de namen in van de deelnemers. 'N' to stop  :")
    if VraagNamen != "N":
        if VraagNamen in NamenDeelnemers:
            print("deze deelnemer zit er al in")
        else:
            NamenDeelnemers.append(VraagNamen)
            Lootjes.append(VraagNamen)
    else:
        break

random.shuffle(NamenDeelnemers)
random.shuffle(Lootjes)

if len(NamenDeelnemers) > 2:
    while a == True:
        for x in range(len(NamenDeelnemers)):
            if NamenDeelnemers[x] == Lootjes[x]:
                random.shuffle(NamenDeelnemers)
                random.shuffle(Lootjes)
                a = True
            else:
                print(f"{NamenDeelnemers[x]} heeft {Lootjes[x]}!")
                a = False
                