torre1 = ['G','D','V','Z','J','S','B']
torre2 = ['Z','S','M','G','V','P']
torre3 = ['C','L','B','S','W','T','Q','F']
torre4 = ['H','J','G','W','M','R','V','Q']
torre5 = ['C','L','S','N','F','M','D']
torre6 = ['R','G','C','D']
torre7 = ['H','G','T','R','J','D','S','Q']
torre8 = ['P','F','V']
torre9 = ['D','R','S','T','J']
torri = [torre1,torre2,torre3,torre4,torre5,torre6,torre7,torre8,torre9]

def NumeroScatole(frase):
    separ = frase.find('from')
    numeroScatole = int(frase[4:separ])
    return numeroScatole
def DaDoveADove(frase):
    separ = frase.find('from')
    separ2 = frase.find('to')
    daDove = int(frase[separ+4:separ2])
    aDove= int(frase[separ2+2:])
    return daDove,aDove
def SpostaScatole(qtaScatole,torreA,torreB):
    while qtaScatole > 0:
        x=len(torreA)
        y=torreA[x-1]
        torreB.append(y)
        torreA.pop(x-1)
        qtaScatole -=1
    return torreA,torreB
def printFinal(pila):
    for scatole in pila:
        x=len(scatole)
        print(scatole[x-1])
with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        x,y = DaDoveADove(line)
        qtaScatole = NumeroScatole(line)
        torri[x-1],torri[y-1]=SpostaScatole(qtaScatole,torri[x-1],torri[y-1])
    print(torri)
    printFinal(torri)
