import asyncio
import json
import logging
import websockets
import partie as p
import intCons as IC
import intWeb as IW
import time

class Client(object):

	def __init__(self,joueur,ws):
		self.joueur=joueur
		self.ws=ws

	def memeWs(self,ws):
		return self.ws==ws

	def estLoupGarou(self):
		return self.joueur.role.devoile()=="Loup-Garou"

	def getNom(self):
		return self.joueur.nom

	def memeRole(self,role):
		return self.joueur.role==role

	def memeJoueur(self,joueur):
		return self.joueur==joueur

	def memeNom(self,Nom):
		return self.joueur.nom==Nom


	async def envoyerMessage(self,message):
		await self.ws.send(message)
