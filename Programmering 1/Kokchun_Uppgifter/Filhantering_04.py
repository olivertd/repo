#importerar random
import random as rnd

#gör txt filen
with open('simulering.txt', 'w+') as doinkster:
    doinkster.write("")


def supertarningen(mangd):
    tarningrolling = []
    for i in range(mangd):
        tarningrolling.append(rnd.randint(1,6))
    with open('simulering.txt', "a") as doinkster:
        doinkster.write("mangd of dices: {} \n".format(mangd))
        doinkster.write("Antal Ettor: " + str(tarningrolling.count(1)) + " Sannolikhet: " + str(tarningrolling.count(1) / mangd) + "\n")
        doinkster.write("Antal Tvaor: " + str(tarningrolling.count(2)) + " Sannolikhet: " + str(tarningrolling.count(2) / mangd) + "\n")
        doinkster.write("Antal Treor: " + str(tarningrolling.count(3)) + " Sannolikhet: " + str(tarningrolling.count(3) / mangd) + "\n")
        doinkster.write("Antal Fyror: " + str(tarningrolling.count(4)) + " Sannolikhet: " + str(tarningrolling.count(4) / mangd) + "\n")
        doinkster.write("Antal Femmor: " + str(tarningrolling.count(5)) + " Sannolikhet: " + str(tarningrolling.count(5) / mangd) + "\n")
        doinkster.write("Antal Sexor: " + str(tarningrolling.count(6)) + " Sannolikhet: " + str(tarningrolling.count(6) / mangd) + "\n")
        doinkster.write("\n")

khalielectrics = 1
for i in range(5):
    khalielectrics *= 10
    supertarningen(khalielectrics)