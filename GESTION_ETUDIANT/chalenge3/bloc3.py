# 1 - Ouvrir un fichier avec open() et connaître les modes (r, w, a, x, b, +)
# 2 - Écrire dans un fichier avec write() / writelines()

# def ecrire_liste_courses(chemin, articles):

#     fichier = open(chemin,"w",encoding="utf-8")
#     for article in articles:
#         fichier.write(article + "\n")       
#     fichier.close()

# articles = ["pommes", "lait", "pain"]

# ecrire_liste_courses("courses.txt", articles)


# 3 - Différencier le mode w (écrasement) du mode a (ajout)

# def ajouter_article(chemin, article):
#     with open(chemin, "a") as fichier:
#         fichier.write(article + "\n")

# ajouter_article("courses.txt", "oeufs")

# 4 - Lire un fichier avec read(), readline(), readlines()

# def lire_fichier(chemin):
#     with open(chemin, "r") as fichier:
#         return fichier.readlines()

# print(lire_fichier("courses.txt"))

# 5 - Parcourir un fichier ligne par ligne avec une boucle

# def compter_lignes(chemin):
#     compteur = 0
#     with open(chemin, "r") as fichier:
#         for ligne in fichier:
#             compteur += 1
#     return compteur

# print("Nombre de lignes :", compter_lignes("courses.txt"))

# 6 - Utiliser le context manager with pour une fermeture automatique