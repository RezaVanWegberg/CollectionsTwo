boodschappenlijstje = {}

A = True
while A:
    toevoeging = input("wilt u iets toevoegen? J/N :")
    if toevoeging == "J":
        wat = input("wat wilt u toevoegen? :")
        if wat in boodschappenlijstje:
            boodschappenlijstje[wat] += 1
        else:
            boodschappenlijstje[wat] = 1
    elif toevoeging == "N":
        A = False

print(boodschappenlijstje)
print('hello world!')