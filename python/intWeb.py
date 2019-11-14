import asyncio

class IntWeb(object):
    """docstring for IntWeb."""
    def __init__(self,ws):
        self.webSocket=ws
        super(IntWeb, self).__init__()

    async def afficher(self, message):
        await self.webSocket.majChat(message)
        
    async def mettreAJour(self, partie):
        partie.updateGame()
        await self.webSocket.majEtat(getEtatsJoueurs(partie))

    async def faireChoix(self, list):
        choix=await self.webSocket.getChoix()
        print("je fais un choix")
        try :
            choix = int(choix)
        except :
            choix=-1
        while (choix >= len(list) or choix < 0):
            choix=await self.webSocket.getChoix()
            try :
                choix = int(choix)
            except :
                choix =-1
            await asyncio.sleep(0.5)
        choix = list[choix]
        return (choix)

    async def faireVote(self, partie, votant, list):
        vote = []
        for player in votant:
            vote.append(await player.voter(partie, list))
        vote =  partie.majorite(vote)
        return (vote)

def getEtatsJoueurs(partie):
    village=partie.playerbase
    l=[]
    for player in village : 
        if (player.vivant):
            l.append([player.role.__class__.__name__,True])
        else :
            l.append([player.role.__class__.__name__,False])
    return l