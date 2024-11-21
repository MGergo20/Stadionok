def new_york(stadion_lista):
    db=0
    for i in range(0,len(stadion_lista),1):
        if stadion_lista[i].varos == "New York":
            db+=1
    return db


def csapatszam(stadion_lista):
    csapat_db=0
    for i in range(0,len(stadion_lista),1):
        if 1<= stadion_lista[i].csapatok_szama <=100:
            csapat_db+=1
    return csapat_db














def Buffalo(stadion_lista):
    buffalo_db=0
    for i in range(0,len(stadion_lista),1):
        if stadion_lista[i].varos == "Buffalo":
            buffalo_db+=1
    return buffalo_db



