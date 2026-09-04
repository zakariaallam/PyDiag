# 1 - max min
 
# notes = [12, 18, 7, 15, 9, 20, 3, 14]
# max = notes[0]
# min = notes[0]
# for i in range(len(notes)):
#    if max < notes[i]:
#        max = notes[i] 
    
#    if min > notes[i]:
#        min = notes[i]
    
# print(f"Note max : {max}")       
# print(f"Note min : {min}")       
       
# 2 - Filtrer une liste selon un seuil

# notes = [8, 14, 6, 17, 11, 20]

# notes_seuil = []
# seuil = 12

# for note in notes:
#     if note >= 12:
#         notes_seuil.append(note)
# print(notes_seuil)   


# 3 - Compter les occurrences d’éléments sans Counter

# from collections import defaultdict
# fruits = ["pomme", "banane", "pomme", "orange", "banane", "pomme"]
# fruit_object = defaultdict(int)
# for fruit in fruits:
#     if  fruit not in fruit_object:
#         fruit_object[fruit] = 0
    
#     if fruit in fruit_object:
#         fruit_object[fruit] += 1        

# print(fruit_object)     

# 4 - Inverser une liste sans reverse() ni [::-1]
   
liste = [1, 2, 3, 4, 5]

# def reverse(list):
#    if not list:
#        return list
   
#    return [list[-1]] + reverse(list[:-1])  

# print(reverse(liste))

# 5 - Fusionner deux listes triées sans sorted()

# liste_a = [1, 4, 7]
# liste_b = [2, 3, 8, 9]

# def Fusionner(liste_a,liste_b):
#     if not liste_a:
#         return sorted(liste_b)
    
#     if not liste_b:
#         return sorted(liste_a)
    
#     max_a = max(liste_a)
#     max_b = max(liste_b)
    
#     if max_a > max_b:
#         liste_a.remove(max_a)
#         return [max_a] + Fusionner(liste_a,liste_b)
#     else:
#         liste_b.remove(max_b)
#         return [max_b] + Fusionner(liste_a,liste_b)
           
# print(Fusionner(liste_a,liste_b))      


# 6 - Utiliser une compréhension de liste

# nombres = [3, 12, 7, 25, 8, 19, 2]

# def comprehension(list):
    
#     if not list :
#         return list

#     if list[0]%2 != 0:
#         return comprehension(list[1:])
    
#     else :
#         return [list[0]*list[0]] + comprehension(list[1:])
    
# print(comprehension(nombres))    