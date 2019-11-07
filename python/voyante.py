class Voyante(object):
    """docstring for Voyante."""
    def __init__(self):
        super(Voyante, self).__init__()

    def devoile(self):
        return ("Voyante");

    def pouvoir(self, partie):
        partie.interface.afficher(partie.alive)
        partie.interface.afficher("Sonder qui (index): ")
        choix = partie.interface.faireChoix(partie.alive)
        partie.interface.afficher("La voyante a sonde un " + choix.role.devoile())
