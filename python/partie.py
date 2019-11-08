#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import joueur as j
import intCons as IC

class Partie(object):
    """docstring for Partie."""
    def __init__(self, players, roles):
        super(Partie, self).__init__()
        self.interface = IC.IntCons()
        self.playerbase = self.distribRole(players, roles)

        self.alive = self.getAlive(self.playerbase)
        self.LG = self.getLG(self.alive)
        self.vill = self.getVillage(self.alive)

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

    #Lance une partie
    def playGame(self):
        self.printAllJoueur(self.playerbase)
        self.interface.afficher("\nLa partie commence!")
        self.interface.mettreAJour(self)
        i = 0
        while (self.isFinished() == False):
            self.interface.afficher("\nNuit " + str(i) + "\n")
            mort = self.voteLG()
            vovo = self.getVovo(self.alive)
            if (vovo != None):
                vovo.role.pouvoir(self)
            self.interface.afficher("\nJour " + str(i) + "\n")
            self.revelerMorts(mort)
            self.interface.mettreAJour(self)
            if (self.isFinished() == False):
                mort = self.voteVillage()
                self.revelerMorts(mort)
                self.interface.mettreAJour(self)
            i = i + 1
        self.victoire()

    #Détermine la victoire
    def victoire(self):
        if (len(self.alive) == 0):
            self.interface.afficher("\nPersonne a gagné")
        elif (len(self.LG) == 0):
            self.interface.afficher("\nLes Villageois ont gagné!")
        elif (len(self.vill) == 0):
            self.interface.afficher("\nLes Loups-Garous ont gagné!")

    #Determine si la partie de LG est finie
    def isFinished(self):
        if (len(self.LG) == 0 or len(self.vill) == 0):
            return (True)
        else:
            return (False);

    #Effectue le vote du Village
    def voteVillage(self):
        vote = self.interface.faireVote(self, self.alive, self.alive)
        if (len(vote) == 1):
            self.interface.afficher("\nLe Village a décidé d'éliminer " + vote[0].nom + " et leur sentence est irrévocable")
            return (vote)
        else:
            self.interface.afficher("\nSecond tour de vote")
            vote = self.interface.faireVote(self, self.alive, vote)
            if (len(vote) == 1):
                self.interface.afficher("\nLe Village a décidé d'éliminer " + vote[0].nom + " et leur sentence est irrévocable")
                return (suspect)
            else:
                self.interface.afficher("\nLe Village ne s'est pas mis d'accord : Aucun bûcher")
        return ([])

    #Effectue le vote des LG
    def voteLG(self):
        vote = self.interface.faireVote(self, self.LG, self.vill)
        if (len(vote) == 1):
            self.interface.afficher("\nLes Loups-Garous ont décidés de manger " + vote[0].nom + "\n")
            return (vote)
        else:
            self.interface.afficher("\nLes Loups-Garous ne se sont pas mis d'accord et ne mangeront personne\n")
            return ([])

    #Revele les morts de la nuit et les morts du vote
    def revelerMorts(self, mort):
        for player in mort:
            player.mourir(self)

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

    #Returne la voyante si elle existe
    def getVovo(self, list):
        vovo = None
        for player in list:
            if (player.role.__class__.__name__ == "Voyante"):
                vovo = player
        return (vovo)

    #Retourne tout les joueurs vivants
    def getAlive(self, list):
        alive = []
        for player in list:
            if (player.vivant == True):
                alive.append(player)
        return (alive)

    #Affiche tout les joueurs
    def printAllJoueur(self, playerbase):
        for player in playerbase:
            player.printJoueur(self)

    #Fonction interne de MaJ
    def updateGame(self):
        self.alive = self.getAlive(self.playerbase)
        self.LG = self.getLG(self.alive)
        self.vill = self.getVillage(self.alive)
