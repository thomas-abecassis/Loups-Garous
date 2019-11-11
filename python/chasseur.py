#Pas encore en etat de marche
class Chasseur(object):
    """docstring for Chasseur."""
    def __init__(self):
        super(Chasseur, self).__init__()

    def devoile(self):
        return ("Chasseur");

    async def pouvoir(self, partie):
        await partie.interface.afficher(partie.alive)
        await partie.interface.afficher("Tirer sur qui? (index)")
        choix = partie.interface.faireChoix(partie.alive)
        await partie.interface.afficher("Le chasseur entraine dans sa mort " + choix.nom)
        await choix.mourir(partie)
