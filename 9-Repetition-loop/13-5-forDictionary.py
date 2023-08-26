#  on va utilisre  le dictionary avec le loop for 
#   pour chaque valeur de la liste, il faut ajouter une clé et un item dans le dictionnaire.
#   
# - On peut utiliser l'opé rateur in afin d'avoir les valeurs qui sont présentes 
# dans deux listes ou dicts.

# par exemple

# liste = ['python', 'c#' , 'c++' , 'java' ,'javascript']

# for langues in range(len(liste)) :
#     print (liste[langues])
#python
# c#
# c++
# java
# javascript


liste_1 = ['python', 'c#' , 'c++' , 'java' ,'javascript']

for langues in range(len(liste_1)) :
    if liste_1[langues] == 'python':
          
        print (liste_1[langues], 'hello my new language of programation')
    else:
        print (liste_1[langues] )   

    # python hello my new language of programation
    #c#
    #c++
    #java
    #javascript



# nous allons voir le loop for avec le dictionary

dico_langue = {
    'name': 'Saif',
     'age': '26',
     'cuntory' : 'Irak' }
for test in dico_langue:
    print (dico_langue[test]) #---> pour recuperer les valeurs qui se trouvent dans les cles de la dictionary

# name Saif
# age 26
# country Irak

# +
# on va maintenant créer notre propre fonction
def afficher_nom():
    
    nom = input('Entrez votre prenom ')
    return nom  
afficher_nom()
print ('bonjour ', afficher_nom())


