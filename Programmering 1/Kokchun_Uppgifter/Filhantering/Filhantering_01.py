#FILHANTERING 01,
#A)
#imnpotera randomm
import random as rnd

#skapar en lista
tomoensamlist = []

#skapar en txt fil med rätt namn
with open("diceRoll.txt", "w+") as f:
    f.write("")

#gör en foor loop som loopar 10 gånger, i loopen randomizas ett randomised nummer mellan 1-6 och senn appendas det in i diceRoll filen
for i in range(10):
    kasst = rnd.randint(1,6)
    tomoensamlist.append(kasst)
    with open("diceRoll.txt", "a+") as f:
        f.write(str(kasst))
        f.write(" ")

#B)

#här skapar jag en backwardslash n så det blir en new line
with open("diceRoll.txt", "a+") as f:
        f.write(str("\n"))

#här soterar jag tomoensamlsit så alla talen kommer i rätt ordning
tomoensamlist.sort()

#här skriver jag in den nya sorterade listan in i diceroll txt fil
with open("diceRoll.txt", "a+") as f:
        f.write(str(tomoensamlist))

#C)

#här skapar jag en backwardslash n så det blir en new line
with open("diceRoll.txt", "a+") as f:
        f.write(str("\n"))

#gör ny variabel femmor o gör en foor loop för att räkna femmorna i tomoensamlist
femmor = 0
for i in tomoensamlist:
    if i == 5:
        femmor+=1

#här skriver jag antalet femmor o printar det förra foor loopen räkadenede
with open("diceRoll.txt", "a+") as f:
        f.write("antal femmor som rullades po supertarningen ar: ")
        f.write(str(femmor))


