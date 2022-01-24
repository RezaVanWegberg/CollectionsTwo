# Maak een programma die een wachtwoord van 24 tekens genereerd.

# Het wachtwoord moet aan de volgende eisen voldoen:

# 2 tot 6 hoofdletters.
# Minimaal 8 kleine letters.
# 3 speciale tekens uit de volgende reeks: @ # $ % & _ ?.
# De speciale tekens mogen niet op de eerste of laatste positie staan en ook niet op een vaste plek.
# 4 tot 7 cijfers (0 t/m 9).
# Op de eerste 3 posities mag geen cijfer staan.

import string
import random

string.ascii_uppercase

HoofdLetterList = []
for x in range(random.randint(2,6)):
    HoofdLetter = (random.choice(string.ascii_uppercase))
    HoofdLetterList.append(HoofdLetter)



string.ascii_lowercase

KleineLetterList = []
for y in range(random.randint(8,14)):
    KleineLetter = (random.choice(string.ascii_lowercase))
    KleineLetterList.append(KleineLetter)


SpecialeTekens = ["@", "#", "$", "%", "&", "_", "?"]
SpecialeTekenList = []
for z in range(random.randint(3,10)): #het maximum is niet aangegeven
    SpeciaalTeken = (random.choice(SpecialeTekens))
    SpecialeTekenList.append(SpeciaalTeken)

NulTotNegen = [0,1,2,3,4,5,6,7,8,9]
NummerList = []
for n in range(random.randint(4,7)):
    Nummer = random.choice(NulTotNegen)
    NummerList.append(Nummer)

Password = HoofdLetterList + KleineLetterList + SpecialeTekenList + NummerList


print(HoofdLetterList)
print(KleineLetterList)
print(SpecialeTekenList)
print(NummerList)


random.shuffle(Password)
while True:
    if Password[0] in SpecialeTekenList or Password[-1] in SpecialeTekenList or Password[0:3] in NummerList: # [-1] pakt de laatste element van een list en [0:3] pakt de eerste 3 elementen
        print("reRollDobbelsteen")
        print(Password)
        random.shuffle(Password)
    else:
        break

print("result")
print(Password)
