from Stadion import Stadion

import filebeolvasas, feladatok

stadionok=filebeolvasas.beolvas("stadionok.txt",[])
for i in range(1,len(stadionok),1):
    print(stadionok[i])

print(f"Első stadion neve:{stadionok[0]}")


feladat1=feladatok.new_york(stadionok)
print(f"A New York-i Stadionok száma: {feladat1}")

feladat2=feladatok.csapatszam(stadionok)
print(f"Csapatok száma: {feladat2}")
