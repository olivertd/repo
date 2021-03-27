#importerar random as rnd
import random as rnd

#skapar variablar för varje mängd av siffror
ETTORVAR = 0
TVÅORVAR = 0
TREORVAR = 0
FYRORVAR = 0
FEMMORVAR = 0
SEXORVAR = 0

#SKAPAR MIN DICTIONARy
doinkctionary = {"ETTOR" : 0,  "TVÅOR" : 0, "TREOR" : 0,"FYROR" : 0, "FEMMOR" : 0, "SEXOR" : 0,}


#SIMULERAR TÄRNINGSKASSTEN med en foor loop och random OCH SORTERAR IN DEM I RÄTT VARIABLE BEROENDE PÅ HUR MÅNGA AV VARJE SOM SLÅS
for i in range(100000):
    kasst = rnd.randint(1,6)
    if kasst == 1:
        ETTORVAR += 1
    if kasst == 2:
        TVÅORVAR += 1
    if kasst == 3:
        TREORVAR += 1
    if kasst == 4:
        FYRORVAR += 1
    if kasst == 5:
        FEMMORVAR += 1
    if kasst == 6:
        SEXORVAR += 1

#HÄr uppdaterar jag dicitonaryn med mina nya värdet som jag fick från for loopen där jag simulerade tärningarna och uppdaterar antalet av varje kasst med rätt värde.
doinkctionary.update({"ETTOR" : ETTORVAR,  "TVÅOR" : TVÅORVAR, "TREOR" : TREORVAR,"FYROR" : FYRORVAR, "FEMMOR" : FEMMORVAR, "SEXOR" : SEXORVAR,})

#Här gör jag multipla fina prints som gör så att allt kommer ut fint formaterat och i rätt ordning
print("HÄr är en tabbel på hur många ganger varje siffra slogs:")
print("ETTOR slogs", doinkctionary["ETTOR"], "Gånger")
print("TVÅOR slogs", doinkctionary["TVÅOR"], "Gånger")
print("TREOR slogs", doinkctionary["TREOR"], "Gånger")
print("FYROR slogs", doinkctionary["FYROR"], "Gånger")
print("FEMMOR slogs", doinkctionary["FEMMOR"], "Gånger")
print("SEXOR slogs", doinkctionary["SEXOR"], "Gånger")