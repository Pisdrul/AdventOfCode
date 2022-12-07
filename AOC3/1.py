def Priority(carattere): #converte carattere in priorità
    if(carattere.islower()):
            priorità = ord(carattere) - 96
            return priorità
    else:
            priorità = ord(carattere) - 38
            return priorità

def dividiZaino(zaino): #divida la stringa in 2
    grandezza=int(len(zaino)) +1
    split=grandezza/2 -1
    primaParte=zaino[0:int(split)]
    secondaParte=zaino[int(split):grandezza]
    return primaParte,secondaParte

def iteraString(primaParte,secondaParte):
    c=''
    for lettera in primaParte:
        c=controllaDuplicati(lettera,secondaParte)
        if (c != None):
            return c


def controllaDuplicati(carattere,zaino):
    for lettera in zaino:
        if(carattere == lettera):
            return carattere

with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    priorità=0
    count=0
    for line in lines:
        count+=1
        zaino= line
        primo,secondo=dividiZaino(zaino)
        carattere=iteraString(primo,secondo)
        priorità+=Priority(carattere)
    print(priorità)
