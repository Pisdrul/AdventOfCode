# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 10:16:47 2022

@author: super
"""

with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    count=0
    primo=0
    secondo=0
    terzo=0
    for line in lines:
        if line.strip() == "":
            if(count>primo):
                terzo=secondo
                secondo=primo
                primo=count
            elif(count>=secondo):
                terzo=secondo
                secondo=count
            elif(count>terzo):
                terzo=count
            count=0
        else:
            current = int(line)
            count+=current
    
    print(primo)
    print(secondo)
    print(terzo)
    somma=primo+secondo+terzo
    print(somma)