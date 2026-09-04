# 1 - Agrégation d’une liste de ventes vers un dictionnaire de totaux
# 2 - Recherche du produit le plus vendu
# 3 - Extraction d’un set de produits distincts

# ventes = [
#     {"produit": "pommes", "montant": 120},
#     {"produit": "bananes", "montant": 80},
#     {"produit": "pommes", "montant": 45},
#     {"produit": "oranges", "montant": 60},
#     {"produit": "bananes", "montant": 30},
# ]

# total_par_produit = {}

# for vente in ventes:
#     produit = vente["produit"]
#     montant = vente["montant"]

#     if produit in total_par_produit:
#         total_par_produit[produit] += montant
#     else:
#         total_par_produit[produit] = montant

# print(total_par_produit)

# 4 - Fusion de deux inventaires avec addition des quantités communes


# def fusionner_inventaires(inv1, inv2):
#     resultat = inv1.copy()

#     for produit, quantite in inv2.items():
#         if produit in resultat:
#             resultat[produit] += quantite
#         else:
#             resultat[produit] = quantite

#     return resultat


# inv1 = {"pommes": 20, "bananes": 15}
# inv2 = {"bananes": 10, "kiwis": 5}

# print(fusionner_inventaires(inv1, inv2))




# 5 - Mini-challenge final combinant listes, dicts imbriqués et sets

# etudiants = [
#     {"nom": "Ali", "matieres": {"maths": 14, "physique": 12}},
#     {"nom": "Sara", "matieres": {"maths": 18, "physique": 16, "svt": 15}},
#     {"nom": "Lina", "matieres": {"maths": 9, "physique": 11}},
# ]

# 1. Moyenne par étudiant
# moyennes_etudiants = {}

# for etudiant in etudiants:
#     nom = etudiant["nom"]
#     notes = etudiant["matieres"].values()

#     moyenne = sum(notes) / len(notes)
#     moyennes_etudiants[nom] = moyenne

# print("Moyenne par étudiant :")
# for nom, moyenne in moyennes_etudiants.items():
#     print(nom, ":", round(moyenne, 2))


# 2. Matières enseignées
# matieres_enseignees = set()

# for etudiant in etudiants:
#     for matiere in etudiant["matieres"]:
#         matieres_enseignees.add(matiere)

# print("Matières enseignées :", matieres_enseignees)


# 3. Notes par matière
# notes_par_matiere = {}

# for etudiant in etudiants:
#     for matiere, note in etudiant["matieres"].items():

#         if matiere not in notes_par_matiere:
#             notes_par_matiere[matiere] = []

#         notes_par_matiere[matiere].append(note)

# print("Notes par matière :")
# for matiere, notes in notes_par_matiere.items():
#     print(matiere, ":", notes)


# 4. Meilleure matière
# moyennes_matieres = {}

# for matiere, notes in notes_par_matiere.items():
#     moyenne = sum(notes) / len(notes)
#     moyennes_matieres[matiere] = moyenne

# meilleure_matiere = max(
#     moyennes_matieres,
#     key=moyennes_matieres.get
# )

# print(
#     "Meilleure matière :",
#     meilleure_matiere,
#     f"({moyennes_matieres[meilleure_matiere]:.2f})"
# )


