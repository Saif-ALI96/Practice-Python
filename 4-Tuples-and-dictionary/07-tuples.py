#pour appeler les tuples , on doit mettre les parenthèses après.
# les tuples sont un peu près comme les list sauf , on peut pas les modifier une fois qu'elle est créée !
#par exemple :

tuple1 = (34,"<NAME>",3546789)
tuple1[0] = 5 # ----> TypeError: 'tuple' object does not support item assignment

print(tuple1)
 #on affiche le tuple ici, il est un objet donc pas de point d'interrogation à la fin.

# donc on utilise les tuples pour les element qu'on veut jamais les modifier comme on fait avec la list (tableau)
