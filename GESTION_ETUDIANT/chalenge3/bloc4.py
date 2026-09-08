# 1 - Combiner try/except avec l’ouverture d’un fichier

# def lire_fichier_securise(chemin):
#     try:
#         with open(chemin, "r") as fichier:
#             return fichier.readlines()
#     except FileNotFoundError:
#         print(f'Erreur : le fichier "{chemin}" n’existe pas.')
#         return None


# 2 - Gérer FileNotFoundError et PermissionError lors d’un accès fichier
# 3 - Utiliser finally pour garantir la fermeture d’un fichier
# 4 - Lire un fichier CSV et gérer les lignes mal formées
# 5 - Lire/écrire un fichier JSON avec gestion d’erreurs
# 6 - Mini-challenge final combinant fichiers, exceptions et structures de données