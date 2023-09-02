#nous pouvons utiliser plusieurs fonctions dans le tableau pour faciliter les taches 

tableau = ['python','Php','Css','Html']


#une function pour ajouter un element dans un tableau par utiliser le append()

tableau.append('Sass')
print(tableau)#-----> ['python', 'Php', 'Css', 'Html', 'Sass']
# il faut savoir que la fonction append() ajoute l'element par defuat a la fin du tableau 



#une fonction pour inserer un element dans un endroit spécifique dans le tableau,
#c'est la fonction insert() qui prend 2 parametres : index et valeur à insérer

tableau.insert(2,'Javascript')
print(tableau)  #--->['Javascript', 'Python', 'Php', 'Css', 'Html', 'Sass']


#nous pouvons fuisonner un tableau avec un autre afin de pouvoir avoir un seul 
#pour faire cela, on utilise la fonction .extend()

#par exemple  :


tableau2 = [1,2,3,4,5,12]
tableau.extend(tableau2)

print (tableau)


# il y a aussi une autre maniere pour les fuisonner en utilisant l'opérateur +
#par exemple:

#liste_a= [0,1,2,'Python','Javascript']

#liste_b=[789,890,[1,2]]

#liste_c =liste_a + liste_b
 
#print (liste_c) # -----> [0, 1, 2, 'Python', 'Javascript', 789, 890, [1, 2]]


#une fonction .sort() pour mettre le tableau par ordre 
#par exemple 

tableau2 = [5,4,6,3,2,8,0,9,7]

#tableau2.sort()
#print(tableau2) #-----> [0, 2, 3, 4, 5, 6, 7, 8, 9]

# la fonction .reversed() permet de reverse les éléments dans un tableau 
# par exemple : 

tableau2.reverse()
print(tableau2) #----->[7, 9, 0, 8, 2, 3, 6, 4, 5]


#fonction .clear() c'est pour enlever tous les elemnts se trouvent dans mon tableau 

#fonction .remove() c'est pour supprimer un elemnt dans notre tableau 


#la méthode count permet d'afficher combien fois apparaît un élément donné dans notre tableau
#tab = ['python', 'php', 'javascript', 'html', 'css', 'java', 'ruby', 'go', 'rust']
#print('nombre de "r" dans ce tableau:', tab.count("r")) 


