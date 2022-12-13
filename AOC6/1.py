def TrovaParola(Segnale,Start,End):
    SubSegnale = Segnale[Start:End]
    print(SubSegnale)
    if ControllaDoppie(SubSegnale):
        return True
    else:
        return False
def ControllaDoppie(SubSegnale):
    for lettera in SubSegnale:
        if SubSegnale.count(lettera) >=2:
            return False
    return True
with open('input.txt', 'r', encoding="utf-8") as f:
    line = f.readlines()
    segnale = line[0]
    found = False
    start = 0
    end = 14
    while found == False:
        found=TrovaParola(segnale,start,end)
        if found:
            print(end)
        else:
            start+=1
            end +=1
