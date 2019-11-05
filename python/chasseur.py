class Chasseur(object):
    """docstring for Chasseur."""
    def __init__(self):
        super(Chasseur, self).__init__()

    def devoile(self):
        return ("Chasseur");

    def pouvoir(self, alive):
        print(alive)
        choix = int(input("Sonder (index): "))
        while (choix >= len(alive) or choix < 0):
            choix = int(input("Sonder (index): "))
        sonde = alive[choix]
        print("Le chasseur entraine dans sa mort " + sonde)
        sonde.mourir()
