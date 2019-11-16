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

	async def envoyerMessage(self,message):
		await self.ws.send(message)
