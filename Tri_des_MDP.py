fichier = open("richelieu.txt",'rt')
texte = fichier.read()
liste = texte.split("\n")
print(liste[0])