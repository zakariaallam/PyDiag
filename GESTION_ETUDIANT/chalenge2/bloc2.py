# 1 - Fonction vendre(stock, produit, quantite) avec vérification de disponibilité
# stock = {"pommes": 50, "bananes": 30, "oranges": 0}

# def vendre(stock, produit, quantite):
#     if produit not in stock:
#         return f"produit not in stock "
    
#     if stock[produit] < quantite:
#         return f"Stock insuffisant pour {produit}"
       
#     stock[produit] -= quantite
    
#     return    f"Vente enregistree : {quantite} {produit}"

        
    
# print(vendre(stock, "pommes", 20))
# print(vendre(stock, "oranges", 5))
    
# 2 -  Fonction produits_epuises(stock)

# stock = {"pommes": 30, "bananes": 0, "oranges": 0, "kiwis": 12}

# def produits_epuises(stock):
#     if not stock:
#         return []
    
#     produit = next(iter(stock))
#     quantite = stock.pop(produit)
#     if quantite == 0:
#         return [produit] + produits_epuises(stock)
#     else:
#         return produits_epuises(stock)
# print(produits_epuises(stock))    

# 3 - Agrégation par clé à partir d’une liste de commandes

# commandes = [
# {"client": "Ali", "produit": "pommes", "quantite": 5},
# {"client": "Sara", "produit": "bananes", "quantite": 10},
# {"client": "Ali", "produit": "oranges", "quantite": 2},
# ]


# new_command = {}
# for command in commandes:
#     if command["client"] not in new_command:
#         new_command[command["client"]] = command["quantite"]
#     else:
#         new_command[command["client"]] += command["quantite"]

# print(new_command)        

# 4 - Inversion d’un dictionnaire (clés ↔ valeurs)

d = {"a": 1, "b": 2, "c": 3}

