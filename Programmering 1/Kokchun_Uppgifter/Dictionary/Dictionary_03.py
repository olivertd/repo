#skapar variablar
POKEDEX  = {}

#ÖPPNAR provresultat.txt och gör en foor loop för varje rad som sorterar med index och typ
with open("pokemonlista.txt", "r",encoding="utf8") as doinkster:
    for line in doinkster:
        index, pokemon, typ = line.split()
        POKEDEX[pokemon] = [typ, index]

#Gör en print som printar typen och indexet (första value av key och sen andrra)
print("typ:", POKEDEX["Gastly"][0], ", index", POKEDEX["Gastly"][1])
print("typ:", POKEDEX["Pikachu"][0], ", index", POKEDEX["Pikachu"][1])