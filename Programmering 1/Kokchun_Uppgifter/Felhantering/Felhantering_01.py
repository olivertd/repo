#Importerarny py numpy y-
import numpy as np

#här är min funktion som definerar distance med hjälp av np.sqrt och returnar värdet
def distance(x,y):
    distans = np.sqrt(x + y)
    return distans

#här printar jag "HÄR ÄR DIN SITANS" följt med printed distance som skickar in värdet in i funktionen 0.5 x 0.5!
print("HEJ HÄR ÄR DIN DISTANS!")
print(distance(0.5,0.5))