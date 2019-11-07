class IntWeb(object):
    """docstring for IntWeb."""
    def __init__(self):
        super(IntWeb, self).__init__()

    def afficher(self, message):
        pass
        #Code pour envoyer un message sur le tchat

    def mettreAJour(self, partie):
        #Update la data de la partie en background
        partie.updateGame()
        #Envoyer les infos sur le web
