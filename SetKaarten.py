import random
soort = ["schoppen", "harten", "klaver", "ruiten"]
nmrkaart = ["aas",2,3,4,5,6,7,8,9,10,"boer","vrouw","heer"]
deck = []
kaarten = {}

for key in soort:
    for value in nmrkaart:
        kaarten= {key:value}
        deck.append(kaarten)
for x in range(2):
    deck.append('joker')   
random.shuffle(deck)
for n in range(6):
    print(deck.pop(n))
print("------------------")
print(deck)