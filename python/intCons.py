class IntCons(object):
    """docstring forIntCons."""
    def __init__(self):
        super(IntCons, self).__init__()

    def afficher(self, message):
        print(message)

    def mettreAJour(self, partie):
        partie.updateGame()

    def faireChoix(self, list):
        choix = int(input())
        while (choix >= len(list) or choix < 0):
            choix = int(input())
        choix = list[choix]
        return (choix)

    def faireVote(self, partie, votant, list):
        vote = []
        for player in votant:
            vote.append(player.voter(partie, list))
        vote = partie.majorite(vote)
        return (vote)
