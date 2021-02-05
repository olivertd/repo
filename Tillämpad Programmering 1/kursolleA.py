#Skapar inputs för användaren
s1 = int(input("Ange Sida 1: "))
s2 = int(input("Ange Sida 2: "))

#Här beräknar jag arean med korrekt matematik
arean = s1 * s2
print(arean)

#Här gör jag en IF sats för att kolla om sida 1 är = sida 2 för att enligt korrekt matematik är det då en kvadrat
if s1 == s2:
    print("Det är en kvadrat")
else:
    pass

#Här loopar jag 1-11, Beräknar volymen genom att ta sida 1 gånger sida 2 gånger antalet loopar och sedan printar jag svaret av volymen
for loop in range(11):
    volym = s1 * s2 * loop
    print(volym)
