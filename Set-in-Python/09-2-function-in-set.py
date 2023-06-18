

#Les fonctions suivantes permettent de manipuler facilement nos sets :
#.union() permet de fuisonner deux sets en un seul
#add() permet d'ajouter un élément à un set existant ; 
# remove() permet de retirer un élément du set; 
# clear()efface tout le set ; copy() crée une copie d'un set ; 
# update() met à jour un set par rapport à un autre set; 
# pop() retourne un élément aléatoire du set ;
#  discard() retire un élément spécifique du set

#Exemples :

num1 = {1,2,4,8,9}
num2 = {8,9,3,5}
#print(num1.union(num2))
print(num1|num2) # une autre maniere pour fussionner les sets
#--> {1, 2, 4, 8, 9, 3, 5}

A = {10,'python',25}

A.update([67,65,23]) # on puet ajouter plusieurs elements en meme temps
# -----> {65, 67, 10, 'python', 23, 25}
#A.add(67)
# c'est la meme chose que .update() mais, on peut ajouter un seul element seulement 
# avec parantheses [] pour ajouter un element 
print(A)
#--> {67, 25, 10, 'python'}

A.discard(25) # c'est la meme fonctionnalite de .remove() mais l'agantage de celle ci,
#il ne nous affiche pas un message d'errure si on supprime un element qui n'existe pas dans notre set.
#  bien evidement c'est l'inverse que la fonctio remove()
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

