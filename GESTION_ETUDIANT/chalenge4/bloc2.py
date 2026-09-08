# 1 - Distinguer attributs publics, protégés (_attr) et privés (__attr)

class CompteBancaire:
    def __init__(self,name,solde):
        self.name = name
        self.__solde = solde
        
compte = CompteBancaire("Ali", solde=100)
compte.solde
compte.solde = 5000
# 2- Exposer un attribut privé en lecture seule via @property
# 3 - Valider une donnée avant de modifier l’état interne d’un objet
# 4 - Utiliser @staticmethod pour une fonction utilitaire liée à la classe mais indépendante d’une
# instance
# 5 - Utiliser @classmethod pour manipuler un attribut de classe
# 6 - Différencier un membre de classe (partagé) d’un membre d’instance (propre à l’objet)