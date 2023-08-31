#  ajourd'hui on va utiliser le formating en python


#  la première  methode 

name = 'HassaN'
age = 17
country = 'france'

print("Hello my name is {} and I am {}, born in {}".format(name,age,country))


# print('my name is %s, and i am %s years old, born in %s' %(name , age , country))


#  on plusieurs types comme ca , par exemple :
#  %s , %d , %f etc...


#  le %s ---- >  c'est pour le type STRING
#  le %d ---- >  c'est pour le type NUMBERS
#  le %f ---- >  c'est pour le type FLOAT

#   les autres sont similaires à ce que l'on peut trouver sur  internet


# on peut preciser, demander plus de precision . on va ajouter (.) apres le %
# par exemple :

print('i am %.3f years old' %age)  # -----> i am 17.000 years old

print('my name is %.4s ' % name)   # -----> my name is hass 



# d signifie qu'il y aura la partie décimale dans notre
# nombre
# après la virgule



# pour afficher des nombres avec une virgule et un espace.
# Exemple:
# "123456789,0" devient "1 234 567 890".