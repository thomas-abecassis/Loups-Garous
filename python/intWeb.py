import asyncio

class IntWeb(object):
    """docstring for IntWeb."""
    def __init__(self,ws):
        self.webSocket=ws
        super(IntWeb, self).__init__()

    async def afficher(self, message):
        print (message)
        await self.webSocket.majChat(message)
        
    def mettreAJour(self, partie):
        partie.updateGame()

    async def faireChoix(self, list):
        choix=await self.webSocket.getChoix()
        print("je fais un choix")
        choix = int(choix)
        while (choix >= len(list) or choix < 0):
            choix = int(input)
        choix = list[choix]
        return (choix)

    async def faireVote(self, partie, votant, list):
        vote = []
        for player in votant:
            vote.append(await player.voter(partie, list))
        vote =  partie.majorite(vote)
        return (vote)


