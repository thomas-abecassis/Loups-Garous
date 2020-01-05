#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import joueur as j
import asyncio 

class Partie(object):
    """docstring for Partie."""
    def __init__(self, interface, players, roles):
        super(Partie, self).__init__()
        self.interface = interface
        self.playerbase = self.distribRole(players, roles)

        self.prochainRole="LG"
        self.alive = self.getAlive(self.playerbase)
        self.LG = self.getLG(self.alive)
        self.vill = self.getVillage(self.alive)
        self.jour=False

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
    async def playGame(self):
        # on l'enlève pour le web 
        # await self.printAllJoueur(self.playerbase)
        await self.interface.afficher("\nLa partie commence!")
        await self.interface.mettreAJour(self)
        i = 0
        while (self.isFinished() == False):
            self.jour=False
            await self.interface.mettreAJour(self)
            self.prochainRole="LoupGarou"
            mort = await self.voteLG()
            vovo = self.getVovo(self.alive)
            if (vovo != None):
                await vovo.role.pouvoir(self) 
            self.updateGame() 
            if (self.isFinished() == False):
                self.jour=True
                await self.revelerMorts(mort)
                self.updateGame()
                if (self.isFinished() == False):
                    await self.interface.mettreAJour(self)
                    self.prochainRole="Village"
                    mort = await self.voteVillage()
                    await self.revelerMorts(mort)
                    self.updateGame()
            i = i + 1
        await self.interface.mettreAJour(self)
        await self.victoire()

    #Détermine la victoire
    async def victoire(self):
        if (len(self.alive) == 0):
            await self.interface.afficher("\nPersonne a gagné")
        elif (len(self.LG) == 0):
            await self.interface.afficher("\nLes Villageois ont gagné!")
        elif (len(self.vill) == 0):
            await self.interface.afficher("\nLes Loups-Garous ont gagné!")

    #Determine si la partie de LG est finie
    def isFinished(self):
        if (len(self.LG) == 0 or len(self.vill) == 0):
            return (True)
        else:
            return (False);

    #Effectue le vote du Village
    async def voteVillage(self):
        vote = await self.interface.faireVote(self, self.alive, self.alive)
        if (len(vote) == 1):
            await self.interface.afficher("\nLe Village a décidé d'éliminer " + vote[0].nom + " et leur sentence est irrévocable")
            return (vote)
        else:
            await self.interface.afficher("\nSecond tour de vote")
            vote = await self.interface.faireVote(self, self.alive, vote)
            if (len(vote) == 1):
                await self.interface.afficher("\nLe Village a décidé d'éliminer " + vote[0].nom + " et leur sentence est irrévocable")
                return (vote)
            else:
                await self.interface.afficher("\nLe Village ne s'est pas mis d'accord : Aucun bûcher")
        return ([])

    #Effectue le vote des LG
    async def voteLG(self):
            vote = await self.interface.faireVote(self, self.LG, self.alive)
            if (len(vote) == 1):
                # Pour la version web il ne faut l'afficher que pour les lg
                await self.interface.afficherPourLeslg("\nLes Loups-Garous ont décidés de manger " + vote[0].nom + "\n")
                return (vote)
            else:
                await self.interface.afficherPourLeslg("\nLes Loups-Garous ne se sont pas mis d'accord et ne mangeront personne\n")
                return ([])

    #Revele les morts de la nuit et les morts du vote
    async def revelerMorts(self, mort):
        for player in mort:
            await player.mourir(self)

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

    def aliveToStr(self):
        alive=self.alive
        aliveStr=[]
        for p in alive:
            aliveStr.append(p.__str__())
        return aliveStr

    def getJour(self):
        return self.jour

    #Affiche tout les joueurs
    async def printAllJoueur(self, playerbase):   
        for player in playerbase: 
            await player.printJoueur(self)

    #Fonction interne de MaJ
    def updateGame(self):
        self.alive = self.getAlive(self.playerbase)
        self.LG = self.getLG(self.alive)
        self.vill = self.getVillage(self.alive)

    def JoueursAvecRole(self,role):
        ret=[]
        for player in self.playerbase:
            if(player.role==role):
                ret.append(player)
        return ret
