# 1 - Ouvrir un fichier avec open() et connaître les modes (r, w, a, x, b, +)
def ecrire_liste_courses(chemin, articles):

    fichier = open(chemin,"w",encoding="utf-8")
    for article in articles:
        fichier.write(article + "\n")       
    fichier.close()

articles = ["pommes", "lait", "pain"]

ecrire_liste_courses("courses.txt", articles)

# 2 - Écrire dans un fichier avec write() / writelines()
# 3 - Différencier le mode w (écrasement) du mode a (ajout)
# 4 - Lire un fichier avec read(), readline(), readlines()
# 5 - Parcourir un fichier ligne par ligne avec une boucle
# 6 - Utiliser le context manager with pour une fermeture automatique