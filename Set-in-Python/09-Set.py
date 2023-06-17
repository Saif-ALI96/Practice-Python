#LES SETS EN PYTHON
#Comme les dictionnaires, les sets sont des collections d'éléments non-ordonnées.

#Dans un set, chaque élément doit être unique et immuable , c’est-à- dire qu'il ne peut pas être modifié.

#On peut donc stocker des chaînes de caractères, des nombres et des tuples dans un set mais pas de listes ou de dictionnaires !

#En revanche, le set en lui-même peut être modifié ! On peut y ajouter des objets et aussi en supprimer.
#Les sets sont souvent utilisés pour contrôler les doublons et effectuer des opérations sur les ensembles comme 
#les unions, les différences, les intersections, etc.
#Exemple :

#a = {10,'python',25} #Crée une liste avec trois éléments uniques (10, 'python' and 25)

#print(type(a)) #---> <class 'set'>

#b= {'java','php'} #Crée une autre liste avec deux éléments uniques ('java'and 'php')
#print(type(b)) #---><class'set'>

#Les fonctions suivantes permettent de manipuler facilement nos sets :
#add() permet d'ajouter un élément à un set existant ; 
# remove() permet de retirer un élément du set; 
# clear()efface tout le set ; copy() crée une copie d'un set ; 
# update() met à jour un set par rapport à un autre set; 
# pop() retourne un élément aléatoire du set ;
#  discard() retire un élément spécifique du set

#Exemples :
A = {10,'python',25}

A.update([67])
print(A)
#--> {67, 25, 10, 'python'}
A.discard(25)
print(A)
#--> {67, 10, 'python'}
A.clear()
print(A)
#--> set{}

B=[10,25]
B.remove(25)
print(B)
#--> [10]
#La fonction len() renvoit le nombre d'objets contenus dans un set.
#Exemple :

C = {10,12,45,67,25}
print("Le nombre d'éléments dans mon set est:",len(C))
#--> Le nombre d'éléments dans mon set est: 5
