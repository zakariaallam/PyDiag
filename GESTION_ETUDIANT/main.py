name_etudiant = input("Nom: ")
prenom_etudiant = input("prénom: ")
notes_etudiant = []
coefficients_notes = []

def notes():
    i=1
    while i<=3:
        note = float(input(f"entre la note {i}: "))
        coefficient = float(input(f"entre le coefficient de cette note: "))
        notes_etudiant.append(note)
        coefficients_notes.append(coefficient)
        i= i+1


def moyen(notes_etudiant):
    somme = 0
    soome_coeffisients = 0
    for i ,note in enumerate(notes_etudiant):
        somme += note * coefficients_notes[i]
        soome_coeffisients += coefficients_notes[i]
    
    return somme/soome_coeffisients

def mention(moyen):
    if moyen < 10:
        return "Insuffisant"
    if moyen >= 10 and moyen < 12:
        return "Passable"
    if moyen >= 12 and moyen < 14:
        return "Bien"
    if moyen >= 14:
        return "Trea Bien"
    
def affichage():
    print(f"Nom : {name_etudiant}")
    print(f"prénom : {name_etudiant}")
    print(f"moyen : {moyen(notes_etudiant)}")
    print(f"mention : {mention(moyen(notes_etudiant))}")
    
notes()
affichage()    