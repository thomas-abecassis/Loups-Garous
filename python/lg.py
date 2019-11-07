import role

class LoupGarou(object):
    """docstring for LoupGarou."""
    def __init__(self):
        super(LoupGarou, self).__init__()

    def manger(self, joueur, partie):
        partie.interface.afficher(partie.vill)
        partie.interface.afficher("Voter contre (index): ")
        choix = partie.interface.faireChoix(partie.vill)
        partie.interface.afficher(joueur.nom + " veux manger " + choix.nom)
        return (choix)

    def devoile(self):
        return ("Loup-Garou");

    def pouvoir(self, partie):
        pass
