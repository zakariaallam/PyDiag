# 1 - Intersection, union et différence de deux ensembles

# atelier_python = ["Ali", "Sara", "Lina", "Karim"]
# atelier_java = ["Sara", "Omar", "Lina", "Yasmine"]


# atelier_set = set(atelier_java + atelier_python)
# double = set()

# for x in atelier_python:
#     if x in atelier_java:
#         double.add(x)

# print(double)

# 2 - Détection de doublons avec un set

# liste_1 = ["Ali", "Sara", "Lina"]
# liste_2 = ["Ali", "Sara", "Ali"]

# set_liste_1 = set(liste_1)
# set_liste_2 = set(liste_2)

# if len(liste_2) > len(set_liste_2):
#     print("True")
# else:
#     print("False")    

# 3 - Construction d’un set unique à partir de listes imbriquées

tags_articles = [
    ["python", "web", "api"],
    ["python", "data"],
    ["web", "css"],
]

tags_uniques = set()

for article in tags_articles:
    for tag in article:
        tags_uniques.add(tag)

print(tags_uniques)

# 4 - Comprendre les limites des sets (éléments non hashables) et l’alternative avec des tuples


