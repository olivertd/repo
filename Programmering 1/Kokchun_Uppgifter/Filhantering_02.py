
#ÖPPNAR provresultat.txt och printar alla rader
with open('Provresultat.txt', 'r') as doinkster:
    for line in doinkster:
        print(line,end="")


tomoensamlista = []

#här skapar jag en backwardslash n så det blir en new line
with open('Provresultat.txt', 'a+') as f:
        f.write(str("\n"))

with open('Provresultat.txt', 'r+') as doinkster:
    for line in doinkster:
        tomoensamlista.append(line)
        tomoensamlista.sort()
    for i in tomoensamlista:
        doinkster.write(i)


#här gör jag listor för alla betygen

a = []
b = []
c = []
d = []
e = []
F = []

#här gör jag en tom o ensamlista nummer två för att ha en ny som faktist är tom o ensam
tomoensamlistatva = []


#här öppnar jag provresultat.txt och loopar och appendar alla personer och deras resultat in i rätt lista med rätt betyg
with open('Provresultat.txt', 'r+') as f:
    for i in range(1,20):
        tomoensamlistatva.append(f.readline())
    for elev in tomoensamlistatva:
        elev_betyg = int(elev[-3:])
        if elev_betyg < 20:
            F.append(elev)
        elif elev_betyg >= 20 and elev_betyg <= 29:
            e.append(elev)
        elif elev_betyg >= 30 and elev_betyg <= 39:
            d.append(elev)
        elif elev_betyg >= 40 and elev_betyg <= 49:
            c.append(elev)
        elif elev_betyg >= 50 and elev_betyg <= 59:
            b.append(elev)
        elif elev_betyg >= 60 and elev_betyg <= 70:
            a.append(elev)


#här skriver jag ut resulatet och skriver "betyg" och sen elewverna som hamnat i det betyget
    f.write("\n(a) ELEVER \n")
    for elev in a:
        f.write(elev)
    f.write("\n(b) ELEVER:\n")
    for elev in b:
        f.write(elev)
    f.write("\n(c) ELEVER:\n")
    for elev in c:
        f.write(elev)
    f.write("\n(d) ELEVER:\n")
    for elev in d:
        f.write(elev)
    f.write("\n(e) ELEVER:\n")
    for elev in e:
        f.write(elev)
    f.write("\n(F) ELEVER: \n")
    for elev in F:
        f.write(elev)
