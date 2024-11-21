import datetime
def new_york(stadion_lista):
    db=0
    for i in range(0,len(stadion_lista),1):
        if stadion_lista[i].varos == "New York":
            db+=1
    return db


def csapatszam(stadion_lista):
    csapat_db=0
    for i in range(0,len(stadion_lista),1):
        csapat_db+=stadion_lista[i].csapatok_szama
    return csapat_db

def ezerkilenc(stadion_lista):




def ketezer_ota(stadion_lista):
    eredmény=[]
    for i in range (1,len(stadion_lista)):
        if stadion_lista[i].utolso_merk <datetime.strptime("2000-01-01","%Y-%m-%d"):
            ketezres+=1
    return ketezres


def Buffalo(stadion_lista):
    buffalo_db=0
    for i in range(0,len(stadion_lista),1):
        if stadion_lista[i].varos == "Buffalo":
            buffalo_db+=1
    return buffalo_db



