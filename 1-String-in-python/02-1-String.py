# en string 
# on écrit le contenu dans un virgule ('') ou ("") pour le string

# PAR EXEMPLE

name = ('HELLO WORLD')
print(name)
name1 = ("HELLO WORLD")
print(name1)

# pour écrire un contenu assez long en string, on utilse le triple virgule (""")

test = (""" HELLO EVERY ONE , THIS IS A LONGUE TEST IN PYTHON WHEN WE USE THE EXEMPLE""")
print(test)

# pour écrire un contenu et aller a linge , on utilise le anti-slache (\n)

test1 = ("HELLO EVERY ONE \n THIS IS A LONGUE TEST IN PYTHON")
print(test1)


#pour cibler un caractère ou l'imprimer , on utilise un list [] pour cibler 
#un ou plusieurs

test2 = ("python is a programming language")
print(test2[0])
print(test2[0:6]) 
# un tableau commence toujours par Zéro et bien pas en commençant par 1
# par exemple comme le mot ---python-- c'est six caractéres, 
# donc de 0 a 5 mais attention pour afficher 
###################
# le dernier caractère on souhite afficher dans le mot (python),
#  nous deveons ajouter 1 de plus, du coup cela s'ecrit comme ca [0:6] ===> python

print(test2[-1])
# pour afficher le dernier carctere d'un tableau or list en englais, c'est par ecrire [-1]
# comme dans l'exemple ci-dessus
#  