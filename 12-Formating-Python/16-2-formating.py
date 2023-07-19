

#  nous allons voir la deuxième méthode avec le formating  de string.
# format() qui est plus simple et facile à utiliser que les autres:

#  par exemple:


age = 25
name ="John"
country = "France"


print("Hello, {}!".format(name)) # Hello John ! 

print("{} is {} years old.".format(name, age) )   # John is 25 years old .

#  pour cibler un lettre dans le string ou numbre , on va l'ajouter dans les parentheses
# par exemple: 

print('hello {:.2s}' .format(name))  # hello Jo

#  on peut meme ecrire autre chose que le vraible declarer avant :

print('{} {}'.format(10+3*4,'bonjour'))    # output: 22 bonjour

#  on peut separer les chiffres par des vergules pour que ce soit plus visible et moins difficile a lire

print('The price is {:,}' .format(1000000))  # The price is 1,000,000



#  maintenant on voir comment peut on disposer les element avec le .format():
#  par exemple:

num1 = 23
num2 = 53
num3 = 64

print('the number is {} {} {}'.format(num1,num2,num3))  # the number is 23 53 64

#  si nous souhaitons deplacer les numbers , on prend le systeme du tableau 
# car en python (les index commence toujours a zero), donc :

print('the number is {2} {0} {1}'.format(num1,num2,num3))  # the number is 64 23 53

#  le %s ---- >  c'est pour le type STRING
#  le %d ---- >  c'est pour le type NUMBERS
#  le %f ---- >  c'est pour le type FLOAT

# meme on peut changer le type du numbre au lieu d'un int a float par exemple:
#   
print('the number is {2:.2f} {0:d} {1:.2f}'.format(num1,num2,num3))   # the number is 64.00 23 53.00

 