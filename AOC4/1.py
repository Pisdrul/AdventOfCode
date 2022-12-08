def numeroRange(range):
    separazione=range.find('-')
    inizio=int(range[0:separazione])
    fine=int(range[separazione+1:])
    return inizio,fine

def controllaOverlap(inizio1,fine1,inizio2,fine2):
    if(inizio1<=inizio2 and fine1>=fine2):
        return 1
    elif(inizio2<=inizio1 and fine2>=fine1):
        return 1
    else:
        print(inizio1,fine1,inizio2,fine2)
        return 0






with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    conta = 0
    for coppia in lines:
        separazione=coppia.find(",")
        elfo1=coppia[0:separazione]
        elfo2=coppia[separazione+1:]
        inizio1,fine1=numeroRange(elfo1)
        inizio2,fine2=numeroRange(elfo2)
        conta += controllaOverlap(inizio1,fine1,inizio2,fine2)
        print(conta)
