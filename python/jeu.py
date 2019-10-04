#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import joueur as j
from collections import Counter

def distribRole(joueur, role):
    distrib = []
    while (len(role) != 0 or len(joueur) != 0):
        a = random.randrange(len(joueur))
        b = random.randrange(len(role))
        player = j.Joueur(joueur[a],role[b])
        distrib.append(player)
        joueur.remove(joueur[a])
        role.remove(role[b])
    return (distrib)

def printAllJoueur(distrib):
    for player in distrib:
        player.printJoueur()

def getAlive(distrib):
    alive = []
    for player in distrib:
        if (player.vivant == True):
            #print("" + player.nom + " est encore vivant")
            alive.append(player)
    return (alive)

def voteVillage(alive):
    vote = []
    for player in alive:
        vote.append(player.voter(alive))

    #A améliorer s'il y a égalite
    suspect = Counter(vote).most_common()
    #print(suspect)
    suspect = suspect[0][0]
    #print(suspect)
    return (suspect)

def voteLG(LG,vill):
    vote = []
    for player in LG:
        vote.append(player.role.manger(player.nom, vill))

    #A améliorer s'il y a égalite
    suspect = Counter(vote).most_common()
    #print(suspect)
    suspect = suspect[0][0]
    #print(suspect)
    return (suspect)

def getLG(list):
    LG=[]
    for player in list:
        if (player.role.__class__.__name__ == "LoupGarou"):
            LG.append(player)
    return (LG)

def getVillage(list):
    vill=[]
    for player in list:
        if (player.role.__class__.__name__ != "LoupGarou"):
            vill.append(player)
    return (vill)

joueur = ["Remi", "Thomas", "Samuel", "Hugo", "Chollet"]
role = ["LG", "SV", "SV", "LG" , "SV"]
distrib = distribRole(joueur, role)
printAllJoueur(distrib)
print("\nLa partie commence!")
alive = getAlive(distrib)
LG = getLG(alive)
vill = getVillage(alive)
i = 0
while (len(alive) != 0 and len(LG) != 0 and len(vill) != 0):
    print("\nNuit " + str(i) + "\n")
    mort = voteLG(LG,vill)
    print("\nJour " + str(i) + "\n")
    mort.mourir()
    alive = getAlive(distrib)
    LG = getLG(alive)
    vill = getVillage(alive)
    if (len(alive) != 0 and len(LG) != 0 and len(vill) != 0):
        mort = voteVillage(alive)
        mort.mourir()
        alive = getAlive(distrib)
        LG = getLG(alive)
        vill = getVillage(alive)
    i = i + 1

if (len(alive) == 0):
    print("\nPersonne a gagné")
elif (len(LG) == 0):
    print("\nLes Villageois ont gagné!")
elif (len(vill) == 0):
    print("\nLes Loups-Garous ont gagné!")
#print(vote)
