# the loop (boucle) in python ce sont les ---for-- et ----while---


#En programmation, les boucles sont utilisées pour exécuter de manière répétée un bloc de code jusqu'à ce qu'une certaine condition soit satisfaite. 
#Elles vous permettent d'automatiser des tâches répétitives et de traiter des collections de données.
# Python propose deux principaux types de boucles : la boucle "for" (pour) et la boucle "while" (tant que).

# La première ---for -- 
#est plus efficace lorsque le nombre d’éléments à par courir est connu avant l’exécution du script ; 
# celle-ci est mieux adaptée aux listes ou tuples. Cependant elle ne peut pas être interrompue en particulier si on veut revenir sur
#un élément précédent dans une liste.

for test1 in 'HELLO WORLD':
    print(test1)
  #----> H
        #E
        #L
        #L
        #O
 
        #W
        #O
        #R
        #L
        #D

   # print('FIN')
   # break #on sort de la boucle si on veut, cela permet de ne
#pas avoir un code qui s'execute toujours

test2 = ['hello','world','bonjour']
for exemple in test2:
    print(exemple)
     #---> hello
         # world
         # bonjour



test3 = [3,5,7,8,9,90,]
print(len([x for x in test2]))









