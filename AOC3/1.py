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
    secondaParte=zaino[int(split)  :grandezza]
    return primaParte,secondaParte

def iteraString(primaParte,secondaParte):
    for lettera in primaParte:
        c=controllaDuplicati(lettera,secondaParte)
        if (c!=' '):
            print(c)
            return c

def controllaDuplicati(carattere,zaino):
    for lettera in zaino:
        if(carattere == lettera):
            return carattere
            break

with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    priorità=0
    for line in lines:
        zaino= line
        primo,secondo=dividiZaino(zaino)
        priorità+=Priority(iteraString(primo,secondo))
        print(priorità)
