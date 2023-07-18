
#  la fonction lambda in pytho 

'''
lambda arguments: expression

Expliquons cela :

# lambda : est le mot-clé qui indique à Python que nous définissons une fonction lambda.

# arguments : sont les entrées ou paramètres que la fonction lambda prend.
            Vous pouvez avoir plusieurs arguments séparés par des virgules, ou aucun du tout.
# expression : est le calcul ou l'opération que la fonction lambda effectue. 
             C'est généralement une seule ligne de code qui renvoie une valeur.


'''

'''
est une anonyme function qui ne possède pas de nom. Elle peut être utilisée
 pour définir des fonctions plus simples et courtes, en particulier lors
qu'on veut utiliser une fonction dans un contexte où il n'y aura
jamais besoin d'enregistrer le résultat dans une variable ou passer par l'appel à une autre
fonction..
Par exemple :
```python
 
double = (lambda x:x*2) # on définit double comme ét
ant une lambda expression avec paramètre x
print(double(5))   # affichera "10"

car doubler prend un entier donné en argument et retourne sa valeur multiplié par deux
'''

result = lambda loop :loop * 3
print(result(5))  #--->  15 



# Vous pouvez également utiliser des lambdas directement sans les assigner à une variable. 
# Par exemple, vous pouvez passer une fonction lambda comme argument à une autre fonction :

nombres = [1, 2, 3, 4, 5]
carres = map(lambda x: x ** 2, nombres)
print(list(carres))  # Résultat : [1, 4, 9, 16, 25]

# Dans cet exemple, nous avons utilisé la fonction map() avec une fonction lambda
#  pour élever au carré chaque élément de la liste nombres.
