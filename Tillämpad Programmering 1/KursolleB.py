#Här är en funktion för area
def area(s1,s2):
    area = s1 * s2
    return area

#Här är en funktion för kvadrat
def kvadrat(s1,s2):
    if s1 == s2:
        kvadrat = "ja"
    else:
        kvadrat = "nej"
    return kvadrat

#Nedanför är alla mina listor
arealista = []
s1lista = []
s2lista = []

kvadratlista = []

#Gör en variabel
dankstercountyboi = 0


#
while True:
    user_input = str(input("Vill du göra en beräkning y/n?: "))
    if user_input == "n":
        break

    dankstercountyboi += 1
    #Skapar inputs för användaren
    s1 = int(input("Ange Sida 1: "))
    s2 = int(input("Ange Sida 2: "))

    #
    s1lista.append(s1)
    s2lista.append(s2)
    arealista.append(area(s1,s2))

    kvadratlista.append(kvadrat(s1,s2))
    print(f"{kvadrat(s1,s2)} kvadrat")

    #Här loopar jag 1-11, Beräknar volymen genom att ta sida 1 gånger sida 2 gånger antalet loopar och sedan printar jag svaret av volymen
    for loop in range(11):
        volym = s1 * s2 * loop
        print(volym)


#
for loopster in range(dankstercountyboi):
    print(f"{loopster} beräkning har sidorna {s1lista[loopster]} {s2lista[loopster]} och är det en kvadrat? {kvadratlista[loopster]}. arean är {arealista[loopster]}.")