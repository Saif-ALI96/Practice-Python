# on quelque function qui peuvent être utile for nous, si nous voulons modifier le contenu 
# par exemple 

# 01 le function// UPPER() ----> pour mettre les lettre en Majuscul 
# 02 le function// LOWER() ----> pour mettre les lettre en Minuscul
# 03 le function// LEN() ----> pour mettre la longueur de la chaîne de caractére
# 04 le function// SUBSTR() ----> pour extraire une partie de la chaîne de caractére
# 05 le function// TRIM() ----> pour supprimer les espaces en début et fin
#   de la chaîne de caractére
# 06 le function// REPLACE() ----> pour remplacer une chaîne de caractére par
#   une autre chaîne de caractére

test = "hello"
print(test.upper()) # on va avoir "HELLO" en Majuscul


test1 = "HeLLo"
print(test1.lower()) # on va avoir "hello" en Minuscul


test2 = "hello"
print(len(test2)) # on va avoir 5 caractére


test3 = "hello"
print(test3[0]) # on va avoir "h"


test4 = "hello"
print(test4[0:3]) # on va avoir "hel


test5 = " hello "
print(test5.strip()) # on va avoir "hello"