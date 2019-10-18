#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import joueur as j

class Partie(object):
    """docstring for Partie."""
    def __init__(self, players, roles):
        super(Partie, self).__init__()
        self.playerbase = self.distribRole(players, roles)
        self.alive = self.getAlive(self.playerbase)
        self.LG = self.getLG(self.alive)
        self.vill = self.getVillage(self.alive)
        print(self.playerbase)

    #Met à jour les listes de joueurs
    def updateGame(self):
        self.alive = self.getAlive(self.playerbase)
        self.LG = self.getLG(self.alive)
        self.vill = self.getVillage(self.alive)

    #Lance une partie
    def playGame(self):
        self.printAllJoueur(self.playerbase)
        print("\nLa partie commence!")
        i = 0
        while (self.isFinished() == False):
            print("\nNuit " + str(i) + "\n")
            mort = self.voteLG()
            print("\nJour " + str(i) + "\n")
            self.revelerMorts(mort)
            self.updateGame()
            if (self.isFinished() == False):
                mort = self.voteVillage()
                self.revelerMorts(mort)
                self.updateGame()
            i = i + 1

        if (len(self.alive) == 0):
            print("\nPersonne a gagné")
        elif (len(self.LG) == 0):
            print("\nLes Villageois ont gagné!")
        elif (len(self.vill) == 0):
            print("\nLes Loups-Garous ont gagné!")

    #Determine si la partie de LG est finie
    def isFinished(self):
        if (len(self.LG) == 0 or len(self.vill) == 0):
            return (True)
        else:
            return (False);

    #Distribue les rôles
    def distribRole(self, joueur, role):
        distrib = []
        while (len(role) != 0 or len(joueur) != 0):
            a = random.randrange(len(joueur))
            b = random.randrange(len(role))
            player = j.Joueur(joueur[a],role[b])
            distrib.append(player)
            joueur.remove(joueur[a])
            role.remove(role[b])
        return (distrib)

    #Effectue le vote du Village
    def voteVillage(self):
        vote = []
        for player in self.alive:
            vote.append(player.voter(self.alive))
        suspect = self.majorite(vote)
        if (len(suspect) == 1):
            print("Le Village a décidé d'éliminer " + suspect[0].nom + " et leur sentence est irrévocable")
            return (suspect)
        else:
            print("Second tour de vote")
            vote = []
            for player in self.alive:
                vote.append(player.voter(suspect))
            suspect = self.majorite(vote)
            if (len(suspect) == 1):
                print("Le Village a décidé d'éliminer " + suspect[0].nom + " et leur sentence est irrévocable")
                return (suspect)
            else:
                print("Le Village ne s'est pas mis d'accord : Aucun bûcher")
        return ([])

    #Effectue le vote des LG
    def voteLG(self):
        vote = []
        for player in self.LG:
            vote.append(player.role.manger(player.nom, self.vill))
        suspect = self.majorite(vote)
        if (len(suspect) == 1):
            print("Les Loups-Garous ont décidés de manger " + suspect[0].nom)
            return (suspect)
        else:
            print("Les Loups-Garous ne se sont pas mis d'accord et ne mangeront personne")
            return ([])

    #Revele les morts de la nuit et les morts du vote
    def revelerMorts(self, mort):
        for player in mort:
            player.mourir()

    #Definit la majorite des votes et prend en compte les possibles egalites
    def majorite(self, list):
        max = 0
        vote = []
        for i in list:
            frequence = list.count(i)
            if (frequence == max and vote.count(i) == 0):
                vote.append(i)
            if (frequence > max):
                max = frequence
                vote = [i]
        return vote

    #Retourne la liste des joueurs LG
    def getLG(self, list):
        LG=[]
        for player in list:
            if (player.role.__class__.__name__ == "LoupGarou"):
                LG.append(player)
        return (LG)

    #Retourne la liste des joueurs non-LG
    def getVillage(self, list):
        vill=[]
        for player in list:
            if (player.role.__class__.__name__ != "LoupGarou"):
                vill.append(player)
        return (vill)

    #Retourne tout les joueurs vivants
    def getAlive(self, list):
        alive = []
        for player in list:
            if (player.vivant == True):
                #print("" + player.nom + " est encore vivant")
                alive.append(player)
        return (alive)

    #Affiche tout les joueurs
    def printAllJoueur(self, playerbase):
        for player in playerbase:
            player.printJoueur()
