# on quelque function qui peuvent être utile for nous, si nous voulons modifier le contenu 
# par exemple 

# 01 le function// .upper ----> pour mettre les lettre en Majuscul 
# 02 le function// .isupper() ----> pour voir si la caractére en Majuscul. le resultat est toujours
#  en boolean, c'est à dire (True ou False).

# 03 le function// .lower() ----> pour mettre les lettre en Minuscul
# 04 le function// .islower() ----> pour voir si la caractère en Miniscul. le resultat est toujours
#  en boolean, c'est à dire (True ou False).

# 05 le function// LEN() ----> pour mettre la longueur de la chaîne de caractére

# 06 le function// SUBSTR() ----> pour extraire une partie de la chaîne de caractére

# 07 le function// TRIM() ----> pour supprimer les espaces en début et fin
#   de la chaîne de caractére

# 08 le function// REPLACE() ----> pour remplacer une chaîne de caractére par
#   une autre chaîne de caractére

#09 le function// .capitalize() -----> pour mettre la premiere lettre seulement en Majuscul

#10 le function// .title() ----> pour mettre  la premiere lettre de chaque mot en Majuscul

#11 le function// .split() -----> pour separer les objets comme dands le tableau dans 
#  double virgule ("").

#12 le function// .rsplit() -----> c'est le même fonctionnement de .split(), 
#   mais il va partir de la droite vers la gauche.


test = "hello"
print(test.upper()) # on va avoir "HELLO" en Majuscul
print(test.islower()) # on va avoir True


test1 = "HELLO"
print(test1.lower()) # on va avoir "hello" en Minuscul
print(test1.isupper()) # on va avoir True


test2 = "hello"
print(len(test2)) # on va avoir 5 caractére


test3 = "hello"
print(test3[0]) # on va avoir "h"


test4 = "hello"
print(test4[0:3]) # on va avoir "hel


test5 = " hello "
print(test5.strip()) # on va avoir "hello"

