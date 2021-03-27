
#här gör jag min dictionary med key och value som är en del kurser
doinkctionary = {"tillämpad_1" : 100, "programmering_1" : 100, "daodac" : 100, "svenska_2" : 100, "fysik_1" : 150, "idrott" : 100, "engelska_6" : 100, "matematik_4" : 100}


#skapar ny variabel med 0 värde

POANG = 0

#här gör jag en foor loop
for key,value in doinkctionary.items():
    POANG += value

#här är min print 
print("DINA TOTALA POANG AR", POANG, "POANG, DET NUMMRET SOM PRESIS SKREVS UT (",POANG ,") ÄR DINA TOTAL POANG")