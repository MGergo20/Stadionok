from Stadion import Stadion

import filebeolvasas

stadionok=filebeolvasas.beolvas("stadionok.txt",[])
for i in range(1,len(stadionok),1):
    print(stadionok[i])

print(f"Első stadion neve:{stadionok[0]}")