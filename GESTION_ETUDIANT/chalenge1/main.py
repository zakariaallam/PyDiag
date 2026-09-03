# Etudiants = []

# def notes(etudiant):
#     i=1
#     while i<=3:
#         note = float(input(f"entre la note {i}: "))
#         coefficient = float(input(f"entre le coefficient de cette note: "))
#         etudiant["note"].append(note)
#         etudiant["coefficients"].append(coefficient)
#         i= i+1


# def moyen(etudiant):
#     somme = 0
#     soome_coeffisients = 0
#     for i ,note in enumerate(etudiant['note']):
#         somme += note * etudiant['coefficients'][i]
#         soome_coeffisients += etudiant['coefficients'][i]
    
#     return somme/soome_coeffisients

# def mention(moyen):
#     if moyen < 10:
#         return "Insuffisant"
#     if moyen >= 10 and moyen < 12:
#         return "Passable"
#     if moyen >= 12 and moyen < 14:
#         return "Bien"
#     if moyen >= 14:
#         return "Trea Bien"
    
# def affichage():
#     if len(Etudiants) == 0:
#         print("Aucun Etudiant")
#         return
#     for etudiant in Etudiants:
#         print(f"Nom : {etudiant['nom']}")
#         print(f"prénom : {etudiant['prenom']}")
#         print(f"moyen : {moyen(etudiant)}")
#         print(f"mention : {mention(moyen(etudiant))}")
    
# def Ajoute():
#     name_etudiant = input("Nom: ")
#     prenom_etudiant = input("prénom: ")
#     etudiant = {
#         'nom' : name_etudiant,
#         'prenom' : prenom_etudiant,
#         'note' : [],
#         'coefficients' : []
#     }
#     notes(etudiant)
#     Etudiants.append(etudiant)

# def regrouper_par_mention():
#     regroup = {}
#     for e in Etudiants:
#         moyenne = moyen(e)
#         mentione = mention(moyenne)
#         if mentione not in regroup:
#             regroup[mentione] = []
#         regroup[mentione].append(e | {"moyenne": 12.0})
        
        
#     Affichier_gegroup(regroup)  
    
# def Affichier_gegroup(regroup):
#     for k , v in regroup.items() :
#         print(f"{k} : {v}")
        
# def menu():
#     while True:
#         print("\n========================")
#         print("     GESTION ETUDIANT   ")
#         print("========================")
#         print("1. Ajouter étudiant")
#         print("2. Afficher classemen")
#         print("3. structures")
#         print("4. Quitter")    

#         choix = input("entrer votre choix: ")
        
#         match choix:
#             case "1":
#                 Ajoute()
#             case "2":
#                 affichage()
#             case "3":
#                 regrouper_par_mention()
#             case "4":
#                 print("Au revoir !")
#                 break            
   
# menu()   

groupe_a = {
"Karim": {"moyenne": 12.0, "mention": "Bien"},
}
groupe_b = {
"Karim": {"moyenne": 15.0, "mention": "Bien"},
"Sara": {"moyenne": 17.0, "mention": "Tres bien"},
}

groupe_c = {}

for name1 in groupe_a.keys():
    for name2 in groupe_b.keys():
        if name1 == name2 :
            groupe_c[name1] = name1 | name2
            
            