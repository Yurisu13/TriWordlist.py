with open("richelieu.txt",'rt') as fichier, open("Trichelieu.txt",'x') as new_fichier

texte = fichier.read()
liste = texte.split("\n")
print(liste[0])
