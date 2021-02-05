#
def omkrets(s1, s2):
   omkrets = s1 + s1 + s2 + s2
   return omkrets

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
omkretslista = []
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
    while True:
        try:
            h = int(input("Ange höjd: "))
            break
        except:
            print("stoopid rarted lortard, det var inget heltal!")

    if h < 0:
        h = 1
    elif h > 10:
        h = 10


    #
    s1lista.append(s1)
    s2lista.append(s2)
    arealista.append(area(s1,s2))
    omkretslista.append(omkrets(s1,s2))
    kvadratlista.append(kvadrat(s1,s2))
    print(f"{kvadrat(s1,s2)} kvadrat")

    #Här loopar jag 1-11, Beräknar volymen genom att ta sida 1 gånger sida 2 gånger antalet loopar och sedan printar jag svaret av volymen
    for loop in range(h + 1):
        volym = s1 * s2 * loop
        print(volym)


#
for loopster in range(dankstercountyboi):
    print(f"{loopster} beräkning har sidorna {s1lista[loopster]} och {s2lista[loopster]}. Är det en kvadrat? {kvadratlista[loopster]}. arean är {arealista[loopster]}. Omkretsen är {omkretslista[loopster]}.")