# 1 - Définir une classe et comprendre la différence classe / objet

class Livre:
    
    livres = []
    
    def __init__(self, titre,auth):
        self.titre = titre
        self.auth = auth
        self.desponible = True
    
    def __str__(self):
        
        return f"{self.titre} de {self.auth} -- desponible"    
    

# livre = Livre("Dune", "Frank Herbert")
# print(livre)

# 2 - Écrire un constructeur __init__ et comprendre le rôle de self

class Adherent:
    
    def __init__(self,nom):
        self.nom = nom
        self.length = 0
        
    def emprunter_livre(self,livre):
        if livre.desponible:
            livre.desponible = False
            livre.livres.append(livre)
            
        else:
            return f'Erreur : le livre "{livre.titre}" n’est pas disponible. '   
        
        self.length = len(livre.livres)
        
        
    def nombre_livres_empruntes(self):
        return self.length
    
    def rendre_livre(self,livre):
        livre.desponible = True
        livre.livres.remove(livre)
        self.length = len(livre.livres)
                
# livre = Livre("Dune", "Frank Herbert")
# ali = Adherent("Ali")
# ali.emprunter_livre(livre)
# print(livre)
# print(ali.nombre_livres_empruntes()) 
               
# 3 - Faire collaborer deux objets de classes différentes (un Adherent qui manipule un Livre)

# livre = Livre("Dune", "Frank Herbert")
# ali = Adherent("Ali")
# sara = Adherent("Sara")
# ali.emprunter_livre(livre)
# print(sara.emprunter_livre(livre))

# 4 - Créer plusieurs instances indépendantes de la même classe

ali = Adherent("Ali")
livre = Livre("Dune", "Frank Herbert")
print(livre)
ali.emprunter_livre(livre)
ali.rendre_livre(livre)
print(ali.nombre_livres_empruntes())