



#Pour arrondir les nombres, nous devons utiliser
#la fonction round()  (عمليه تقريب الاعداد العشريه)
#La syntaxe est la suivante:

print(round(13.5)) #----> nous aurons le chiffre 14 
print(round(9.4)) # ----> nous aurons le chiffre 9
'''
# de 0 jusque a 4 le number reste tel qu'il est 
# de 5 jusque a 9 le number agumente a la prochain chiffre 
# et on continue avec cette methode pour chaque nombre entier qui suit...
#pour afficher tous les resultats des numeros entiers entre -7 et
#-1 incluant il faut ecrire une boucle for'''
#  par exemple :
'''
for i in range(2,6):    

    print(i,round(float((abs(i)+1.0))))
    
'''

