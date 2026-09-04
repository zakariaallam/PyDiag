# 1 - Différencier une erreur de syntaxe d’une exception (runtime)

# try:
#     extrait_a = "print(’bonjour’"
#     extrait_b = "resultat = 10 / 0"
#     extrait_c = "valeurs = [1, 2, 3]\nprint(valeurs[5])"
    
# except ZeroDivisionError:
#     print("")
# except IndexError:
#     print("")
    
# 2 - Situer une exception dans la hiérarchie (BaseException, Exception)
# def division_securisee(a, b):
#     try:
#         print(a/b)
#     except:
#         print("Erreur : division par zero impossible")
   
# division_securisee(10, 2)
# division_securisee(10, 0)

# 3 - Écrire un bloc try/except basique

# def convertir_entier(valeur):
     
#     try:
#         print(int(valeur))
#     except ValueError:
#         print("Erreur : 'abc' n’est pas un entier valide")
        
# convertir_entier("42")
# convertir_entier("abc")

# 4 - Intercepter une exception spécifique (ZeroDivisionError, ValueError...)
# notes = [12, 15, 9]

# def acceder_element(liste, index):
    
#     try:
#         print(liste[index])
#     except IndexError:
#         print(f"Erreur : index {index} hors limites (taille de la liste : {len(liste)}).")    
    
# acceder_element(notes, 1)
# acceder_element(notes, 10)


# 5 - Intercepter plusieurs types d’exceptions dans un même bloc

# eleve = {"nom": "Sara", "age": 20}

# def acceder_cle(dictionnaire, cle):
#     try:
#         print(dictionnaire[cle])
#     except:
#         print(f"Erreur : la cle '{cle}' n’existe pas.")
        
# acceder_cle(eleve, "nom")
# acceder_cle(eleve, "email")

# 6 - Utiliser else et finally à bon escient

# def traiter_valeur(valeur):
#     try:
#         print(int(valeur))
#     except ValueError:
#         print(f"Erreur : {valeur} n’est pas convertible.")
#     finally:
#         print("Traitement termine")    
            

# traiter_valeur("8")
# traiter_valeur("x") 

  