class IntCons(object):
    """docstring forIntCons."""
    def __init__(self):
        super(IntCons, self).__init__()

    async def afficher(self, message):
        print(message)

    def mettreAJour(self, partie):
        partie.updateGame()

    async def faireChoix(self, list):
        choix = int(input())
        while (choix >= len(list) or choix < 0):
            choix = int(input())
        choix = list[choix]
        return (choix)

    async def faireVote(self, partie, votant, list):
        vote = []
        for player in votant:
            vote.append(await player.voter(partie, list))
        vote = partie.majorite(vote)
        return (vote)
