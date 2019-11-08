import partie as p
import intCons as IC

interface = IC.IntCons()
joueur = ["Remi", "Thomas", "Samuel", "Hugo", "Chollet", "Arnaud"]
role = ["LG", "SV", "Voyante", "LG" , "SV", "Chasseur"]
partie = p.Partie(interface, joueur, role)
partie.playGame()
