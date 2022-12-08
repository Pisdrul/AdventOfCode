def Priority(carattere): #converte carattere in priorità
    if(carattere.islower()):
            priorità = ord(carattere) - 96
            return priorità
    else:
            priorità = ord(carattere) - 38
            return priorità

def iteraLista(team):
    c=''
    for lettera in team[0]:
        c=controllaDuplicati(lettera,team)
        if (c != None):
            return c
def controllaDuplicati(lettera,team):
    for lettere1 in team[1]:
        if(lettera==lettere1):
            for lettere2 in team[2]:
                if(lettera==lettere2):
                    print(team)
                    print(lettere2)
                    return lettera

def CheckBadge(team):
    parola = team[0]
    for lettera in team[0]:
        team[0]=lettera

with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    team=[]
    priorità=0
    for line in lines:
        if(len(team)==3):
            priorità+=Priority(iteraLista(team))
            print(priorità)
            team.clear()
        team.append(line)
    priorità+=Priority(iteraLista(team))
    print(priorità)
