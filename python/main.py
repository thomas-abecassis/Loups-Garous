import partie as p

joueur = ["Remi", "Thomas", "Samuel", "Hugo", "Chollet", "Arnaud"]
role = ["LG", "SV", "Voyante", "LG" , "SV", "Chasseur"]
partie = p.Partie(joueur, role)
partie.playGame()
