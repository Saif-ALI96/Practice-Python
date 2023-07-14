#  on peut ecrire dans le ficher a partir de notre ficher python

#  r , r+ , w , w+ , a , a+ 
# mode d’ouverture des fichiers sur Python est très similaire aux modes utilisés
# dans les autres langages informatiques tels que C/C++, Java et PHP.

# - Le mode ‘r’ permet de lire une portion fixée du contenu d’un fichier existant sans modifier son état actuel;
# il sert par exemple à afficher le contenue d’une page web.
# par exemple:

# filles = open('files-in-python/15-2-write.txt', 'r')
# print(filles.read()) #----> pour lire le contenu
# filles.close()

# - Le mode ‘r+’ permet de lire et d’écrire dans un fichier
# existant tout en conservant l’état initial du fichier avant toute opération. 
# Il sera utile si vous souhaitez mettre à jour certains données présentes dans votre document pendant sa lecture.

# filles = open('files-in-python/15-2-write.txt', 'r+')
# print( filles.write('hello sir'))
# # pour ajouter dans le fichier write.txt 

# filles.close()


# - Le mode ‘w’ crée un nouveau fichier vide qui ne possède pas
# encore été créé au cas où il existe déjà un fichier portant ce nom et efface tous ses anciens données. 
# Si le fichier n’existait pas, alors qu’il est demandé à être mis à jour en mode ‘w’, al 
#on obtient simplement un nouvel emplacement vide pour y stocker nos nouvelles informations.
# Ce mode est particulièrement adapté lorsque nous souhaitons créer un nouveau fichier completement vide.
#par exemple:

# filles = open('files-in-python/15-2-write.txt', 'w')
# print(filles.write("Hello World"))
# # -----> on va ajouter le contenu dans le fichier en supprimant tout le contenu deja existe
#         # on va trouver seulement le contenu qu'on vient l'ajouter 

# filles.close()

filles = open('files-in-python/15-3-write2.txt', 'w')
print(filles.write("Hello World"))
# ---->  on peut meme creer un nouveau fichier et ajouter du contenu 
filles.close()


# - Le mode ‘w+’ combine les caractéristiques des deux précédents modes en permettant de lire et d’écrire dans un fichier existant
# tout en supprimant complètement son contenu initiale. 
# On utilise cette option pour remplacer entièrement le contenu d’un fichier existant par de nous propres. 
# Par exemple, si vous avez besoin de réinitialiser un formulaire sur une page HTML, cela devra utiliser ce mode.



# - Le mode ‘a’ permet d’ajouter du contenu à la fin d’un fichier existant mais aussi de lire celui ci.
# L’utilisation de ce mode gardera intacts les parties non modifiées du fichier original.


# Enfin, le mode ‘a+’ combinera les capacités des trois premiers
# modaux en autorisant à la fois la lecture et l’écriture vers la suite du fichier.
# Il faut choisir le bon mode selon vos besoins et veiller à bien
# fermer le fichier après utilisation pour libérer les ressources système.
#  Exemples :
