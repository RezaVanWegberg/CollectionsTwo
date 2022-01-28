from operator import truediv
import random

aces = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0

k = True

def bord():
    print(f"[1] ACES {aces}")
    print(f"[2] TWOS {twos}")
    print(f"[3] THREES {threes}")
    print(f"[4] FOURS {fours}")
    print(f"[5] FIVES {fives}")
    print(f"[6] SIXES {sixes}")

GeroldeStenen = [' ']*5

def Rolstenen(GeroldeStenen:list):
    for x in range(5):
        GeroldeStenen[x] = random.randint(1,6)
    return GeroldeStenen

def reroll(LijstRerolls,Dobbelstenen):
    for x in LijstRerolls:
        position = x -1
        roll = random.randint(1,6)
        Dobbelstenen[position] = roll
    return Dobbelstenen
    
pogingen = 2

bord()
for x in range(6):
    
    GeroldeStenen = Rolstenen(GeroldeStenen)
    print(GeroldeStenen)

    pogingen = 2

    k = True
    while pogingen != 0:
        RollInput = input(f"Wilt u rerollen? U heeft nog {pogingen} pogingen (Y/N) ")
        if RollInput.lower() == "y":
            LijstRerolls = []
            while True:
                inputReroll = int(input("Welke dobbelstenen moeten opnieuw worden gererolled? (0 is klaar): "))
                if inputReroll != 0:
                    LijstRerolls.append(inputReroll)
                else:
                    break
            GeroldeStenen = reroll(LijstRerolls,GeroldeStenen)
            print(GeroldeStenen)
            pogingen -= 1
        elif RollInput.lower() == "n":
            break
        else:
            print("dat kan niet")

    bord()
    while k == True:
        KeuzeScore = input("Kies welke score je wilt invullen! \n:")
        if KeuzeScore == "1":
            if aces == 0:
                for i in range(5):
                    if GeroldeStenen[i] == 1:
                        aces += 1
                        k = False
            else:
                print("die kan niet meer")
        elif KeuzeScore == "2":
            if twos == 0:
                for i in range(5):
                    if GeroldeStenen[i] == 2:
                        twos += 1
                        k = False
            else:
                print("die kan niet meer")
        elif KeuzeScore == "3":
            if threes == 0:
                for i in range(5):
                    if GeroldeStenen[i] == 3:
                        threes += 1
                        k = False
            else:
                print("die kan niet meer")
        elif KeuzeScore == "4":
            if fours == 0:
                for i in range(5):
                    if GeroldeStenen[i] == 4:
                        fours += 1
                        k = False
            else:
                print("die kan niet meer")
        elif KeuzeScore == "5":
            if fives == 0:
                for i in range(5):
                    if GeroldeStenen[i] == 5:
                        fives += 1
                        k = False
            else:
                print("die kan niet meer")
        elif KeuzeScore == "6":
            if sixes == 0:
                for i in range(5):
                    if GeroldeStenen[i] == 6:
                        sixes += 1
                        k = False
            else:
                print("die kan niet meer")
        elif KeuzeScore == "HELP":
            k = False
        else:
            print("dat kan niet")
    bord()
