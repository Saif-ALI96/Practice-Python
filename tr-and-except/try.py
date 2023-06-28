#  on va utiliser le try et except en python
# par exemple

# num = int(input('enter number: '))
# #on demande à l'utilisateur d'entrer un nombre entier
# # , il peut y avoir des espaces entre les chiffres.
# print(num)
# # ---->     num = int(input('enter number: '))
#         #   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ValueError: invalid literal for int() with base 10: '23.3

# print('hello')
# si l'utilisateur mettre un number float ou un string, on va avoir une errure 
# et le rest de code ne serait jamais excuter 
# dans ce cas la, on va utiliser le try() et except pour intercepter cette erreur

# par exemple 

try :
     num = int(input("entrez votre numero: "))
     print(num)
except ValueError as error: #----> except d'une maniere generale 
     print ("valueError")

except:
     print ("autre type d'error ")


print ('bonjour tout le monde!')



