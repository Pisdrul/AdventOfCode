# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 10:57:20 2022

@author: super
"""

def Carta(giocatore):
    match giocatore:
        case "Y":#Carta giocata dal giocatore c
            return "Draw"
        case "X":#Roccia giocata dal giocatore contro carta
            return "Loss"
        case "Z":#Forbici giocate dal giocatore contro carta
            return "Win"
def Sasso(giocatore):
    match giocatore:
        case "Y":
            return "Win"
        case "X":
            return "Draw"
        case "Z":
            return "Loss"
def Forbici(giocatore):
    match giocatore:
        case "Y":
            return "Loss"
        case "X":
            return "Win"
        case "Z":
            return "Draw"
def MatchResult(nemico,giocatore):
    match nemico:
        case "A":
            return Sasso(giocatore)
        case "B":
            return Carta(giocatore)
        case "C":
            return Forbici(giocatore)
def Points(result,shape):
    punteggio=0
    match result: #0 se loss 3 se draw 6 se win
        case "Loss":
            punteggio+=0
        case "Win":
            punteggio+=6
        case "Draw":
            punteggio+=3
    match shape: #+1 se roccia +2 se carta +3 se forbici
        case "X":
            punteggio+=1
        case "Y":
            punteggio+=2
        case "Z":
            punteggio+=3
    return punteggio



with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    score = 0
    for line in lines:
        current = line.split()
        risultato = MatchResult(current[0],current[1])
        score+=Points(risultato,current[1])
    print(score)
