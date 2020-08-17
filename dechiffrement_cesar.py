#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 20:09:26 2020

@author: michee Nonga Mahukola

Ce programme applique l'analyse frequentielle pour casser un chiffrement additif

L'analyse fréquentielle est basée sur le fait que, dans chaque langue, certaines lettres ou combinaisons de lettres apparaissent avec une certaine fréquence. Par exemple, en français, le e est la lettre la plus utilisée, suivie du a et du s. Inversement, le w est peu utilisé.
Une deuxième condition nécessaire pour appliquer cette technique est la longueur du cryptogramme. En effet, un texte trop court ne reflète pas obligatoirement la répartition générale des fréquences des lettres. De plus, si la clé est de la même longueur que le message, il ne pourra y avoir de répétition de lettre et l'analyse fréquentielle deviendra impossible.

"""

import string
import argparse
import random

# ABC...Z
LETTERS = string.ascii_uppercase
# fréquence d'apparition des lettres en Français
# merci wikipédia : http://fr.wikipedia.org/wiki/Analyse_fréquentielle
FR_FREQ = {'a':9.2,'b':1.02,'c':2.64,'d':3.39,'e':15.87,'f':0.95,'g':1.04,\
               'h':0.77,'i':8.41,'j':0.89,'k':0.00,'l':5.34,'m':3.24,'n':7.15,\
               'o':5.14,'p':2.86,'q':1.06,'r':6.46,'s':7.90,'t':7.26,'u':6.24,\
               'v':2.15,'w':0.00,'x':0.30,'y':0.24,'z':0.32}

def chiffrement_additif(text,cle):
    text = text.upper()
    result = ""
    for i in text:
        if i==" " or i=="\t" or i=="\n":
            result = result+i
        else:
            pos = LETTERS.find(i)
            if pos>=0:
                result = result + LETTERS[(pos+cle)%26]
            else:
                result = result + i
    return result

def dechiffrement_additif(text,cle):
    text = text.upper()
    result = ""
    for i in text:
        if i==" " or i=="\t" or i=="\n":
            result = result+i
        else:
            pos = LETTERS.find(i)
            if pos>=0:
                result = result + LETTERS[(pos-cle)%26]
            else:
                result = result + i
    return result
    
def print_table_chiffrement(cle):
    print("TABLE DE CHIFFREMENT, CLE :",cle)
    
    for i, char in enumerate(LETTERS):
        print("%4d"%i, end="")
    print("")
    print('-'*(26*4))
    for i, char in enumerate(LETTERS):
        print("%4s"%char, end="")
    print("")
    print('-'*(26*4))
    for i, char in enumerate(LETTERS):
        print("%4s"%LETTERS[(i+cle)%26], end="")
    print("")
    print('-'*(26*4))

def print_table_dechiffrement(cle):
    print("TABLE DE DECHIFFREMENT, CLE :", cle)
    
    for i, char in enumerate(LETTERS):
        print("%4d"%i, end="")
    print("")
    print('-'*(26*4))
    for i, char in enumerate(LETTERS):
        print("%4s"%char, end="")
    print("")
    print('-'*(26*4))
    for i, char in enumerate(LETTERS):
        print("%4s"%LETTERS[(i-cle)%26], end="")
    print("")
    print('-'*(26*4))


def start_application(text, combien):
    text = text.upper()
    dechiffre_list = []
    frequences_list = []
    ponderation_list = {}
    
    for i in range(26):
        dechiffre = dechiffrement_additif(text, i)
        dechiffre_list.append(dechiffre)
        frequences = {}
        ponderation = 0
        for j in LETTERS:
            # frequence du caractère dans la phrase
            freq = dechiffre.count(j)*100/len(text)
            frequences[j] = freq
            # on pondere la frequence avec les stats
            ponderation += freq*FR_FREQ[j.lower()]
        frequences_list.append(frequences)
        # on stocke la ponderation pour cette phrase
        ponderation_list[i]=ponderation
        
    # trier par ordre croissant
    result = sorted(ponderation_list.items(), key=lambda x: x[1])   
    # inverser pour avoir l'ordre decroissant
    result.reverse()
    print("LES %d TEXTES CLAIRES POSSIBLES"%combien)
    print("-"*56)
    for key, val in result[:combien]:
        print("Clé %2d, ponderation %4.2f"% (key, val))
        print(dechiffre_list[key])
    exit()

    
if __name__=="__main__":
    
    parser = argparse.ArgumentParser()
    #parser.add_argument('action', help="Action à effectuer", choices=["crypter","decrypter"])
    parser.add_argument('text' , help="Texte à dechiffrer")
    parser.add_argument('combien', help="Combien de principaux texte en clair vous voulez?", type=int)
    args = parser.parse_args()
    
    # chiffre le texte clair recu avec une cle generer aleatoirement
    chiffre = chiffrement_additif(args.text, random.randint(0,26 ))   
    # tenter de dechiffrer 
    start_application(chiffre, args.combien)
    
