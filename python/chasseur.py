#Pas encore en etat de marche
class Chasseur(object):
    """docstring for Chasseur."""
    def __init__(self):
        super(Chasseur, self).__init__()

    def devoile(self):
        return ("Chasseur");

    def pouvoir(self, partie):
        partie.interface.afficher(partie.alive)
        partie.interface.afficher("Tirer sur qui? (index)")
        choix = partie.interface.faireChoix(partie.alive)
        partie.interface.afficher("Le chasseur entraine dans sa mort " + choix.nom)
        choix.mourir(partie)
