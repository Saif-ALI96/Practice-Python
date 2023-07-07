#  LES FUNCTIONS EN PYTHON

#- Les fonctions sont des blocs de code qui peuvent être réutilisés plusieurs fois.
#Elles permettent d'éviter la duplication du code et donc une maintenance moins onerous مرهق pour les développeurs.

#Les fonctions ont deux parties :

#    Une partie interne appelée corps de fonction ou body of function
#    Un ensemble de paramètres entre parenthèses

#La syntaxe générale d'une fonction en Python se présente comme suit :

# def <nom_de_la_fonction>(<liste_des_paramètres>):
#     <corps>

# Le corps de notre fonction doit contenir au minimum une instruction return.
# Cette instruction permet de renvoyer une valeur à partir de notre fonction.

#par exemple
def myFunction(x,y):
    sum = x + y
    print(sum)
myFunction(6,8) # ---> 14

def presentation(name, age) :
    print('Hello : ' + name)
    print('your age is : ' + str(age) + ' years old')
presentation("John",25)
















# - La fonction peut prendre un nombre variable d’arguments, séparés par des virgules:
#def additionner(*args): # args est le nom que l'on attribue à cette liste contenant tous nos arguments
  #  resultat = sum(args)
   # print ("Le résultat est :",resultat)



# ### FONCTIONS ANONYMES
# Il existe également des fonctions anonymes, celle-ci ne possédant pas de nom mais uniquement une adresse
# Elle sert principalement aux travaux asynchrones.
# Pour créer une fonction anonyme il suffit de définir son corps puis de lui attribuer une adresse mémo
# Par exemple nous pouvons utiliser une fonction lambda sur une liste afin de calculer la moyenne des éléments de ce tableau
l=[30,57,9]
average=lambda x: sum(x)/len(x)
print("Moyenne:", average(l))
