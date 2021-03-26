import string
import math


def ar_fyrsirigt(tal):
    if tal/1000 >= 10:
        return False
    elif tal/1000 < 1 and tal//1000>0:
        return False
    elif tal/1000 >= 1 and tal//1000 < 10:
        return True
    elif tal/1000 < 0 and tal//1000 > -1:
        return False 
    elif tal/1000 <= -1 and tal//1000 > -10:
        return True
    elif tal/1000 > -1 and tal//1000 < 0:
        return False
    elif tal/1000 <= -10:
        return False


# testprogram
testtal = [100, 231, 10000, 10001, -1000, 102313,]

for t in testtal:
    if ar_fyrsirigt(t):
        print(f"{t} är fyrsiffrigt")
    else:
        print(f"{t} är inte fyrsiffrigt")
