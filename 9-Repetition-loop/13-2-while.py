
#La seconde ----while---  permet de contrôler la fin de la boucle avec une variable qui doit toujours avoir comme valeur True.
# Elle n’a pas besoin d’avoir connaissance du nombre d’itérations possibles car 
#il faudrait seulement compter au fur et à mesure de chaque itération la valeur de cette variable.

#Exemple:

#index = 0
#while index <= 6 :
#    print(index)
#    index = index + 1
#0
#1
#2
#3
#4
#5
#6

#On peut aussi utiliser des conditions dans les while pour s'arrêter avant
#d'atteindre un certain point (on parle alors d'un break
test =0
while test <= 7 : #condition
    test += 1
    if test == 5:
        continue # c'est pour sauter la condition que l'on indiquer 
    print(test)
    # ----> 1 2 3 4 6 7 


test3 = 2
while test3 < 8 : # on utilise le mot clé "
    test3+=1
    if test3 == 5:
        break #c'est pour arrêter la boucle quand on veut
    print(test3)
 # ----> 3 4 
 
  
    



