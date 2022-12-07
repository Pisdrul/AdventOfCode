# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 10:57:20 2022

@author: super
"""

def Carta(result):
    match result:
        case "Win": # vinci contro carta quindi forbici (+3)
            return 3
        case "Draw": # pareggi contro carta quindi carta (+2)
            return 2
        case "Loss": # perdi contro carta quindi sasso (+1)
            return 1
def Sasso(result):
    match result:
        case "Win": # vinci contro sasso quindi carta (+2)
            return 2
        case "Draw": # pareggi contro sasso quindi sasso (+1)
            return 1
        case "Loss": # perdi contro sasso quindi forbici (+3)
            return 3
def Forbici(result):
    match result:
        case "Win": # vinci contro forbici quindi sasso (+1)
            return 1
        case "Draw": # pareggi contro forbici quindi forbici (+3)
            return 3
        case "Loss": # perdi contro forbici quindi carta (+2)
            return 2
def MatchResult(result):
    match result:
        case "X":
            return "Loss"
        case "Y":
            return "Draw"
        case "Z":
            return "Win"
def Points(result,nemico):
    punteggio=0
    match result: #0 se loss 3 se draw 6 se win
        case "Loss":
            punteggio+=0
        case "Win":
            punteggio+=6
        case "Draw":
            punteggio+=3
    match nemico: #punteggio in base a cosa hai giocato
        case "A":
            punteggio+=Sasso(result)
        case "B":
            punteggio+=Carta(result)
        case "C":
            punteggio+=Forbici(result)
    return punteggio



with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    score = 0
    for line in lines:
        current = line.split()
        risultato = MatchResult(current[1])
        score+=Points(risultato,current[0])
    print(score)
