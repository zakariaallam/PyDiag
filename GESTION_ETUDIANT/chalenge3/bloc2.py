# 1 - Lever une exception avec raise
# def verifier_age(age):
#     if age < 0:
#         raise ValueError(f"l’age ne peut pas etre negatif ({age}).")
#     print(f"Age valide : {age}")

# try:
#     verifier_age(25)
#     verifier_age(-3)
# except ValueError as e:
#     print(f"{e}")  


# 2 - Relancer une exception interceptée (raise sans argument)

# def traiter_liste_de_valeurs(valeurs):
#     for valeur in valeurs:
#         try:
#             nombre = int(valeur)
#             print(nombre)
#         except ValueError:
#             print(f'Log : valeur "{valeur}" invalide, exception relancee.')
#             raise


# traiter_liste_de_valeurs(["3", "9", "x", "5"])

# 3 - Créer une exception personnalisée par héritage de Exception
# class StockInsuffisantError(Exception):
#     def __init__(self, produit, demande, disponible):
#         message = (
#             f'Stock insuffisant pour "{produit}" '
#             f'(demande : {demande}, disponible : {disponible})'
#         )
#         super().__init__(message)



# 4 - Utiliser une exception personnalisée dans une fonction métie

# def retirer_stock(stock, produit, quantite):
#     disponible = stock.get(produit, 0)

#     if quantite > disponible:
#         raise StockInsuffisantError(produit, quantite, disponible)

#     stock[produit] -= quantite
#     print(f"Retrait effectue : {quantite} {produit}.")


# stock = {"pommes": 20, "bananes": 4}

# try:
#     retirer_stock(stock, "pommes", 5)
#     retirer_stock(stock, "bananes", 10)
# except StockInsuffisantError as e:
#     print(f"{e}")    