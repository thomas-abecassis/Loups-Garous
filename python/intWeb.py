import asyncio

class IntWeb(object):
    """docstring for IntWeb."""
    def __init__(self,ws):
        self.webSocket=ws
        super(IntWeb, self).__init__()

    async def afficher(self, message):
        await self.webSocket.majChat(message)
        
    def mettreAJour(self, partie):
        partie.updateGame()

    def faireChoix(self, list):
        choix = int(input())
        while (choix >= len(list) or choix < 0):
            choix = int(input())
        choix = list[choix]
        return (choix)

    async def faireVote(self, partie, votant, list):
        vote = []
        for player in votant:
            vote.append(await player.voter(partie, str(list)))
        vote =  partie.majorite(vote)
        return (vote)

def str(list):
    l=[]
    for p in list:
        l.append(p.__str__())
    return l
